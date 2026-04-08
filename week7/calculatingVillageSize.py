def get_village_class_iterative(population):
    digits = 0

    while population > 0:
        population = population // 10
        digits += 1


    return digits

def get_village_class_recursive(population):
    
    if population < 10:
        return 1
    return 1 + get_village_class_recursive(population//10)



print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))