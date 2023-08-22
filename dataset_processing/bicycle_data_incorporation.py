import os
import json
data_dir = "183.이륜자동차 안전 위험 시설물 데이터/01.데이터/1.Training/라벨링테이터_230222_add/TL_Bounding Box_27.침수구간"
file_list = os.listdir(data_dir)
new_annot_dict = {"info":{},"licenses":[{}], "categories":[{"id":0, "name": "blackice", "supercategory":"none"}, {"id":1, "name": "puddle", "supercategory":"none"}, {"id":2, "name": "slush", "supercategory":"none"}, {"id":3, "name": "snow", "supercategory":"none"}, {"id":4, "name": "rain", "supercategory":"none"}],"images":[], "annotations":[]}
cur_id = 0
annot_id = 0
for f in file_list:
    with open(data_dir + "/" + f, 'r', encoding='UTF8') as annot:
        json_data = json.load(annot)
        d = {"id": cur_id, "file_name": f[:-4] + "png", "height": json_data["images"]["height"], "width" : json_data["images"]["width"]}
        ann = {"id": annot_id, "image_id": cur_id, "category_id": 1}
        for a in json_data["annotation"]:
            ann["bbox"] = a["bbox"]
            annot_id += 1
        new_annot_dict["images"].append(d)
        new_annot_dict["annotations"].append(ann)
        cur_id += 1
with open(data_dir + "/" + "annotation.json", 'w') as file:
    json.dump(new_annot_dict, file)        


