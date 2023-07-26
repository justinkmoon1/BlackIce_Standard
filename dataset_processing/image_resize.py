from PIL import Image

# 원본 이미지 열기
image = Image.open("assets/blackice_backgrounddiff.jpg")

# 새로운 크기로 이미지 조정
new_size = (640, 640)  # 새로운 크기 (가로, 세로)
resized_image = image.resize(new_size)

# 조정된 이미지 저장
resized_image.save("assets/blackice_backgrounddiff.jpg") 