#이륜자동차 안전 위험 시설물 데이터
#annotation 파일의 label 명을 COCO_CLASSES 파일에 있는 클래스 중 하나인 "puddle" 로 바꾸는 코드
import os
import json

IMAGE_DIR = ""
ANNOT_DIR = "C:/Users/Justin Moon/BlackIce/183.이륜자동차 안전 위험 시설물 데이터/01.데이터/2.Validation/라벨링데이터_230222_add/VL_Bounding Box_27.침수구간"

lst = os.listdir(ANNOT_DIR)
print(lst)
for item in lst:
    with open(ANNOT_DIR + "/" + item, 'r', encoding="UTF8") as f:
        json_data = json.load(f)
        json_data["annotation"][0]["label"] = "puddle"
        with open(ANNOT_DIR + "/" + item, 'w') as file:
            json.dump(json_data, file)
        

