# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:42:03 2024

@author: Admin
"""
import math
def count_primes(n):
  """Đếm số lượng số nguyên tố nhỏ hơn n bằng sàng Eratosthenes.
  Args:
    n: Số nguyên dương.
  Returns:
    Số lượng số nguyên tố nhỏ hơn n.
  """
  if n <= 2:
    return 0
  # Tạo danh sách các số nguyên từ 2 đến n, giả định tất cả là số nguyên tố
  primes = [True] * (n + 1)
  primes[0] = primes[1] = False
  # Sàng Eratosthenes
  for p in range(2, int(math.sqrt(n)) + 1):
    if primes[p]:
      for i in range(p * p, n + 1, p):
        primes[i] = False
  # Đếm số lượng số nguyên tố
  return sum(primes)
if __name__ == "__main__":
  import sys
  if len(sys.argv) != 2:
    print("Vui lòng nhập một số nguyên dương.")
    sys.exit(1)
  try:
    n = int(sys.argv[1])
    if n <= 0:
      print("Số nhập vào phải là số nguyên dương.")
    else:
      count = count_primes(n)
      print(f"Số lượng số nguyên tố nhỏ hơn {n} là: {count}")
  except ValueError:
    print("Vui lòng nhập một số nguyên.")
