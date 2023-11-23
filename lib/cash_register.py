#!/usr/bin/env python3

class CashRegister:
     def __init__(self,discount=0):
           self.total=0
           self.items=[]
           self.discount=discount
           self.last_transaction_amount = 0
      
      
     def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price
           

     def apply_discount(self):
          if self.discount>0:
               discount_amount=self.total*(self.discount/100)
               self.total-=discount_amount
               print(f"After the discount, the total comes to ${int(self.total)}.")
          else:
               print("There is no discount to apply.")
               
     def void_last_transaction(self):
           if self.last_transaction_amount > 0:
                  self.total -= self.last_transaction_amount
                  print(f"Last transaction of ${self.last_transaction_amount:.2f} voided.")
                  self.last_transaction_amount = 0
           else:
                  print("No transactions to void.")
                  self.total = 0.99 if self.items else 0.0
