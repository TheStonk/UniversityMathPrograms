def sum_rule(sets:list[set]):
    print(sets[0].union(sets[1:]))
    return len(sets[0].union(sets[1:]))


def product_rule():
    pass

def subtraction_rule():
    pass

def division_rule():
    pass

print(sum_rule([{1},{2},{3}]))