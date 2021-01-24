# -*- coding: utf-8 -*-
# 2. 특수문자 제거
test_text2 = '@@@@Hello~~ Every One!!!@@@@'
print("기본 텍스트: [" + test_text2 + "]")
print("----------------------------------")
print("양쪽 공백 제거: [" + test_text2.strip('@') + "]")
print("오른쪽 공백 제거: [" + test_text2.rstrip('@') + "]")
print("왼쪽 공백 제거: [" + test_text2.lstrip('@') + "]")
print("\n")
test_text3 = '@@ @@Hello~~ Every One!!!@@ @@'
print("기본 텍스트: [" + test_text3 + "]")
print("----------------------------------")
print("양쪽 공백 제거: [" + test_text3.strip('@') + "]")
print("오른쪽 공백 제거: [" + test_text3.rstrip('@') + "]")
print("왼쪽 공백 제거: [" + test_text3.lstrip('@') + "]")
