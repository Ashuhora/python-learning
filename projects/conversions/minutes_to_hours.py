# Minutes to Hours Converter


total_minutes = int(input("Enter the number of minutes:"))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60


print(f"{total_minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")