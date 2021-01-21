# -*- coding: utf-8 -*-
animal = 'dog'
cat = 'cat'
dog = 'dog'
ret = None

# 1. if 문 #
if animal is dog:
    ret = dog
print("Default: " + ret)

if animal is dog: ret = dog
print("One-Line: " + ret)
