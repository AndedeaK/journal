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

# Cast the date to str for it to be written
date = str(d)

# Let us write the date to the text file with a new line
file1 = open("text", "a")

# Add the date to the text file
# You might want to consider if it is the first entry or not for knowing when to write new lines.
# This new line is just for looks
file1.write("\n \n")

file1.write(date)
file1.write("\n \n")
entry = [input("you may now make your entry: ")]
file1.writelines(entry)

# Remember to also close the file
file1.close

# entry = input("You may make your new entry: ")

# Now display the entry with date and time
""" print(d)
print(entry)
print("Would you like to save this entry?: y/n_") """


""" d = date(2023, 5, 23)
print(type(d.year)) """