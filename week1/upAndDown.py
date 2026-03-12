def up_and_down(lst):
    oddNums = 0
    evenNums = 0

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            evenNums += 1
        else:
            oddNums += 1

    return oddNums - evenNums

lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))