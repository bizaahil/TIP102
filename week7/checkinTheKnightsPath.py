def is_increasing_path(path):
    


    #if path is len 1 -> return true
    if len(path) == 1:
        return True
    
    #if path at 0 is more than 1 - > return false
    if path[0] >= path[1]:
        return False
    
    return is_increasing_path(path[1:])




print(is_increasing_path([1, 2, 3, 4, 5]))
print(is_increasing_path([3, 5, 2, 8]))