# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:15:57 2024

@author: Admin
"""
n = int(input("Nhập số lần in 'Hello': "))
if n <= 0 or n > 1000:
    print("Số lần lặp không hợp lệ. Vui lòng nhập số nguyên dương nhỏ hơn 1000.")
else:
    for _ in range(n):
      print("Hello")

