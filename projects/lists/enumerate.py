# This program uses enumerate to print
# the number and name of each item in a list.

planets = planets = ["mercury", "venus", "earth", "mars", "jupiter",
           "saturn", "uranus", "neptune", "pluto"]

for i, planet in enumerate(planets):
    print(f"{i + 1}. {planet.title()}")