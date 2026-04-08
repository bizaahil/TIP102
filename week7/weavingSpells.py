class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def weave_spells(spell_a, spell_b):


    
    #if spell_a is empty, attach rest of b
    if spell_a is None:
        return spell_b

    #if spell_b is empty, attach rest of a
    if spell_b is None:
        return spell_a

    next_a = spell_a.next
    next_b = spell_b.next

    spell_a.next = spell_b
    spell_b.next = weave_spells(next_a, next_b)

    return spell_a


spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))

print_linked_list(weave_spells(spell_a, spell_b))