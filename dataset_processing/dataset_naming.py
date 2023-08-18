"""- 실제 예시
    
    indoor custom
    
    ID_SN_YYYYMMDDTHHMMSS_frame
    
    outdoor custom
    
    OD_CL_YYYYMMDDTHHMMSS_frame
    
    외부데이터
    
    O_CL_YYYYMMDDTHHMMSS_frame
    
    O_SN_YYYYMMDDTHHMMSS_frame
    
    O_RN_YYYYMMDDTHHMMSS_frame
    

- 외부데이터 예시
    
    20210825_152815_맑음_오후_591_w0009.png
    
    O_SN_20210825T152815_w0009.png"""


#실내 데이터
from PIL import Image
from PIL.ExifTags import TAGS
import os
import json
import shutil
"""
PATH = "BlackIce/images"

file_list = os.listdir(PATH)
num = 1
for f in file_list:
    image = Image.open(PATH + "/" + f)
    info = image.getexif()
    taglabel = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value
    num += 1
    image.close()
    os.rename(PATH + "/" + f, PATH + "/" + "OD_CL_" + taglabel["DateTime"].replace(' ', 'T').replace(':', '') + "_" + "0" * (4 - len(str(num))) + str(num) + ".jpg")
"""
#실외 데이터
"""
PATH = "BlackIce/images"

file_list = os.listdir(PATH)
num = 1
for f in file_list:
    image = Image.open(PATH + "/" + f)
    info = image.getexif()
    taglabel = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value
    num += 1
    image.close()
    os.rename(PATH + "/" + f, PATH + "/" + "ID_SN_" + taglabel["DateTime"].replace(' ', 'T').replace(':', '') + "_" + "0" * (4 - len(str(num))) + str(num) + ".jpg")"""


"""외부데이터
    
    O_CL_YYYYMMDDTHHMMSS_frame
    
    O_SN_YYYYMMDDTHHMMSS_frame
    
    O_RN_YYYYMMDDTHHMMSS_frame
    

- 외부데이터 예시
    
    20210825_152815_맑음_오후_591_w0009.png
    
    O_SN_20210825T152815_w0009.png"""

#이륜차 데이터
PATH = "BlackIce/183.이륜자동차 안전 위험 시설물 데이터/01.데이터/2.Validation/원천데이터_230222_add/VS_Bounding Box_27.침수구간"
#이미지가 위치한 폴더 경로
JSON_PATH = "183.이륜자동차 안전 위험 시설물 데이터/01.데이터/1.Training/라벨링테이터_230222_add/TL_Bounding Box_27.침수구간"
#어노테이션이 위치한 폴더 경로

file_list = os.listdir(JSON_PATH)
dict = {}
for f in file_list:
    prefix = ""
    datetime = ""
    with open(JSON_PATH + "/" + f, 'r', encoding = "UTF8") as file:
        json_data = json.load(file)
        
        if json_data["images"]["collect_weather"] == "맑음":
            prefix = "SN"  
        elif json_data["images"]["collect_weather"] == "흐림":
            prefix = "CL"
        elif json_data["images"]["collect_weather"] == "우천":
            prefix = "RN"
        else:
            continue
        
        try:
            datetime = json_data["images"]["collect_date"].replace("-", "") + "T" + json_data["images"]["collect_time"].replace(":", "")
            if datetime in dict:
                dict[datetime] += 1
            else:
                dict[datetime] = 1
        except:
            continue    
        file.close()
        print("O_" + prefix + "_" + datetime + "_w" + "0" * (5 - len(str(dict[datetime]))) + str(dict[datetime]))
        #os.rename(PATH + "/" + f, PATH + "/" + "O_" + prefix + "_" + datetime + "_w" + "0" * (5 - len(str(dict[datetime]))) + str(dict[datetime]) + ".png")
        os.rename(JSON_PATH + "/" + f, "Named" + "/" + "O_" + prefix + "_" + datetime + "_w" + "0" * (5 - len(str(dict[datetime]))) + str(dict[datetime]) + ".json")
    

    

        