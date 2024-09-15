# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:25:29 2024

@author: Admin
"""
def gcd(a, b):
  """Tính ước chung lớn nhất của hai số a và b bằng thuật toán Euclid.
  Args:
    a: Số nguyên thứ nhất.
    b: Số nguyên thứ hai.
  Returns:
    Ước chung lớn nhất của a và b.
  """
  while b != 0:
    a, b = b, a % b
  return a
if __name__ == "__main__":
  import sys
  if len(sys.argv) != 3:
    print("Vui lòng nhập đúng 2 số nguyên.")
    sys.exit(1)
  try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = gcd(x, y)
    print(f"Ước chung lớn nhất của {x} và {y} là: {result}")
  except ValueError:
    print("Vui lòng nhập các số nguyên.")
