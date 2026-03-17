def max_audience_performances(audiences):
    max_val = max(audiences) #220

    total = 0

    for i in range(len(audiences)):
        if audiences[i] == max_val:
            total += audiences[i]
    
    return total



audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))