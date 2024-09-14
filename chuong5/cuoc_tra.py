# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:02:36 2024

@author: Admin
"""
s = float(input("Nhập số km di chuyển: "))
tong_tien=0
if s<=1:
 print (" so tien phai tra la 15000")
elif 2<=s<=5:
 cuoc_dau1 = 15000 +(s -1)*13500
 print(" tiền trả:", cuoc_dau1)
else:
 cuoc_dau2 = 15000 + 4*13500 + (s-5)*11000
 print (" tiền trả:", cuoc_dau2)
if s>120:
    cuoc_dau3 = (15000+4*13500+(s-5)*11000)*0.9
    print(" tiền trả: ", cuoc_dau3)
 