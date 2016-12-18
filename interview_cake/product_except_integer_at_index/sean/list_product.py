def find_product_list(integers):
    left_products = []
    right_products = []
    result = []
    total = 1
    for number in integers:
        left_products.append(total)
        total *= number
    total = 1
    for number in reversed(integers):
        right_products.append(total)
        total *= number
    right_products = reversed(right_products)
    for left_num, right_num in zip(left_products, right_products):
        result.append(left_num * right_num)
    return result
