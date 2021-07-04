# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFilter

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


# 3. 이미지 썸네일 만들기 #
try:
    im = Image.open("anchors.png")
    img_width, img_height = im.size
    print("이미지 사이즈:", im.size)
    print("이미지 가로:", img_width)
    print("이미지 세로:", img_height)
    print("이미지 모드:", im.mode)

    size = (100, 100)
    im.thumbnail(size)
    im.save("anchors_thumbnail.png")
    thum_im = Image.open("anchors_thumbnail.png")
    img_width, img_height = thum_im.size
    print("썸네일 이미지 사이즈:", thum_im.size)
    print("썸네일 이미지 가로:", img_width)
    print("썸네일 이미지 세로:", img_height)
    print("썸네일 이미지 모드:", thum_im.mode)
except OSError as e:
    print(e)


# 4. 이미지 크기 변경 #
try:
    im = Image.open("anchors.png")
    img_width, img_height = im.size
    print("이미지 사이즈:", im.size)
    print("이미지 가로:", img_width)
    print("이미지 세로:", img_height)
    print("이미지 모드:", im.mode)

    size = (1000, 1000)
    resize_img = im.resize(size)
    resize_img.save('anchors_resize.png')

    resize_im = Image.open("anchors_resize.png")
    img_width, img_height = resize_im.size
    print("크기변경 이미지 사이즈:", resize_im.size)
    print("크기변경 이미지 가로:", img_width)
    print("크기변경 이미지 세로:", img_height)
    print("크기변경 이미지 모드:", resize_im.mode)
except OSError as e:
    print(e)


# 5. 이미지 회전 각도 변경 #
try:
    im = Image.open("anchors.png")
    img_width, img_height = im.size
    print("이미지 사이즈:", im.size)
    print("이미지 가로:", img_width)
    print("이미지 세로:", img_height)
    print("이미지 모드:", im.mode)

    rotate = 90
    rotate_img = im.rotate(rotate)
    rotate_img.save('anchors_rotate.png')

    rotate_im = Image.open("anchors_rotate.png")
    img_width, img_height = rotate_im.size
    print("회전 각도 이미지 사이즈:", rotate_im.size)
    print("회전 각도  이미지 가로:", img_width)
    print("회전 각도  이미지 세로:", img_height)
    print("회전 각도  이미지 모드:", rotate_im.mode)
except OSError as e:
    print(e)


# 6. 이미지 필터 적용 #
try:
    im = Image.open("anchors.png")
    img_width, img_height = im.size
    print("이미지 사이즈:", im.size)
    print("이미지 가로:", img_width)
    print("이미지 세로:", img_height)
    print("이미지 모드:", im.mode)

    filter_img = im.filter(ImageFilter.BLUR)
    filter_img.save("anchors_filter.png")

    filter_im = Image.open("anchors_filter.png")
    img_width, img_height = filter_im.size
    print("필터 이미지 사이즈:", filter_im.size)
    print("핕터 이미지 가로:", img_width)
    print("핕터 이미지 세로:", img_height)
    print("핕터 이미지 모드:", filter_im.mode)
except OSError as e:
    print(e)

