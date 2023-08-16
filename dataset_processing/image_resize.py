from PIL import Image

# 원본 이미지 열기
image = Image.open("datasets/COCO/train2017/IMG_0990_JPG.rf.61cba2f4f2ad1faee43de902dca15aed.jpg")

# 새로운 크기로 이미지 조정
new_size = (416, 416)  # 새로운 크기 (가로, 세로)
resized_image = image.resize(new_size)

# 조정된 이미지 저장
resized_image.save("datasets/COCO/train2017/IMG_0990_JPG.rf.61cba2f4f2ad1faee43de902dca15aed.jpg") 