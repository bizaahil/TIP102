def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    dict_s = {}
    dict_t = {}
    total = 0

    for i in range(len(s)):
        dict_s[s[i]] = i

    for j in range(len(t)):
        dict_t[t[j]] = j

    #find total number of differences
    for value in dict_s.keys():
        total += abs(dict_s[value] - dict_t[value])

    return total


s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))