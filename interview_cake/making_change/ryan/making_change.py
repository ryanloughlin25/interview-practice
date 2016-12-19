from itertools import islice

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
