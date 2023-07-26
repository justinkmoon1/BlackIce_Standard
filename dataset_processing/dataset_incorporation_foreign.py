#이륜자동차 안전 위험 시설물 데이터
#coco 형식에 맞게 학습시킬 수 있는 한 파일로 만들도록 하는 코드
import os
import json
IMAGE_DIR = ""
ANNOT_DIR = ""
NEW_ANNOT_PATH = ""
cur_id = 0
with open(NEW_ANNOT_PATH, 'r') as f:
    json_data = json.load(f)
    cur_id = json_data["images"][-1]["id"]
    for item in os.listdir(ANNOT_DIR):
        with open(ANNOT_DIR + "/" + item, 'r') as file:
            annotations = json.load(file)
            image_dict = {}
    json_data["images"].append(dict)