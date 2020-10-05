"""CSC 161 Project Extra Credit

Blessing Babajide
Lab Section TR 12:30 - 1:45pm
Fall 2019
"""

class Stock:

    def __init__(self, stocks, funds, price, qty):
        self.stocks = stocks
        self.funds = funds
        self.price = price
        self.qty = qty

    def buy_stock(self):
        if self.funds < (self.qty * self.price):
            return self.funds, self.stocks

        else:
            self.new_funds = self.funds - (self.price * self.qty)
            self.new_stocks = self.stocks + self.qty
            return self.new_funds, self.new_stocks

    def sell_stock(self):
        if self.stocks < self.qty:
            return self.funds, self.stocks
        else:
            self.new_funds = self.funds + (self.price * self.qty)
            self.new_stocks = self.stocks - self.qty
            return self.new_funds, self.new_stocks
