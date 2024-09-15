# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:35:11 2024

@author: Admin
"""
import math
def print_table(values):
  """In bảng giá trị theo định dạng.
  Args:
    values: Danh sách các giá trị cần in.
  """
  for row in values:
    print("\t".join(map(str, row)))
if __name__ == "__main__":
  # Các giá trị của n
  n_values = [2, 4, 8, 16, 32, 64, 128]
  # Tính toán các giá trị tương ứng
  table_data = []
  for n in n_values:
    log_n = math.log2(n)
    n_log_n = n * log_n
    n_squared = n**2
    n_cubed = n**3
    table_data.append([log_n, n, n_log_n, n_squared, n_cubed])
  # In tiêu đề bảng
  print("log(n)\tn\tn*log(n)\tn^2\tn^3")
  # In dữ liệu
  print_table(table_data)
