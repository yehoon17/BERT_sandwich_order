# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from sklearn import metrics
import tensorflow as tf
import os, pickle
import sys

sys.path.append(os.path.join(os.getcwd(), "bert_slot_kor"))
from to_array.bert_to_array import BERTToArray
from models.bert_slot_model import BertSlotModel
from to_array.tokenizationK import FullTokenizer

print(os.getcwd())

graph = tf.compat.v1.get_default_graph()

# enable GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.ConfigProto(
    intra_op_parallelism_threads=1,
    inter_op_parallelism_threads=1,
    allow_soft_placement=True,
    device_count={"CPU": 1},
)
sess = tf.compat.v1.Session(config=config)

# pretrained model path - 로컬에서 실행시 따로 다운로드 받아야함
# bert_model_hub_path = os.path.join(os.getcwd(), "bert-module")
bert_model_hub_path = "/content/drive/MyDrive/bert-module"

# fine-tuned model path - 로컬에서 실행시 따로 다운로드 받아야함
# load_folder_path = os.path.join(os.getcwd(), "save")
load_folder_path = "/content/drive/MyDrive/save"

# tokenizer vocab file path
vocab_file = os.path.join(bert_model_hub_path, "assets/vocab.korean.rawtext.list")
bert_to_array = BERTToArray(vocab_file)

tags_to_array_path = os.path.join(load_folder_path, "tags_to_array.pkl")
with open(tags_to_array_path, "rb") as handle:
    tags_to_array = pickle.load(handle)
    slots_num = len(tags_to_array.label_encoder.classes_)

model = BertSlotModel.load(load_folder_path, sess)

tokenizer = FullTokenizer(vocab_file=vocab_file)

app = Flask(__name__)
run_with_ngrok(app)
app.static_folder = "static"


@app.route("/")
def home():
    # 슬롯 사전 만들기
    app.slot_dict = {
        "sandwich": None,
        "length": None,
        "bread": None,
        "cheese": None,
        "sauce": None,
        "vegetable": None,
        "topping": None,
    }
    # 점수제한
    app.score_limit = 0.8

    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg").strip()  # 사용자가 입력한 문장

    # 사용자가 입력한 문장을 토큰화
    input_text = " ".join(tokenizer.tokenize(userText))
    tokens = input_text.split()
    data_text_arr = list(input_text)
    data_input_ids, data_input_mask, data_segment_ids = bert_to_array.transform(
        data_text_arr
    )

    print("tokens:", tokens)
    print("data_text_arr:", data_text_arr)

    print(app.slot_dict)

    with graph.as_default():
        with sess.as_default():
            inferred_tags, slots_score = model.predict_slots(
                [data_input_ids, data_input_mask, data_segment_ids], tags_to_array
            )

    print("inferred_tags:", inferred_tags[0])
    print("slots_score:", slots_score[0])

    return "hi"  # 챗봇이 이용자에게 하는 말을 return


###############################################################################
