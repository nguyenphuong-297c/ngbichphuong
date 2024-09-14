# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:04:19 2024

@author: Admin
"""
n = int(input())
print("Danh sách các ước số của ", n, " là")
for i in range(1, n+1):
    if (n % i == 0):
        print(i, end=",")
