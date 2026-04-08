def reverse_scroll(scroll):
    if len(scroll) == 0:
        return ""
    return scroll[-1] + reverse_scroll(scroll[:len(scroll)-1])

print(reverse_scroll("cigam"))
print(reverse_scroll("lleps"))