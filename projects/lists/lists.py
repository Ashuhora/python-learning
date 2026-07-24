# Declare a new List

colors = ["red", "green", "blue", "yellow"]
print(colors)

# Access elements by index

colors = ["red", "green", "blue", "yellow"]
print(colors[2])

# Replace list elements

colors = ["red", "green", "blue", "yellow"]

colors[2] = "purple"
colors[1] = colors[2]

print(colors)
print(colors[0].title())

# f-string example

brands = ["microsoft", "google", "apple"]
print(f"The first brand is {brands[0].title()}.")

# insert()

planets = ["mercury", "mars", "saturn"]

# Insert Venus
planets.insert(1, "venus")
print(planets)

# Insert Earth
planets.insert(2, "earth")
print(planets)

# Insert Jupiter
planets.insert(4, "jupiter")
print(planets)

# Insert Pluto
planets.insert(9, "pluto")
print(planets)

# append()
planets = ["mercury", "venus"]

planets.append("earth")
print(planets)

# remove()

planets = ["mercury", "venus", "earth"]

planets.remove("mercury")
print(planets)

# pop()

planets = ["mercury", "venus", "earth"]

planets.pop()
print(planets)

# len()

planets = ["mercury", "venus", "earth"]

print(len(planets))

# Loop through a list

# Loop through a list

planets = ["mercury", "venus", "earth"]

for planet in planets:
    print(planet)