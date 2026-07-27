# An intersection returns only the elements that exist in both sets.
# it can use the & operator or the intersection() method.

fav1 = {"action", "fantasy", "mystery", "adventure", "sci-fi"}
fav2 = {"comedy", "fantasy", "mystery", "romance"}

# intersection (elements in both sides)
matches = fav1 & fav2
print(matches)

# both & and intersection are equivalent
matches2 = fav1.intersection(fav2)
print(sorted(matches2))
