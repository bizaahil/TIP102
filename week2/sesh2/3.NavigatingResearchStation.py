def navigate_research_station(station_layout, observations):
    distance = 0
    current_distance = 0 #starting index


    for char in observations:

        next_position = station_layout.index(char)

        distance += abs(current_distance - next_position)

        current_distance = next_position


    return distance

  





station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
