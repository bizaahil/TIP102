def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    
    max = strongest_avenger(strengths[1:])

    if strengths[0] > max:
        return strengths[0]
    return max





print(strongest_avenger([88, 92, 95, 99, 97, 100, 94])) #100
print(strongest_avenger([50, 75, 85, 60, 90])) #90