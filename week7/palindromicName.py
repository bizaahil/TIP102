def is_palindrome(name):

    #if name is 1 letter or less
    if len(name) <= 1:
        return True
    
    #if first and last dont match -> not palindrome
    if name[0] != name[-1]:
        return False
    
    return is_palindrome(name[1:-1])
    
    



print(is_palindrome("eve"))
print(is_palindrome("ling"))
print(is_palindrome(""))