# BERT_sandwich_order  

## 목차
 - [프로젝트 주제](#프로젝트-주제)  
 - [서비스 기획 목적](#서비스-기획-목적)
 - [프로젝트 구현 과정](#프로젝트-구현-과정)
 - [의존성](#의존성)
 - [실행 방법](#실행-방법)

## 프로젝트 주제 

- BERT 기반 슬롯태깅 모델을 이용해서 샌드위치 주문 챗봇을 구현하는 프로젝트입니다.  

## 서비스 기획 목적

 - 사회적약자(장애인, 노인, 아동 등)의 사용이 어려움  
     > 기존 키오스크 주문이 어려움을 해소하기 위함  
     > 원활한 서비스를 위해서 대화형 시나리오를 설계  
 - 사용자의 메시지 분석을 통해 주문 과정을 구현  


## 프로젝트 구현 과정

 1. 데이터 수집  
    - 실제 프랜차이즈 메뉴(서브웨이)의 프로세스 이용
    - 상황에 따른 예상 질문 패턴 작성(직접작성 + 코드로 임의의 문장 작성)  
 2. 데이터 전처리
    - 구축한 데이터를 슬롯필링 데이터 포맷(Goo et al. (2018))에 맞추어 seq.in, seq.out을 생성
    - 토큰화를 위해 ETRI에서 BPE 알고리즘을 이용해 만든 토크나이저를 이용
 3. Fine-tuning
    - ETRI의 한국어 BERT 사전훈련 모델을 이용해서 모델 훈련 진행
    - Fine-tuning 모델 수정 및 보완하여 최적화 
 4. 서비스용 웹 구축
    - Flask를 이용한 웹 애플리케이션 제작
    - 모델과 웹을 결합하여 테스트

## 의존성
```
tensorflow == 1.15 
h5py == 2.10.0
flask-ngrok == 0.0.25
```


## 실행 방법
### 1. 데이터 생성
 - `data/generate`에 `data_merge.py`를 실행하면, `data.txt`가 `data/seq/resources`에 생성됨.

### 2. 데이터 전처리
 - `data/seq`에 `data_to_seq.py`를 실행하면, `seq_in.txt`과 `seq_out.txt`가 `data/seq/resources`에 생성됨.

### 3. 데이터셋 분리
 - `split.py`의 Spliter 클래스를 이용하여 seq_in과 seq_out을 train, test, validation set으로 8:1:1의 비율로 나누어 각각의 텍스트 파일에 담는다.

### 4. korBERT 모델을 모듈로 내보내기
 - ETRI에서 사전훈련한 BERT의 체크포인트를 가지고 BERT 모듈을 만든다.
 - 실행커맨드 예시: `python export_korbert/bert_to_module.py -i /content/drive/MyDrive/004_bert_eojeol_tensorflow -o /content/drive/MyDrive/bert-module`

### 5. Fine-tuning
 - 적절한 epoch와 batch_size를 설정하여 Fine-tuning 훈련을 진행한다.
 - 실행커맨드 예시: `python train.py -t /data/seq/resources/seq_in_train.txt -v /data/seq/resources/seq_in_valid.txt -s /saved_model_path -e 10 -bs 10`

### 6. 모델 평가
 - 훈련된 모델을 평가한다.
 - 실행커맨드 예시: `python eval.py -m /load_folder_path -d /data_folder_path`
 - 테스트의 결과는 --model에 넣어준 모델 경로 아래의 `test_results`에 저장된다.

### 7. Inference
 - 훈련된 모델을 임의의 데이터를 입력해서 추론을 시켜보기
 - 실행커맨드 예시: `python inference.py --model {훈련된 모델이 저장된 경로}`
 - "Enter your sentence:"라는 문구가 나오면 모델에 넣어보고 싶은 문장을 넣어 주면 됨
 - quit를 입력하면 종료된다.

### 8. Web Application
 - `python web_demo/run.py`로 실행
 - Colab에서 실행하기 위해서는 flask-ngrok패키지가 설치되어 있어야한다.
 - 실제 구현은 `web_demo`의 readme 참고
