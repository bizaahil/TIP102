def double_power(initial_power, n):
    if n == 0:
        return initial_power
    
    return double_power(initial_power*2, n-1)


print(double_power(5, 3))
print(double_power(7, 2))