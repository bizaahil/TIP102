def longest_streak(challenges, current_length=0, max_length=0):
    

    #if len is 0, then return 0
    if len(challenges) == 0:
        return max(current_length, max_length)

    # if s then update value by 1
    if challenges[0] == 'S':
        current_length+=1
        if current_length > max_length:
            max_length = current_length


    #if 0, then reset s to 0
    if challenges[0] == '0':
        if current_length > max_length:
            max_length = current_length
        current_length = 0

    


    return longest_streak(challenges[1:], current_length, max_length)


print(longest_streak("SSOSSS"))
print(longest_streak("SOSOSOSO"))