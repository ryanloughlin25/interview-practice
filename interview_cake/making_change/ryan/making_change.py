from itertools import islice


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
