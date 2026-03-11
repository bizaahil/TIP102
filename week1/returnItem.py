def get_item(items, x):
    if 0 <= x < len(items):
        return items[x]
    else:
        return "None"
        

items = ["apple", "banana", "cherry", "date", "elderberry"]
x = 2
print(get_item(items, x))  # Output: "cherry"