def identify_conflicts(venue1_schedule, venue2_schedule):
    same_schedule = {}


# traverse thru venue1
# check if it exists in venue2
# if it does check if values (times) are same
# if they are add into dictionary

    for artist in venue1_schedule:
        if artist in venue2_schedule:
            if venue1_schedule[artist] == venue2_schedule[artist]:
                same_schedule[artist] = venue1_schedule[artist]


    return same_schedule


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))