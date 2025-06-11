""" Unstructured journalling is free writing without and pre-sets. I.E "What are your grateful for?" already written in
the journal. You just write freely. 
According to https://en.wikipedia.org/wiki/Diary the word 'journal' and 'diary' are often used interchangeably. But
a 'diary' aims to have daily entries whereas a 'journal' entries can be done less often. """

"""This is a command-line journal to improve privacy and to provide a feeling ease when writing. You can just relax and
write freely as this is an unstructured journal."""

# import libraries
from argparse import ArgumentParser
from datetime import date
import sys

# Assist the user to use the programme
parser = ArgumentParser("A Command line journal")
parser.add_argument("-n", "--new", help="Make a new journal entry", action="store_true")
parser.add_argument("-v", "--view", help="To view your journal entries", action="store_true")
args = parser.parse_args()

# Today's date
date = date.today()


def main():
	# Further assist the user on the commandline
	check_cmdline()
	
	# Execute the user's disire
	if args.new:
    		entry = input("Feel free to make your entry: ")        		
    		print(make_entry(entry))    		
	elif args.view:
    		with open("journal.txt", "r") as file:
        		for line in file:
            			print(line.rstrip())
            			
def check_cmdline():
	if len(sys.argv) < 2:
		sys.exit("Too few arguments. Type{python3 journal.py -h] for help}")
            			
            			
def make_entry(entry: str) -> None:
	if isinstance(entry, int) == True:
		raise TypeError("Your entry must be a str.")
	if entry.isdigit():
		raise ValueError("Those are only digits.")
	else:
		with open("journal.txt", "a") as file:
        		file.write(f"{date}\nDear journal\n{entry}\n")
        		return "Your entry as been entered into your yournal successfully."
       
	      
        	
            		
if __name__ == "__main__":
	main()
