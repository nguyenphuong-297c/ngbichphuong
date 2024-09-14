# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:38:50 2024

@author: Admin
"""
n = int(input("Nhập giá trị nguyên n: "))
result_dict = {i: i ** i for i in range(1, n + 1)}
print(result_dict)

