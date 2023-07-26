import os
import json
import cv2
import numpy as np
from dataset_evaluation.custom_evaluator import Evaluator
from yolox.models.yolox import YOLOX
import torch
from yolox.exp.build import get_exp

DATA_PATH = "C:/Users/Justin Moon/BlackIce/blackice3.v1i.coco/train"
ANNOT_PATH = "C:/Users/Justin Moon/BlackIce/blackice3.v1i.coco/annot/_annotations.coco.json"
MODEL_PATH = "C:/Users/Justin Moon/BlackIce/YOLOX_outputs/yolox_tiny/latest_ckpt.pth"

img_list = os.listdir(DATA_PATH)
evaluator = Evaluator(DATA_PATH, ANNOT_PATH, MODEL_PATH)
with open(ANNOT_PATH, 'r') as f:
        json_data = json.load(f)
TP_List = [0 for i in range(6)]
FP_List = [0 for i in range(6)]
Whole_FP = [0 for i in range(6)]
model = YOLOX()
saved_checkpoint = torch.load(MODEL_PATH)
model.load_state_dict(saved_checkpoint, strict = False)
model.eval()
exps = get_exp("C:/Users/Justin Moon/BlackIce/exps/default/yolox_tiny.py")
predictor = Predictor(exp = exps, model = model)

for i in range(len(img_list)):
    if i > 0:
        quit()
    prediction_list, info = evaluator.predict(DATA_PATH + "/" + img_list[i])
    #prediction_list, info = evaluator.predict("blackice3.v1i.coco/train/dd77fb60-2min_jpg.rf.9fcaac62c6214e61d2250433d7ed50a4.jpg")

    actual_list = []
    actual_label = []
    for bbox in json_data["annotations"]:
          if bbox["image_id"] == i:
                actual_list.append(bbox["bbox"])
                actual_label.append(bbox["category_id"])
    ratio = info["ratio"]
    img = info["raw_img"]
    prediction_list = prediction_list[0].cpu()
    bboxes = prediction_list[:, 0:4]
    
    bboxes /= ratio
    cls = prediction_list[:, 6]
    bboxes = list(bboxes)
    cls = list(cls)
    #print(bboxes[0], actual_list)
    #print(cls)
    lst = evaluator._count_res(bboxes, cls, actual_list, actual_label, 0.1)
    try:
        if lst[0] == "TP":
            TP_List[lst[1]] += 1
        else:
            FP_List[lst[1]] += 1
            Whole_FP[lst[1]] += 1
    except:
        continue
print(TP_List)
print(FP_List)
print(Whole_FP)

#print(evaluator.results())