# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:28:03 2024

@author: Admin
"""
import sys
def decimal_to_binary(n):
  """Chuyển đổi số nguyên dương n thành biểu diễn nhị phân dưới dạng chuỗi.
  Args:
    n: Số nguyên dương cần chuyển đổi.
  Returns:
    Chuỗi biểu diễn nhị phân của n.
  """
  binary_string = ""
  while n > 0:
    remainder = n % 2
    binary_string = str(remainder) + binary_string
    n //= 2
  return binary_string
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Vui lòng nhập một số nguyên dương.")
    sys.exit(1)
  try:
    n = int(sys.argv[1])
    if n <= 0:
      print("Vui lòng nhập số nguyên dương.")
    else:
      binary_result = decimal_to_binary(n)
      print(binary_result)
  except ValueError:
    print("Vui lòng nhập một số nguyên.")
