# using the split string method
# by default split uses space as the delimiter.

sentence = "We love Python!"
words = sentence.split()

print(type(words))
print(words)

# Split CSV data using commas

color_csv = "red,green,blue"
colors = color_csv.split(",")

for color in colors:
    print(color)

# We can also condense it into a single statement.

for color in color_csv.split(","):
    print(color)

# Limit the number of splits

csv_header = "user_name,rating,notes"
csv_data = "jsmith,5,This is a great product! However, the price is a bit high"

# Limit the result to three columns by splitting only two commas.

columns = csv_data.split(",", 2)

for column in columns:
    print(column)
