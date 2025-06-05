# 챗봇 웹 데모

Flask로 구현된 웹 애플리케이션에서 샌드위치 주문 챗봇을 체험할 수 있습니다. `run.py`를 실행하면 로컬 서버가 시작됩니다.

## 목차
1. [설치](#설치)
2. [실행](#실행)
3. [사용 예시](#사용-예시)
4. [저작권](#저작권)

## 설치
필요한 패키지를 다음과 같이 설치합니다.
```bash
pip install -r requirements.txt
```

## 실행
아래 명령으로 웹 서버를 실행합니다.
```bash
python run.py
```
기본 포트는 5000이며 Colab에서 사용할 경우 `flask-ngrok`을 통해 공개 URL이 생성됩니다.

## 사용 예시
### 초기 화면
실행 후 첫 화면입니다.  
<img width="600" alt="test1" src="https://user-images.githubusercontent.com/56901668/130546260-5ce532da-d0d3-4dba-9689-173049719dab.png">

### `!` 명령어
`!`와 명령어를 조합해 사용법을 확인할 수 있습니다.  
<img width="600" alt="test2" src="https://user-images.githubusercontent.com/56901668/130546285-b288f5ca-341a-409b-9a28-63d45f32799f.png">

### 명령어 예시
`!빵`을 입력하면 선택 가능한 빵 종류가 표시됩니다.  
<img width="600" alt="test3" src="https://user-images.githubusercontent.com/56901668/130546301-8409c8c3-8e4d-43d9-826f-0fc0b96bc572.png">

### 주문 흐름
채소와 길이 등 누락된 정보를 물어본 뒤 주문 여부를 확인합니다.  
<img width="600" alt="test4" src="https://user-images.githubusercontent.com/56901668/130546322-b36a2bdb-3a98-44b2-b4f2-3555c00640c5.png">

### 주문 종료
토스팅 여부까지 확인하면 시나리오가 마무리됩니다.  
<img width="600" alt="test5" src="https://user-images.githubusercontent.com/56901668/130546331-610fc967-df20-47df-88a3-c4ac56749b9d.png">

## 저작권
웹 구현에 사용된 모든 로고와 이미지는 서브웨이의 저작물입니다.
