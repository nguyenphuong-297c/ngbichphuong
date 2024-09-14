# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 07:46:05 2024

@author: Admin
"""
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if a <= 0 or b <= 0 or c <= 0:
    print ("Không phải là tam giác")
if a + b <= c or b + c <= a or c + a <= b:
    print ("Không phải là tam giác")
if a == b == c:
    print ("Tam giác đều")
elif a == b or b == c or c == a:
    print ("Tam giác cân")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print ("Tam giác vuông")
else:
    print( "Tam giác thường")
