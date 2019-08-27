# Original
planet_list = ["Mercury", "Mars"]
# Add two planets using .append
planet_list.append("Jupiter")
planet_list.append("Saturn")
# Add a list of planets using .extend
new_planets = ["Neptune", "Uranus"]
planet_list.extend(new_planets)
# Use .insert for two planets
inner_planets = ["Earth", "Venus"]
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
# . append pluto
planet_list.append("Pluto")
# make a new list
rocky_planets = planet_list[1:4]
del planet_list[8]

# create a space craft
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Ringo", "Earth"),
   ("MeMaw", "Venus")
]

for planet in planet_list:
    print(planet)
    for visited in spacecraft:
        if visited[1] == planet:
            print(f"{planet} has been visted by {visited[0]}")
        # else:
            # print(planet)
