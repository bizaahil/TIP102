def get_last(items):
    if(len(items) == 0):
        return None
    for i in range(len(items)):
        if i == len(items) - 1:
            return items[i]
        

print(get_last([1, 2, 3, 4, 5]))
print(get_last(["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]))
print(get_last(["a", "b", "c", "d"]))
print(get_last([]))