prices = {"AAPL": 180, "TSLA": 250}
total=0
stock = input("Stock name AAPL/TSLA: ").upper()
qty = int(input("Quantity: "))
total = prices[stock]*qty
print(f"Total = ${total}")