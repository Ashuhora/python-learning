# Parties, per instructions
# This program asks the user for their favorite music genres
# and recommends the party that best matches their music taste.
party1 = {"Rock", "Pop", "Hip Hop", "Electronic", "Country"}
party2 = {"Jazz", "Blues", "Rock", "Classical", "Pop"}
party3 = {"Metal", "Punk", "Alternative", "Rock", "Indie"}

user_genres = set()

print("Welcome to the Music Matchmaker!")
print("Tell us what music genres you enjoy, and we'll match you with a party.")
print("Enter 'Q' to quit when you're done.\n")

# Get the user preferences and Keep asking the user for music genres
while True:
    genre = input("Enter a music genre you enjoy (or 'Q' to quit): ")
    
 # Stop the loop if the user enters Q
    if genre.strip().upper() == 'Q':
        break
    
    # Add the genre to the user's set of preferences (using title case for consistency)
    user_genres.add(genre.strip().title())
# Variables to store the most and the least party
best_party = ""
worst_party = ""
most_matches = 0
least_matches = 0

# Calculate the number of genres in common with each party
matches_party1 = len(user_genres.intersection(party1))
matches_party2 = len(user_genres.intersection(party2))
matches_party3 = len(user_genres.intersection(party3))

# Is party 1 the best?
if matches_party1 >= matches_party2 and matches_party1 >= matches_party3:
    best_party = "Party 1"
    most_matches = matches_party1

    # Party 1 is the best, now which is the worst?
    if matches_party2 <= matches_party3:
        least_matches = matches_party2
        worst_party = "Party 2"
    else:
        least_matches = matches_party3
        worst_party = "Party 3"

# Is party 2 the best?
elif matches_party2 >= matches_party1 and matches_party2 >= matches_party3:
    best_party = "Party 2"
    most_matches = matches_party2

    # compare if Party 2 is the best, now which is the worst?
    if matches_party1 <= matches_party3:
        least_matches = matches_party1
        worst_party = "Party 1"
    else:
        least_matches = matches_party3
        worst_party = "Party 3"
# party 3 must be the best
else:
    best_party = "Party 3"

    # Party 3 is the best, now which is the worst?
    if matches_party1 <= matches_party2:
        least_matches = matches_party1
        worst_party = "Party 1"
    else:
        least_matches = matches_party2
        worst_party = "Party 2"

# Display results or the recomendation
print(f"You would likely enjoy {best_party} the most!")
print(f"You share {most_matches} music genres with {best_party}.")
print(f"You would probably enjoy {worst_party} the least.")
print(f"You only share {least_matches} music genre with {worst_party}.")

