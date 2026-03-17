def num_popular_pairs(popularity_scores):
    total_scores = 0
    scores = {}

    for score in popularity_scores:
        if score not in scores:
            scores[score] = 1
        else:
            scores[score] += 1

        
    for score in scores.values():
        total_scores += score*(score-1)//2

    return total_scores


popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 