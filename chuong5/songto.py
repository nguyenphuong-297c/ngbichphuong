# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:00:18 2024

@author: Admin
"""

n = int(input())
flag = True
if (n < 2):
    flag = False
elif (n == 2):
    flag = True
elif (n % 2 == 0):
    flag = False
else:
    for i in range(3, n, 2):
        if (n % i == 0):
            flag = False
if flag == True:
    print(n, " là số nguyên tố")
else:
    print(n, " không phải là số nguyên tố")