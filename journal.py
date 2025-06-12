"""Unstructured journalling is free writing without and pre-sets. I.E "What are your grateful for?" already written in
the journal. You just write freely.
According to https://en.wikipedia.org/wiki/Diary the word 'journal' and 'diary' are often used interchangeably. But
a 'diary' aims to have daily entries whereas a 'journal' entries can be done less often.
"""

"""This is a command-line journal to improve privacy and to provide a feeling ease when writing. You can just relax and
write freely as this is an unstructured journal."""

# import libraries
import cowsay
import pyttsx3
import emoji
from argparse import ArgumentParser
from datetime import date
import sys

# Assist the user to use the programme
parser = ArgumentParser("A Command line journal")
parser.add_argument("-n", "--new", help="Make a new journal entry", action="store_true")
parser.add_argument(
    "-v", "--view", help="To view your journal entries", action="store_true"
)
args = parser.parse_args()

# Objectify
date = date.today()
engine = pyttsx3.init()


def main():
    # Further assist the user on the commandline
    check_cmdline()
    cowsay.cow("Welcome to your journal.")
    engine.say("Welcome to your journal.")
    engine.runAndWait()
    engine.stop()
    # Execute the user's disire
    if args.new:        
        feedback = make_entry(input("Feel free to make your entry: "))
        cowsay.cow(feedback)
        engine.say(feedback)
        engine.runAndWait()
    elif args.view:
        cowsay.cow("Here is your entries.")
        engine.say("Here's your entries")
        engine.runAndWait()
        file_path = "journal.txt"
        view_entry(file_path)
        answer = input("Do you wish to make a new entry? yes/y or no/n? ")
        if answer == "yes" or answer == "y":
            feedback = make_entry(input("Feel free to make your entry: "))
            print(feedback)
        else:
            sys.exit(emoji.emojize("Goodbye. :smiley:", language='alias', variant='emoji_type'))
                  

        


def check_cmdline():
    """
    Checks if at least one argument is given when running the programme.
    Checks if the user is using the programme correctly.
    Offers the user guidance on how to use the program
    :raise SysExit: if too few arguments.
    """
    if len(sys.argv) < 2:
        sys.exit("Too few arguments. Type{python3 journal.py -h] for help}")


def make_entry(entry: str) -> str:
    """
    Enters the entry into the journal.
    
    :param entry: Entry to be entered into the journal.
    :type entry: str
    :raise TypeError: if entry is not a str
    :raise ValueError: if entry is only digits
    :return: A string which state that the entry has been entered successfully upon completion.
    :rtype: str
    """
    if isinstance(entry, int) == True:
        raise TypeError("Your entry must be a str.")
    if entry.isdigit():
        raise ValueError("Those are only digits.")
    else:
        with open("journal.txt", "a") as file:
            file.write(f"{date}\nDear journal\n{entry}\n")

    return emoji.emojize("Your entry as been entered successfully. :thumbs_up:")

def view_entry(file_path) -> None:
    """
    Allows the user to view entries made.

    :param file_path: path to file to be opened
    :type file_path: .txt file
    :raise FileNotFoundError: if "journal.txt" does not exist.    
    :return: None    
    """
    if not file_path:
        raise FileNotFoundError
    else:
        with open(file_path, "r") as file:
            for line in file:
                print(line.rstrip())
    

if __name__ == "__main__":
    main()
