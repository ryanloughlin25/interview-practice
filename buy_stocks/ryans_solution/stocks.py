import sys


def buy_stock(prices):
    buy_price = sys.maxsize
    max_profit = 0

    for price in prices:
        current_profit = price - buy_price
        if current_profit > max_profit:
            max_profit = current_profit
        if price < buy_price:
            buy_price = price

    return max_profit
