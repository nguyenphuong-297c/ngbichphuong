# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:57:26 2024

@author: Admin
"""
n = int(input('Nhập số n : '))
S = 0
for i in range(n + 1) :
 S += (2 * i + 1) / (2 * i + 2)
print('S = ', S)
