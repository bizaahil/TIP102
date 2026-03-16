def best_set(votes):
    results = {}

    for value in votes.values():
        if value not in results:
            results[value] = 1
        else:
            results[value] += 1

    #return biggest value in results
    return max(results, key=results.get)


#make a new dictionary
#traverse thru votes
#add every arist if not in 
#if alr there, increment the value for that arist
#return the artist with the most votes in the new dictionary


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1236: "Ethel Cain",
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))