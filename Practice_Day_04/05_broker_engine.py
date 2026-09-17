class StockHolding:
    def __init__(self, symbol:str, quantity:int, buy_price : float):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.buy_price = buy_price

    def get_invested_value(self):
        return self.quantity * self.buy_price

class BrokerAccount:
    def __init__(self, trader_name : str, initial_funds : float = 0.0):
        self.trader_name = trader_name
        if initial_funds > 0:
            self.funds = initial_funds
        else:
            self.funds = 0.0

        self.portfolio = {} 
        self.flat_brokerage = 20.0
    
    def deposit_funds(self, amount: float):
        if amount > 0:
            self.funds += amount

    def buy_stock(self, symbol: str, qty: int, market_price: float):
        symbol = symbol.upper()
        order_cost = (qty * market_price) + self.flat_brokerage
        
        if order_cost > self.funds:
            print(f"Insufficient funds! needed Rs. {order_cost}, Available Rs. {self.funds}")
            return False

        self.funds -= order_cost

        if symbol in self.portfolio:
            # Pehle se hai: Values update karo
            holding = self.portfolio[symbol]
            old_cost = holding.quantity * holding.buy_price
            new_cost = qty * market_price
            total_qty = holding.quantity + qty

            holding.buy_price = (old_cost + new_cost) / total_qty
            holding.quantity = total_qty
        else:
            # Naya hai: Naya object dictionary mein daalo
            self.portfolio[symbol] = StockHolding(symbol, qty, market_price)

        print(
            f"BOUGHT: {qty} shares of {symbol} @ Rs.{market_price:.1f} (Brokerage: Rs.20)"
        )
        return True
        
        
    def sell_stock(self, symbol:str, qty:int, market_price: float):
        symbol = symbol.upper()
        if symbol not in self.portfolio or self.portfolio[symbol].quantity < qty:
            current_holding = (self.portfolio[symbol].quantity if symbol in self.portfolio else 0)
            print(f"Short selling not allowed! Holding only {current_holding} shares of {symbol}")
            return False

        credit = (qty * market_price) - self.flat_brokerage
        self.funds += credit

        self.portfolio[symbol].quantity -= qty
        if self.portfolio[symbol].quantity == 0:
            del self.portfolio[symbol]
        print(f"SOLD: {qty} shares of {symbol} @ Rs. {market_price}(Net Credit : Rs.{credit})")
        return True

    def display_portfolio(self, current_market_prices:dict):
        total_portfolio_value = 0.0

        print("\n" + "=" * 50)
        print(f"TRADER: {self.trader_name} | CASH BALANCE: Rs.{self.funds:.1f}")
        print("=" * 50)
        print("HOLDINGS:")


        if len(self.portfolio) == 0:
            print("  (No actice holding)")
        for symbol, holding in self.portfolio.items():
            cmp = current_market_prices.get(symbol, holding.buy_price)
            current_value = holding.quantity * cmp
            invested_value = holding.get_invested_value()
            pnl = current_value - invested_value

            total_portfolio_value += current_value

            pnl_sign = "+" if pnl >= 0 else ""
            print(f"- {symbol}: {holding.quantity} Qty | Avg: Rs.{holding.buy_price:.1f} "
                f"| CMP: Rs.{cmp:.1f} | P&L: Rs.{pnl_sign}{pnl:.1f}")

        total_net_worth = total_portfolio_value + self.funds
        print("-" * 50)
        print(f"PORTFOLIO VALUE : Rs.{total_portfolio_value:.1f}")
        print(f"TOTAL NET WORTH : Rs.{total_net_worth:.1f}")
        print("=" * 50 + "\n")



if __name__ == "__main__":
    account = BrokerAccount(trader_name="Ansh Patel", initial_funds=10000.0)

    print("--- Test 1: Buying Stocks ---")
    account.buy_stock(symbol="TATAMOTORS", qty=10, market_price=600.0)
    account.buy_stock(symbol="INFY", qty=2, market_price=1500.0)

    print("\n--- Test 2: Insufficient Funds Rejection ---")
    account.buy_stock(symbol="RELIANCE", qty=1, market_price=2500.0)

    print("\n--- Test 3: Buying More of Same Stock (Averaging) ---")
    account.deposit_funds(20000.0)
    account.buy_stock(symbol="ADANIGREEN", qty=15, market_price=1200.0)

    print("\n--- Test 4: Selling Stock ---")
    account.sell_stock(symbol="INFY", qty=2, market_price=1700.0)
    account.sell_stock(symbol="ADANIGREEN", qty=15, market_price=1400.0)
    account.sell_stock(symbol="Relience", qty=10, market_price=100)

    print("\n--- Final Portfolio Statement ---")
    live_prices = {"TATAMOTORS": 680.0, "INFY": 1650.0}
    account.display_portfolio(live_prices)