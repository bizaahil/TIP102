def count_walls(walls):
    if not walls:
        return 1
    if isinstance(walls[0], list):
        return count_walls(walls[0]) + count_walls(walls[1:])
    return count_walls(walls[1:])




walls = ["outer", ["inner", ["keep", []]]]

print(count_walls(walls))
print(count_walls([]))