# Punctuation we want to filter
punctuation = ".,!?;:\"'()[]-_"

text = input("Enter the text to process: ")
# Convert to lowercase for comparisions
text = text.lower()

# Loop through each punctuation symbol and replace it with empty string ""
for char in punctuation:
    text = text.replace(char, "")

# Split remaining text on spaces into a set to discard duplicates
words = set(text.split(" "))

print("Here are the unique words: ")
print(words)