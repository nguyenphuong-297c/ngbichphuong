# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:46:48 2024

@author: Admin
"""
tong = 0
n = 0
print("Hãy nhập vào số n: ")
n = int(input())
 
for i in range(1, n + 1) :
    tong += i ** 2
print("Tổng số là: ", tong)
