import os
import json
data_dir = ""
file_list = os.listdir(data_dir)
new_annot_dict = {"info":{},"licenses":[{}], "categories":[{"id":0, "name": "blackice", "supercategory":"none"}, {"id":1, "name": "puddle", "supercategory":"none"}, {"id":2, "name": "slush", "supercategory":"none"}, {"id":3, "name": "snow", "supercategory":"none"}, {"id":4, "name": "rain", "supercategory":"none"}],"images":[], "annotations":[]}
cur_id = 0
for f in file_list:
    with open(data_dir + "/" + f, 'r') as annot:
        json_data = json.load(annot)
        


