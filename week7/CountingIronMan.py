def count_suits_iterative(suits):
    total = 0
    for x in suits:
        total += 1
    
    return total

def count_suits_recursive(suits):
    if suits == []:
        return 0
    return 1+ count_suits_iterative(suits[1:])


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))