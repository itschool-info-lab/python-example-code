# -*- coding: utf-8 -*-
cat = 'cat'
dog = 'dog'
cow = 'cow'
ret = None

# 3. if - elif - eles 문 #
animal = 'cow'
if animal is dog:
    ret = dog
elif animal is cat:
    ret = cat
else:
    ret = cow
print("Default: " + ret)

ret = dog if animal is dog else cat if animal is cat else cow
print("One-Line: " + ret)

# animal 변수값 변경 #
animal = 'cat'
if animal is dog:
    ret = dog
elif animal is cat:
    ret = cat
else:
    ret = cow
print("Default: " + ret)

ret = dog if animal is dog else cat if animal is cat else cow
print("One-Line: " + ret)

# animal 변수값 변경 #
animal = 'dog'
if animal is dog:
    ret = dog
elif animal is cat:
    ret = cat
else:
    ret = cow
print("Default: " + ret)

ret = dog if animal is dog else cat if animal is cat else cow
print("One-Line: " + ret)
