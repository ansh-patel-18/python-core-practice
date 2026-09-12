class StockHolding:
    def __init__(self,symbol:str, quantity : int, buy_price : float):
        self.symbol = symbol
        if quantity<0:
            self.quantity=0.0    
        else:
            self.quantity = quantity

        self.buy_price = buy_price

    def get_invested_value(self):
        print(f"Total Wealth : {self.quantity * self.buy_price}")

class BrokerAccount:
    def __init__(self, trader_name:str, initial_fund : float = 0.0):
        self.trader_name = trader_name
        
        
       
        if initial_fund >= 0:
            self.fund = initial_fund
        else:
            self.fund

        self.portfolio = {}
        self.flat_brockage = 20.0 

    def deposit_fund(self, amount):
        if amount >= 0:
            self.fund += amount

    def buy_stock(self, symbol:str, qty:int, market_price:float):
        symbol = symbol.upper()
        order_cost = (qty * market_price) + self.flat_brockage
        
        if order_cost>self.fund:
            print(f"Insufficient funds! Needed Rs.{order_cost}. Available balance : {self.fund}")
            return False
            
if __name__ == "__main__":
    # u1 = StockHolding(symbol="TATAMOTORS", quantity=2, buy_price=1550)
    # u1.get_invested_value()
    u1 = BrokerAccount(trader_name="Ansh Patel", initial_fund=0)
    u1.deposit_fund(15000)
    u1.buy_stock(symbol="relience", qty=8, market_price=1390.05)