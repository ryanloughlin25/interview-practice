import sys


def buy_stock(prices):
    buy_price = sys.maxsize
    max_profit = 0

    for price in prices:
        current_profit = price - buy_price
        max_profit = max(current_profit, max_profit)
        buy_price = min(price, buy_price)

    return max_profit
