def max_profit(stock_prices):
    """
    what is the max profit possible between two prices
    of stock assuming you must buy before you can sell
    in O(n)^2 time
    """
    max_profit = 0

    for index, current_price in enumerate(stock_prices):
        current_index = index
        max_index = len(stock_prices)

        for i in range(current_index+1, max_index):
            selling_profit = stock_prices[i] - current_price

            if selling_profit > max_profit:
                max_profit = selling_profit

    return max_profit

def max_profit_faster(stock_prices):
    """
    make money faster in O(n) time
    buy low then sell high later for max profits
    """
    if len(stock_prices) is 0:
        return 0

    open_price = stock_prices[0]
    low_price = open_price
    max_profit = 0

    for price in stock_prices:
        current_price_profit = price - low_price
        sell_higher = current_price_profit > max_profit
        buy_lower = price < low_price

        if sell_higher:
            max_profit = current_price_profit
        if buy_lower:
            low_price = price

    return max_profit
