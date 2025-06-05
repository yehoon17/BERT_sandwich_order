# BERT_sandwich_order

BERT 기반 슬롯 태깅 모델을 이용해 샌드위치 주문을 처리하는 챗봇 데모 프로젝트입니다. 
사용자가 입력한 문장을 분석해 주문 정보를 추출하고, 대화형 키오스크 환경을 구축하는 것이 목표입니다.

## 목차
1. [프로젝트 주제](#프로젝트-주제)
2. [서비스 기획 목적](#서비스-기획-목적)
3. [프로젝트 구현 과정](#프로젝트-구현-과정)
4. [의존성](#의존성)
5. [실행 방법](#실행-방법)

## 프로젝트 주제
샌드위치 주문 시나리오를 BERT 모델의 슬롯 태깅 방식으로 구현합니다.

## 서비스 기획 목적
- 사회적 약자(장애인, 노인, 아동 등)도 쉽게 주문할 수 있도록 키오스크 사용의 어려움을 해결합니다.
  > 기존 키오스크 주문이 어려움을 해소하고 원활한 서비스를 위해 대화형 시나리오를 설계합니다.
- 사용자의 메시지를 분석해 필요한 주문 정보를 추출합니다.

## 프로젝트 구현 과정
1. **데이터 수집**
   - 실제 프랜차이즈 메뉴(서브웨이) 프로세스를 참고하여 질문 패턴을 작성합니다.
   - 상황별 예상 질문을 직접 작성하거나 코드로 생성해 데이터 양을 늘립니다.
2. **데이터 전처리**
   - 수집한 데이터를 슬롯 필링 포맷(Goo et al., 2018)에 맞춰 `seq.in`/`seq.out` 파일로 만듭니다.
   - ETRI에서 제공하는 BPE 토크나이저를 사용합니다.
3. **Fine-tuning**
   - ETRI 한국어 BERT 사전학습 모델을 기반으로 슬롯 태깅 모델을 학습합니다.
   - 하이퍼파라미터를 조정하며 모델을 수정·보완합니다.
4. **웹 서비스 구축**
   - Flask로 웹 애플리케이션을 제작하고 모델과 결합하여 테스트합니다.

## 의존성
```
tensorflow==1.15
h5py==2.10.0
flask-ngrok==0.0.25
```

## 실행 방법
1. **데이터 생성**
   - `data/generate/data_merge.py` 실행 시 `data/seq/resources/data.txt`가 생성됩니다.
2. **데이터 전처리**
   - `data/seq/data_to_seq.py` 실행 시 `seq_in.txt`과 `seq_out.txt`가 `data/seq/resources`에 생성됩니다.
3. **데이터셋 분리**
   - `split.py`의 `Spliter` 클래스를 사용해 train/validation/test 세트를 8:1:1로 분리합니다.
4. **korBERT 모듈 생성**
   - ETRI 사전학습 BERT 체크포인트로 모듈을 생성합니다.
   - 예시: `python export_korbert/bert_to_module.py -i /content/drive/MyDrive/004_bert_eojeol_tensorflow -o /content/drive/MyDrive/bert-module`
5. **Fine-tuning**
   - 적절한 epoch와 batch size를 설정해 Fine-tuning을 진행합니다.
   - 예시: `python train.py -t data/seq/resources/seq_in_train.txt -v data/seq/resources/seq_in_valid.txt -s saved_model -e 10 -bs 10`
6. **모델 평가**
   - 예시: `python eval.py -m saved_model -d data/seq/resources`
   - 결과는 `test_results` 폴더에 저장됩니다.
7. **Inference**
   - 임의의 문장을 입력해 추론을 수행합니다.
   - 예시: `python inference.py --model saved_model`
8. **Web Application**
   - `python web_demo/run.py` 실행
   - Colab에서 실행하려면 `flask-ngrok` 패키지가 필요합니다.
   - 자세한 내용은 `web_demo/README.md` 참고

