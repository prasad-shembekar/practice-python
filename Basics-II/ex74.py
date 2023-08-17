
def buy(stock_price):
    max_profit,current_max = 0,0

    for price in reversed(stock_price):
        current_max = max(current_max,price)
        potential_profit =current_max - price
        max_profit = max(potential_profit,max_profit)
    return max_profit

print(buy([8, 10, 7, 5, 7, 15]))


