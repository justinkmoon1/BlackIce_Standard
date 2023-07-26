import os
import json

path_dir = "datasets/183.이륜자동차 안전 위험 시설물 데이터/01.데이터/1.Training/라벨링테이터_230222_add/TL_Bounding Box_27.침수구간"
weather = {}
time = {}
file_list = os.listdir(path_dir)
for f in file_list:
    with open(path_dir + "/" + f, 'r', encoding="UTF8") as file:
        json_data = json.load(file)
        if json_data["images"]["collect_weather"] in weather:
            weather[json_data["images"]["collect_weather"]] += 1
        else:
            weather[json_data["images"]["collect_weather"]] = 1

        if json_data["images"]["collect_time"][:2] in time:
            time[json_data["images"]["collect_time"][:2]] += 1
        else:
            time[json_data["images"]["collect_time"][:2]] = 1

time = sorted(time.items())
print("weather: ", weather)

print("time: ", time)
    

    