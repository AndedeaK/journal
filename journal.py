""" Unstructured journalling is free writing without and pre-sets. I.E "What are your grateful for?" already written in
the journal. You just write freely. 
According to https://en.wikipedia.org/wiki/Diary the word 'journal' and 'diary' are often used interchangeably. But
a 'diary' aims to have daily entries whereas a 'journal' entries can be done less often. """

"""This is a command-line journal to improve privacy and to provide a feeling ease when writing. You can just relax and
write freely as this is an unstructured journal."""

# import libraries
from argparse import ArgumentParser
from datetime import date

date = date.today()

parser = ArgumentParser("A Command line journal")
parser.add_argument("-n", "--new", help="Make a new journal entry", action="store_true")
parser.add_argument("-v", "--view", help="To view your journal entries", action="store_true")
args = parser.parse_args()


if args.new:
    entry = input("Feel free to make your entry: ")
    with open("journal.txt", "a") as file:
        file.write(f"{date}\nDear journal\n{entry}\n")
elif args.view:
    with open("journal.txt", "r") as file:
        for line in file:
            print(line.rstrip())
    


# Create the apps help menu with -h