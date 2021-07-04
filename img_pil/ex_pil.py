# -*- coding: utf-8 -*-
from PIL import Image

# 1. 이미지 파일 기본 정보 읽기 #
try:
    im = Image.open("anchors.png")
    img_width, img_height = im.size
    print("이미지 확장자:", im.format)
    print("이미지 사이즈:", im.size)
    print("이미지 가로:", img_width)
    print("이미지 세로:", img_height)
    print("이미지 모드:", im.mode)
except OSError as e:
    print(e)


# 2. 이미지 파일 변환 #
try:
    im = Image.open("anchors.png").convert('RGB')
    im.save("anchors.webp", 'webp')
    change_im = Image.open("anchors.webp")
    img_width, img_height = change_im.size
    print("이미지 확장자:", change_im.format)
    print("이미지 사이즈:", change_im.size)
    print("이미지 가로:", img_width)
    print("이미지 세로:", img_height)
    print("이미지 모드:", change_im.mode)
except OSError as e:
    print(e)

