"""
목표
이미지, 라벨링 파일 원하는 개수 가져온 후 학습 하기 전 폴더에 만들어 놓기

외부데이터
O_SN_20210825T152815_w0009.png
외부_날씨_날짜T시간_
"""

# 날씨에 따라 랜덤으로 maximum N장 가져오기
# 시간대에 따라 랜덤으로 maximum N장 가져오기

import os
import sys
import shutil
from random import random

"""
쿼리 날리는 방법 설명
"""
how_to_work = """
<쿼리문 컨벤션>
{조건 선택}_{조건 범위}_{장수}

<조건 선택>
날씨 조건 : 0
시간 조건 : 1
-----
<조건 범위>
배열을 문자열로 변경한 상태로 넘겨줘야 함.
CL, SN 날씨를 고르고 싶은 경우 CL SN.
19~21시 선택하고 싶은 경우 19 20 21.
----
<장수>
정수 N.

<예시 쿼리문>
19, 20, 21시의 데이터 300장 랜덤으로 추출
1_19 20 21_300

CL 날씨의 데이터 300장 랜덤으로 추출
0_CL_300
"""    
WEATHERLIST = ['CL','SN','RN']
"""
초기화함수 - img, label 개수 맞는지 체크 후 source dir 경로와 파일 list 리턴.
"""
def initialize(img_s="원천데이터_230222_add/TS_Bounding Box_27.침수구간", lable_s="라벨링테이터_230222_add/TL_Bounding Box_27.침수구간"):
    # 현재 경로 prefix
    PREFIX = os.getcwd()
    
    img_source_dir = os.path.join(PREFIX, img_s)
    label_source_dir = os.path.join(PREFIX, lable_s)

    img_list = os.listdir(img_source_dir)
    label_list = os.listdir(label_source_dir)

    print(f"img 파일 개수 : {len(os.listdir(img_source_dir))}")
    print(f"label 파일 개수 : {len(os.listdir(label_source_dir))}")

    assert len(img_list) == len(label_list), f"img : {len(img_list)}, label : {len(label_list)} 로 서로 쌍이 맞지 않습니다."

    return img_source_dir, img_list, label_source_dir, label_list

def check_query(query_condition):
    assert len(query_condition.split('_')) == 3, "쿼리문이 잘못되었습니다."

    condition_type, condition_list, condition_N = query_condition.split('_')

    # type 체크
    assert int(condition_type) == 0 or int(condition_type) == 1, "쿼리문의 condition_type이 잘못되었습니다."

    # 조건 체크
    condition_list = condition_list.split(' ')
    if condition_type==0:
        for c in condition_list:
            assert c in WEATHERLIST, "날씨 조건이 잘못되었습니다."

    # 장수 체크
    condition_N = int(condition_N)

    if int(condition_type) == 0:
        print(f"날씨, 조건 : {condition_list}, 장수 : {condition_N}장")
    elif int(condition_type) == 1:
        print(f"시간, 조건 : {condition_list}, 장수 : {condition_N}장")

    if input("올바르지 않을 경우, n 혹은 N 누르면 종료입니다.").upper()== "N":
        sys.exit()
    
    return int(condition_type), condition_list, int(condition_N)


def query_weather(condition_list,condition_N):
    print("weather query 시작")
    
def query_time(condition_list,condition_N):
    print("time query 시작")
    

# 각 조건에 따른 파일 결과를 미리 보여줌
def set_query_condition():
    print(how_to_work)
    query_condition = input()
    condition_type, condition_list, condition_N =check_query(query_condition)

    # 날씨 조건 먼저 테스트
    if condition_type == 0:
        query_weather(condition_list,condition_N)
    else:
        query_time(condition_list,condition_N)


if __name__ == "__main__":
    WEATHERLIST = ['CL','SN','RN']
    TARGET_WEATHER = ''
    N = 300

    # 경로 설정
    img_source_dir, img_list, label_source_dir, label_list = initialize()

    # 쿼리할 파일 설정
    set_query_condition()

    # 쿼리할 파일 결과가 마음에 드는 경우에 파일 이동 등 로직 실행
    if input().upper() == "Y":
        # 파일 이동
        print("do it")
        # 결과 파일 로깅 후 종료    
    else:
        print("exit")
        sys.exit()