# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:41:03 2024

@author: Student
"""
N = input("Nhập một số nguyên dương: ")
if N.isdigit():
    tổng_chữ_số = sum(int(chữ_số) for chữ_số in N)
    print(f"Tổng các chữ số của {N} là: {tổng_chữ_số}")
else:
    print("Số nhập vào không hợp lệ. Vui lòng nhập một số nguyên dương.")

