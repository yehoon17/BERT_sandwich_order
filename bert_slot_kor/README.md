# 버트 미세조정 - 슬롯 태깅

샌드위치 주문 데이터를 이용해 한국어 BERT를 슬롯 태깅 방식으로 미세조정합니다.

## 목차
1. [KorBERT 모듈 내보내기](#korbert-모듈-내보내기)
2. [데이터 준비](#데이터-준비)
3. [Fine-tuning](#fine-tuning)
4. [모델 평가](#모델-평가)
5. [Inference](#inference)
6. [Todo List](#todo-list)

## KorBERT 모듈 내보내기
ETRI가 공개한 체크포인트에서 BERT 모듈을 생성합니다.

```bash
python export_korbert/bert_to_module.py -i <체크포인트 디렉터리> -o <output 디렉터리>
```

예시:
```bash
python export_korbert/bert_to_module.py -i /content/drive/MyDrive/004_bert_eojeol_tensorflow -o /content/drive/MyDrive/bert-module
```

## 데이터 준비
모델 학습을 위한 `seq.in`과 `seq.out` 파일을 생성합니다.

- 슬롯 유형을 정의하고 문장 템플릿을 작성한 뒤 `data.txt`로 저장합니다.
- `seq.py`의 `Seq` 클래스로 슬롯을 추출하여 `seq_in.txt`와 `seq_out.txt`를 만듭니다.
- `split.py`의 `Spliter` 클래스를 사용해 train/validation/test 세트를 8:1:1로 나눕니다.

## Fine-tuning
인자값으로 학습 데이터 경로와 epoch, batch size 등을 입력하여 BERT 모델을 미세조정합니다.

```bash
python train.py -t data/seq/resources/seq_in_train.txt -v data/seq/resources/seq_in_valid.txt -s saved_model -e 50 -bs 10
```

## 모델 평가
훈련된 모델과 평가용 데이터를 입력해 성능을 확인합니다.

```bash
python eval.py -m saved_model -d data/seq/resources
```
평가 결과는 `test_results` 폴더에 저장됩니다.

## Inference
임의의 문장을 모델에 넣어 예측 결과를 확인할 수 있습니다.

```bash
python inference.py --model saved_model
```
프롬프트에 문장을 입력하면 슬롯 태깅 결과를 확인할 수 있으며 `quit`을 입력하면 종료됩니다.

## Todo List
- **eval.py**
  - [x] 경로 고치기
  - [x] test set 데이터 불러오기
- **inference.py**
  - [x] 필요한 모듈 불러오기
  - [x] 경로 고치기
  - [x] 모델과 기타 필요한 것들 불러오기
  - [x] 사용자가 입력한 한 문장을 슬롯태깅 모델에 넣어서 결과 뽑아내기
- **train.py**
  - [x] 경로 고치기
  - [x] validation data 불러오기
  - [x] train set과 validation set을 둘 다 넣어서 model.fit 하기
- **utils.py**
  - [x] seq.in과 seq.out을 읽어들여서 리스트로 만들기
- **models/bert_slot_model.py**
  - [x] y_slots를 이용하여 slots_score를 만들기
  - [x] history_dict에 기록된 loss 변화 추이를 이미지로 저장하는 함수 만들기
