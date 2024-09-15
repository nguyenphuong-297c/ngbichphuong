# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:18:14 2024

@author: Admin
"""
for i in range(1000, 2000):
    print(i, end=" ")
    if (i+1) % 5 == 0:
        print()  # Xuống dòng khi số lượng số trên dòng đạt 5
