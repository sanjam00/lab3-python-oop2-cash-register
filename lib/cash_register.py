#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if type(value) is int and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")