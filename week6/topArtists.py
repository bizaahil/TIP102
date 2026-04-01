# Source: https://usaco.guide/general/i


#The assignment statement to the top_hits_2010s variable below creates the linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.
#UMPIRE
"""
#1) travserse the linked list
2) check if the nodes.artist is already in dict -> if not set it to 1, if it is +=1
3) while loop check if the next node is not null




"""


class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    
    my_dict = {}
    
    curr = playlist

    while(curr):

        if curr.artist in my_dict:
            my_dict[curr.artist] += 1
        else:
            my_dict[curr.artist] = 1

        curr = curr.next

    return my_dict

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))