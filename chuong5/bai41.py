# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:08:53 2024

@author: Admin
"""
tong = 0
n = 0
print("Hãy nhập vào số n: ")
n = int(input())
for i in range(1, n + 1):
    tong += 1 / (2 * i + 1)
print("Tổng số là: ", tong)
