# A difference returns the elements that are in the first set
# but not in the second set.
# We can use the - operator or the difference() method.

fav1 = {"action", "fantasy", "mystery", "adventure", "sci-fi"}
fav2 = {"comedy", "fantasy", "mystery", "romance"}

# difference (elements in one set but not the other)
diff = fav1 - fav2
print(diff)

# both - and difference() are equivalent
diff2 = fav2.difference(fav1)
print(sorted(diff2))