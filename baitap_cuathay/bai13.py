# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:38:35 2024

@author: Admin
"""
import sys
def print_powers_of_two(n):
  """In ra tất cả các lũy thừa của 2 nhỏ hơn hoặc bằng n.
  Args:
    n: Số nguyên dương.
  """
  if n <= 0:
    return
  power = 0
  value = 2**power
  while value <= n:
    print(value)
    power += 1
    value = 2**power
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Vui lòng nhập một số nguyên dương.")
    sys.exit(1)
  try:
    n = int(sys.argv[1])
    if n <= 0:
      print("Số nhập vào phải là số nguyên dương.")
    else:
      print_powers_of_two(n)
  except ValueError:
    print("Vui lòng nhập một số nguyên.")
