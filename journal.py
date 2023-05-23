# Import datetime date module
from datetime import date


# Make a new journal entry (python3 journal.py new)

    # Firstly, enter the date

# Get the date from the user
year, month, day = input("Please enter the date: ").split("-")

# change the date from string to int
year = int(year)
month = int(month)
day  = int(day)

d = date(year, month, day)

entry = input("You may make your new entry: ")

# Now display the entry with date and time
print(d)
print(entry)
print("Would you like to save this entry?: y/n_")


""" d = date(2023, 5, 23)
print(type(d.year)) """