from tools.demo import Predictor
from yolox.exp.build import get_exp
from yolox.models.yolox import YOLOX
from yolox.utils.boxes import bboxes_iou

import torch

class Evaluator():
    def __init__(self, img_path, annot_path, model_path):
        self.img_path = img_path
        self.annot_path = annot_path
        self.model_path = model_path
    
    def predict(self, img, model):
        
        return model.inference(img)

    #def demo():

    
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
                    continue
        

