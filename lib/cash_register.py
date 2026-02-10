#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []
    self.previous_transactions = []

  # verify that discount is a number and in between 0 and 100
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if type(value) is int and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity

    for _ in range(quantity):
      self.items.append(item)

    new_transaction = {
      "item": item,
      "price": price,
      "quantity": quantity
    }
    self.previous_transactions.append(new_transaction)

  def apply_discount(self):
    if self.discount > 0:
      self.total -= int((self.discount / 100) * self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      return
    
    last = self.previous_transactions.pop()
    item = last["item"]
    price = last["price"]
    quantity = last["quantity"]

    self.total -= price * quantity

    for _ in range(quantity):
      self.items.remove(item)

trans1 = CashRegister(10, 0)
print(trans1)
trans1.add_item("Bread", 5, 10)
trans1.apply_discount()
print(trans1.previous_transactions)
print(trans1.total)