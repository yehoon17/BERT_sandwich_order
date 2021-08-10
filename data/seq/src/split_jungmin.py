# 데이터를 훈련, 테스트, 검증 8:1:1로 나눔
from sklearn.model_selection import train_test_split

# seq_in, seq_out, 랜덤값
def split(seq_in, seq_out, random_state=None):
    # 80:20 나눔
    X_train, X_test_20, y_train, y_test_20 = train_test_split(
        seq_in, seq_out, test_size=0.2, random_state=random_state)
    # 나눈 20을 10:10 나눔
    X_test, X_valid, y_test, y_valid = train_test_split(
        X_test_20, y_test_20, test_size=0.5, random_state=random_state)
    
    # 리턴값: X_훈련, y_훈련, X_테스트, y_테스트, X_검증, y_검증
    return X_train, y_train, X_test, y_test, X_valid, y_valid

# X_train, y_train, X_test, y_test, X_valid, y_valid = split(seq_in, seq_out, 42)
