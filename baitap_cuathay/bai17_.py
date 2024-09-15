# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:26:28 2024

@author: Admin
"""
import sys
def draw_chessboard(n):
  """Vẽ bàn cờ kích thước n x n.
  Args:
    n: Kích thước của bàn cờ.
  """
  for i in range(n):
    for j in range(n):
      # Sử dụng phép XOR để xen kẽ dấu sao và dấu cách
      char = '*' if (i + j) % 2 == 0 else ' '
      print(char, end='')
    print()
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Vui lòng nhập kích thước bàn cờ.")
    sys.exit(1)
  try:
    n = int(sys.argv[1])
    if n <= 0:
      print("Kích thước bàn cờ phải là số nguyên dương.")
    else:
      draw_chessboard(n)
  except ValueError:
    print("Vui lòng nhập một số nguyên.")
