# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from sklearn import metrics
import tensorflow as tf
import os, pickle, re
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
# 코랩에서 실행 시
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
    text_arr = tokenizer.tokenize(userText)
    input_ids, input_mask, segment_ids = bert_to_array.transform([" ".join(text_arr)])

    # 예측
    with graph.as_default():
        with sess.as_default():
            inferred_tags, slots_score = model.predict_slots(
                [input_ids, input_mask, segment_ids], tags_to_array
            )

    # 결과 체크
    print("text_arr:", text_arr)
    print("inferred_tags:", inferred_tags[0])
    print("slots_score:", slots_score[0])

    # 슬롯에 해당하는 텍스트를 담을 변수 설정
    sandwich_text = ""
    length_text = ""
    bread_text = ""
    cheese_text = ""
    sauce_text = ""
    vegetable_text = ""
    topping_text = ""

    # 슬롯태깅 실시
    for i in range(0, len(inferred_tags[0])):
        if slots_score[0][i] >= app.score_limit:
            if inferred_tags[0][i] == "sandwich":
                sandwich_text += text_arr[i]
                app.slot_dict["sandwich"] = re.sub("_", "", sandwich_text)

            elif inferred_tags[0][i] == "length":
                length_text += text_arr[i]
                app.slot_dict["length"] = re.sub("_", "", length_text)

            elif inferred_tags[0][i] == "bread":
                bread_text += text_arr[i]
                app.slot_dict["bread"] = re.sub("_", "", bread_text)

            elif inferred_tags[0][i] == "cheese":
                cheese_text += text_arr[i]
                app.slot_dict["cheese"] = re.sub("_", "", cheese_text)

            elif inferred_tags[0][i] == "sauce":
                sauce_text += text_arr[i]
                app.slot_dict["sauce"] = re.sub("_", "", sauce_text)

            elif inferred_tags[0][i] == "vegetable":
                vegetable_text += text_arr[i]
                app.slot_dict["vegetable"] = re.sub("_", "", vegetable_text)

            elif inferred_tags[0][i] == "topping":
                topping_text += text_arr[i]
                app.slot_dict["topping"] = re.sub("_", "", topping_text)
        else:
            print("something went wrong!")

    print(app.slot_dict)

    return "hi"  # 챗봇이 이용자에게 하는 말을 return


###############################################################################
