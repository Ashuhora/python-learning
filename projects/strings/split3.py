# Limit the number of splits

csv_header = "user_name,rating,notes"
csv_data = "jsmith,5,This is a great product! However, the price is a bit high"

# Limit the result to three columns by splitting only two commas.

columns = csv_data.split(",", 2)

for column in columns:
    print(column)
