# A symmetric difference returns the elements that are unique
# to each set (elements that are not in both sets).
# We can use the ^ operator or the symmetric_difference() method.

fav1 = {"action", "fantasy", "mystery", "adventure", "sci-fi"}
fav2 = {"comedy", "fantasy", "mystery", "romance"}

# difference ( elements in one set but not the other)
result = fav1 ^ fav2
print(result)

# both ^ and symmetric_difference() are equivalent
# sorted() returns a list, not a set.
result2 = fav1.symmetric_difference(fav2)
print(sorted(result2))