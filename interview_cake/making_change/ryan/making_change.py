from itertools import islice
from collections import defaultdict

"""
bother, I've implemented a function to return the set of
combinations that sum to the amount.  It should have just
been a function to return the number of combinations.
"""
def making_change(amount, denominations):
    result = []
    for index, denomination in enumerate(denominations):
        if amount == denomination:
            result.append([denomination])
        elif denomination < amount:
            subproblems = making_change(
                amount - denomination,
                denominations[index:],
                # islice(denominations, index, None),
            )
            for subproblem in subproblems:
                result.append([denomination] + subproblem)
    return result


def making_change_subproblem(amount, denomination, subresults):
    result = []
    for subresult in subresults:
        result.append(subresult + [denomination])
    if amount == denomination:
        result.append([denomination])
    return result


def making_change(amount, denominations):
    results = defaultdict(list)

    for denomination in denominations:
        for sub_amount in range(denomination, amount + 1):
            subresults = making_change_subproblem(
                sub_amount,
                denomination,
                results[sub_amount - denomination],
            )
            for subresult in subresults:
                results[sub_amount].append(subresult)

    return results[amount]
