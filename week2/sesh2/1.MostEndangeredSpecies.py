def most_endangered(species_list):
    lowest = species_list[0]



    for species in species_list:
        if species["population"] < lowest["population"]:
            lowest = species
        
        
    return lowest["name"]



species_list = [
    {"name": "Amur Leopard", "population": 84},
    {"name": "Javan Rhino", "population": 72},
    {"name": "Vaquita", "population": 10}
]

print(most_endangered(species_list))
