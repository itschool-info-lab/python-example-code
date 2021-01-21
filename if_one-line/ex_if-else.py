# -*- coding: utf-8 -*-
cat = 'cat'
dog = 'dog'
ret = None

# 2. if - eles 문 #
animal = 'cat'
if animal is dog:
    ret = dog
else:
    ret = cat
print("Default: " + ret)

ret = dog if animal is dog else cat
print("One-Line: " + ret)

# animal 변수값 변경 #
animal = 'dog'
if animal is dog:
    ret = dog
else:
    ret = cat
print("Default: " + ret)

ret = dog if animal is dog else cat
print("One-Line: " + ret)
