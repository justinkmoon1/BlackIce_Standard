#program for loading pre-annotated data to label studio (modifying JSON file)
#Black Ice Project

import os
#PATH = "C:\Users\Justin Moon\BlackIce\Users\Justin Moon\BlackIce"
#FOLDER = "\Annot\TL01_지자체도로정비AI데이터_CASE1(도로)\지자체도로정비AI데이터_CASE1(도로)_WET_RAIN_01"

print(os.listdir("Annot\TL01_지자체도로정비AI데이터_CASE1(도로)\지자체도로정비AI데이터_CASE1(도로)_WET_RAIN_01"))
dict = {"data": {
    "image": "",
    }
        "predictions": "",
    }

#   with open("")