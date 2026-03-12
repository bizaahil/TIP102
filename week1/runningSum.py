def running_sum(superhero_stats):
    sum = superhero_stats[0]

    for i in range(len(superhero_stats)):
        superhero_stats[i] = sum
        if(i != len(superhero_stats)-1):
            sum += superhero_stats[i+1]

    return superhero_stats


superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))