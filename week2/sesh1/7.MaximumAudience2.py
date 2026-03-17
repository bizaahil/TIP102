def max_audience_performances(audiences):
    
    counts = {}

    #store all values in max
    for value in audiences:
        if value not in counts:
            counts[value] = 1
        else:
            counts[value] += 1
    

    #find biggest value in max
    largest = max(counts)

    return largest * counts[largest]
    

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
    