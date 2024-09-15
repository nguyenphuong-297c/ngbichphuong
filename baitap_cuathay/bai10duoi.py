# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:43:18 2024

@author: Admin
"""
import math
def probability_no_one_in_n_throws(n):
  """Tính xác suất không nhận được mặt 1 nào trong n lần gieo.
  Args:
    n: Số lần gieo.
  Returns:
    Xác suất.
  """
  return (5/6) ** n
def main():
  # Xác suất không nhận được mặt 1 nào trong 6 lần gieo
  prob1 = probability_no_one_in_n_throws(6)
  # Xác suất không nhận được mặt 1 nào trong 12 lần gieo
  prob2 = probability_no_one_in_n_throws(12)
  # Xác suất nhận được ít nhất 1 lần mặt 1 trong 6 lần gieo
  prob_at_least_one_in_6 = 1 - prob1
  # Xác suất nhận được ít nhất 2 lần mặt 1 trong 12 lần gieo
  prob_at_least_two_in_12 = 1 - prob2
  print(f"Xác suất nhận được ít nhất 1 lần mặt 1 trong 6 lần gieo: {prob_at_least_one_in_6:.4f}")
  print(f"Xác suất nhận được ít nhất 2 lần mặt 1 trong 12 lần gieo: {prob_at_least_two_in_12:.4f}")
  if prob_at_least_one_in_6 > prob_at_least_two_in_12:
    print("Có khả năng hơn khi nhận được ít nhất một lần số 1 khi gieo một con xúc xắc sáu mặt sáu lần.")
  else:
    print("Có khả năng hơn khi nhận được ít nhất hai lần số 1 khi gieo nó 12 lần.")
if __name__ == "__main__":
  main()
