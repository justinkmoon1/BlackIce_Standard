import json
import os

path_dir = 'BlackIce/datasets/COCO/val2017'

with open('BlackIce/datasets/COCO/annotations/instances_val2017.json', 'r') as f:
    json_data = json.load(f)
file_list = os.listdir(path_dir)
#file_lst = file_list[:301]

print(len(file_list))
print(len(json_data['images']))
#print(json_data['images'])
i = 4999
while len(json_data["images"]) > 301:
    if json_data["images"][i]["file_name"] not in file_list:
        del json_data["images"][i]
    i -= 1

with open('BlackIce/datasets/COCO/annotations/instances_val2017.json', 'w') as file:
    json.dump(json_data, file)
#for l in file_list[301:]:
#    os.remove(path_dir + "/" + l)