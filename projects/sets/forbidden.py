# This program censors forbidden espionage-related words in a paragraph.
# It replaces each forbidden word with asterisks (*) and counts how many words were redacted.

# List of forbidden words
forbidden_words = {'spy', 'agent', 'mission', 'classified', 'secret', 'intelligence',
                  'undercover', 'operative', 'espionage', 'covert'}

# Print the words
print(f"Forbidden words: {forbidden_words}")

# Get input from the user
text = input("Enter the text you want to check: ")

# Split the text into individual words
words = text.split()

# Create a list to store the processed words
redacted_text = []
count = 0

# Process each word
for word in words:
    # Check if the word is forbidden (case-insensitive)
    if word.lower() in forbidden_words:
        # Replace the word with the same number of asterisks
        redacted_word = "*" * len(word)
        redacted_text.append(redacted_word)
        count += 1
    else:
        # Keep the original word
        redacted_text.append(word)

# Join the processed words back into a paragraph
final_text = " ".join(redacted_text)

# Print the results
print("\nRedacted text:")
print(final_text)
print(f"\nFound and redacted {count} forbidden words.")