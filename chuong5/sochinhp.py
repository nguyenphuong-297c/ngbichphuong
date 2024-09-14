# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:57:20 2024

@author: Admin
"""
n = int(input())
check = False
for i in range(1, n + 1 ):
    if (i**2 == n):
        check = True
        break
if (check == True):
    print(n, " là số chính phương")
else:
    print(n, " không phải là số chính phương")
