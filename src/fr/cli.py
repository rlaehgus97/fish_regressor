from weightpd import lr_api
from fishclass import knn_api

# length를 받아 weight를 예측해서 return함
def predict():
    length = float(input("물고기의 길이를 입력하시오: "))
    
    # weight 예측 선형회귀 api 호출
    weight = lr_api(length)
    print(f"물고기 무게를 예측한 결과 {weight}가 나왔습니다")

    # 물고기 분류 api 호출
    fish_class = knn_api(length, weight)
    print(f"length:{length}의 길이를 가진 물고기는 무게가 weight:{weight}로 예측되며 종류는 {fish_class}로 예측됩니다")

