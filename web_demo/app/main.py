# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import os, pickle
from to_array.bert_to_array import BERTToArray
from models.bert_slot_model import BertSlotModel
from to_array.tokenizationK import FullTokenizer
from sklearn import metrics

import tensorflow as tf

# enable GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.ConfigProto(
    intra_op_parallelism_threads=1,
    inter_op_parallelism_threads=1,
    allow_soft_placement=True,
    device_count={"CPU": 1},
)
sess = tf.compat.v1.Session(config=config)

# model path
bert_model_hub_path = "/content/drive/MyDrive/bert-module"
is_bert = True

# fine-tuned model path
load_folder_path = "/content/drive/MyDrive/save"

# tokenizer vocab file path
vocab_file = os.path.join(bert_model_hub_path, "assets/vocab.korean.rawtext.list")
bert_to_array = BERTToArray(is_bert, vocab_file)

tags_to_array_path = os.path.join(load_folder_path, "tags_to_array.pkl")
with open(tags_to_array_path, "rb") as handle:
    tags_to_array = pickle.load(handle)
    slots_num = len(tags_to_array.label_encoder.classes_)

model = BertSlotModel.load(load_folder_path, sess)

tokenizer = FullTokenizer(vocab_file=vocab_file)


app = Flask(__name__)
app.static_folder = "static"


@app.route("/")
def home():

    ############################### TODO ##########################################
    # 슬롯 사전 만들기
    app.slot_dict = {
        "sandwich": None,
        "bread": None,
        "cheese": None,
        "sauce": None,
        "vegetable": None,
        "topping": None,
    }
    ###############################################################################

    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg").strip()  # 사용자가 입력한 문장

    ############################### TODO ##########################################
    # 1. 사용자가 입력한 한 문장을 슬롯태깅 모델에 넣어서 결과 뽑아내기
    # 2. 추출된 슬롯 정보를 가지고 더 필요한 정보 물어보는 규칙 만들기 (if문)
    app.slot_dict["a_slot"] = ""
    print(app.slot_dict)

    return "hi"  # 챗봇이 이용자에게 하는 말을 return


###############################################################################
