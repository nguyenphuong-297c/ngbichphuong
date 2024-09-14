# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:38:42 2024

@author: Admin
"""
n = int(input("Nhập n: "))
S = 0 ;
for i in range(1,n+1):
    if i % 2 == 0: S += i ;
print("Tổng là: ",S)
