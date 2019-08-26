planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
new_planets = ["Neptune", "Uranus"]
planet_list.extend(new_planets)
inner_planets = ["Earth", "Venus"]
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
rocky_planets = planet_list[1:4]
del planet_list[8]

print("rocky planets", rocky_planets)
print("all planets", planet_list)