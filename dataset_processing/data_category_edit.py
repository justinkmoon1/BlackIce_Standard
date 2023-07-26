import json
import os

PATH_DIR = 'C:/Users/Justin Moon/BlackIce/datasets/COCO/annotations'
FILE_NAME = "_annotations.coco.json"
with open(PATH_DIR + "/" + FILE_NAME, 'r') as f:
    json_data = json.load(f)
    for item in json_data['annotations']:
        item["category_id"] -= 1

    with open(PATH_DIR + "/" + FILE_NAME, 'w') as file:
        json.dump(json_data, file)