def count_deposits(resources):
    
    if len(resources) == 0:
        return 0
    
    if resources[0] == 'V':
        return 1 + count_deposits(resources[1:])
    else:
        return count_deposits(resources[1:])

#convert string to list
#base case, if len of list is 0 return 0
#we check the first index and if its a 'V' then we add to the sum


print(count_deposits("VVVVV")) #5
print(count_deposits("VXVYGA")) #2