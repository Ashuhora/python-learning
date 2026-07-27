# union combines all the unique elements from two sets.
# We can use the | operator or the union() method. think of like "merge"

fav1 = {"action", "fantasy", "mystery", "adventure", "sci-fi"}
fav2 = {"comedy", "fantasy", "mystery", "romance"}

# union (all elements from both sets)
combined = fav1 | fav2
print(combined)

# both | and union() are equivalent. this also sorted.
combined2 = fav1.union(fav2)
print(sorted(combined2))