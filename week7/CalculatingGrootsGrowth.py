def fibonacci_growth(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)


print(fibonacci_growth(5)) #5
print(fibonacci_growth(8)) #21