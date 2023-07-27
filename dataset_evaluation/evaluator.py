#TODO
"""
implement calculation of metrics (AP, f1 score, etc) from confusion matrix
"""

from tools.demo import Predictor
from yolox.exp.build import get_exp
from yolox.models.yolox import YOLOX
from yolox.utils.boxes import bboxes_iou

import numpy as np
import torch
import json

class Evaluator():
    def __init__(self, img_path, annot_path, model_path):
        self.num_class = 5
        self.img_path = img_path
        self.annot_path = annot_path
        self.model_path = model_path

        # class 에 대한 cnts
        self.cnts = {0: [0, 0], 1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0]}
        # 전체 fp
        self.fp_cnts = {0: 0, 1: 0, 2:0, 3:0, 4:0, 5:0}

    def read_data(self, img, idx):
        with open(self.annot_path, 'r') as f:
            json_data = json.load(f)
            actual_list = []
            actual_label = []
            for bbox in json_data["annotations"]:
                if bbox["image_id"] == idx:
                    actual_list.append(bbox["bbox"])
                    actual_label.append(bbox["category_id"])
            return actual_list, actual_label


    def prediction_process(self, prediction_dict_list, information):
        if prediction_dict_list == None:
            pass
        prediction_dict_list = prediction_dict_list.cpu()
        ratio = information["ratio"]
        bboxes = prediction_dict_list[:, :4]
        bboxes /= ratio
        cls = prediction_dict_list[:, 6]
        bboxes = list(bboxes)
        cls = list(cls)
        return bboxes, cls
    

    def predict(self, img, model):
        return model.inference(img)


    # pred + gt 정보 evaluator 객체에 저장
    def put_data(self, prediction_bbox, prediction_class, actual_bbox, actual_class):
        actual_label_list = []
        actual_bbox_list = []
        
        pred_label_list = []
        pred_bbox_list = []

        # prediction
        for i in range(len(prediction_bbox)):
            # label, bbox 정보 추가
            pred_bbox_list.append(list(map(float, prediction_bbox[i])))
            pred_label_list.append(int(prediction_class[i]))
            label = pred_label_list[i]
            #print(pred_bbox_list, pred_label_list)
            #print(int(label))
            # 하나의 class에 대한 tp, fp, 전체 fp
            try:
                self.cnts[int(label)]
            except:
                self.cnts[int(label)] = np.array([0, 0])
                self.fp_cnts[int(label)] = np.zeros(self.num_class)
        # gt
        for j in range(len(actual_bbox)):
            # label, bbox 정보 추가
            actual_bbox_list.append(actual_bbox[j])
            actual_label_list.append(actual_class[j])
            label = actual_class[j]

            # 하나의 class에 대한 tp, fp, 전체 fp
            try:
                self.cnts[int(label)]
            except:
                self.cnts[int(label)] = np.array([0, 0])
                self.fp_cnts[int(label)] = np.zeros(self.num_class)

        #print(actual_bbox_list)
        #print(len(pred_label_list), len(pred_bbox_list))
        self.count_result(actual_label_list, actual_bbox_list, pred_label_list, pred_bbox_list, 0.5)

    def count_result(self, actual_label_list, actual_bbox_list, pred_label_list, pred_bbox_list, iou_thr):
        
        # prediction bbox 를 for loop 돌면서 actual 랑 비교
        for i, pred_bbox in enumerate(pred_bbox_list):
            # iou 비교 
            for j, actual_bbox in enumerate(actual_bbox_list):
                print(pred_bbox, actual_bbox)
                iou = self.calc_iou(pred_bbox,actual_bbox)
                print(iou)
                # label이 같으면 tp. 아니면 fp
                if iou > iou_thr:
                    #print(iou)
                    if pred_label_list[i] == actual_label_list[j]:
                        self.cnts[pred_label_list[i]][1] += 1
                    else:
                        self.cnts[pred_label_list[i]][0] += 1
                        
                        self.fp_cnts[pred_label_list[i]] += 1

        
    
    # self.cnts 로 ap 계산
    def get_results(self):
        pass


    def calc_iou(self, a, b):
        pred_box_area = (a[2] + 1) * (a[3] + 1)
        actual_box_area = (b[2] + 1) * (b[3] + 1)
        #print("pred_box area: " + str(pred_box_area))
        #print("actual_box_area: " + str(actual_box_area))
        x1 = max(a[0], b[0])
        y1 = max(a[1], b[1])
        x2 = min(a[0] + a[2], b[0] + b[2])
        y2 = min(a[1] + a[3], b[1] + b[3])

        w = max(0, x2 - x1 + 1)
        h = max(0, y2 - y1 + 1)

        inter = w * h
        iou = inter / (pred_box_area + actual_box_area - inter)
        return iou
"""
    def  _count_res(self, pred_bboxes, pred_labels, actual_bboxes, actual_labels, iou_thr):
        if len(pred_labels) == 0 or len(actual_labels) == 0:
            return 0
        
        for i, pred_box in enumerate(pred_bboxes):
            pred_box_list = []
            for t in pred_box:
                pred_box_list.append(float(t))
            for j, actual_bbox in enumerate(actual_bboxes):
                #actual_bbox_list = torch.FloatTensor(actual_bbox)
                #print(pred_box)
                #print("##########")
                #print(actual_bbox)
                iou = self.calc_iou(pred_box_list, actual_bbox)
                #iou = bboxes_iou(pred_box, actual_bbox_list)
                
                #print(iou)
                #print(pred_box_list, actual_bbox)
                if iou > iou_thr:
                    print("Success!")
                    print(int(pred_labels[i]), actual_labels[j])
                    if pred_labels[i] == actual_labels[j]:
                        # 해당 클래스 TP 1 추가
                        #self.TP_List[int(pred_labels[i])] += 1
                        return ["TP", int(pred_labels[i])]
                    else:  # 해당 클래스 FP 1 추가
                        #self.FP_List[int(pred_labels[i])] += 1
                        return ["FP", int(pred_labels[i])]
                        #전체 FP의 카운팅 1 증가
                        #self.Whole_FP[int(pred_labels[i])] += 1
                #precision: TP / (TP + FP)
                #recall: TP / (TP + FN)
                else:
                    continue"""