# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:29:32 2024

@author: Admin
"""
import sys
def decimal_to_base(i, k):
  """Chuyển đổi số nguyên i sang cơ số k.
  Args:
    i: Số nguyên cần chuyển đổi.
    k: Cơ số đích (2-16).
  Returns:
    Chuỗi biểu diễn số i ở cơ số k.
  """
  if not 2 <= k <= 16:
    raise ValueError("Cơ số phải nằm trong khoảng từ 2 đến 16.")
  digits = "0123456789ABCDEF"
  result = ""
  while i > 0:
    remainder = i % k
    result = digits[remainder] + result
    i //= k
  return result
if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Vui lòng nhập hai số nguyên: số cần chuyển đổi và cơ số đích.")
    sys.exit(1)
  try:
    i = int(sys.argv[1])
    k = int(sys.argv[2])
    if k < 2 or k > 16:
      print("Cơ số phải nằm trong khoảng từ 2 đến 16.")
    else:
      result = decimal_to_base(i, k)
      print(f"{i} ở cơ số {k} là: {result}")
  except ValueError:
    print("Vui lòng nhập các số nguyên.")
