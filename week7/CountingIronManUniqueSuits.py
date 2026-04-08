def count_suits_iterative(suits):
    seen = set()

    for suit in suits:
        seen.add(suit)
    
    return len(seen)

    

def count_suits_recursive(suits):
    suits = list(set(suits))

    if len(suits) == 0:
        return 0
    else:
        return 1 + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
