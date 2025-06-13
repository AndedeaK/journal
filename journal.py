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

# Reused message
message1 = "Feel free to make your entry: " 

def main():
    # Further assist the user on the commandline
    check_cmdline()

    # A welcome messge to the user
    message = "Welcome to your journal"
    greet(message)

    # Execute the user's disire
    try:
        if args.new:                       
            interact(make_entry(input(message1)))           
        if args.view:            
            interact1("Here's your entries.")            
            file_path = "journal.txt"
            view_entry(file_path)
            answer = input("Do you wish to make a new entry? yes/y or no/n? ")
            if answer == "yes" or answer == "y":
                interact(make_entry(input(message1)))                              
            elif answer == "no" or answer == "n":
                sys.exit(
                    emoji.emojize(
                        "Ok. Goodbye. :smiley:", language="alias", variant="emoji_type"
                    )
                )        
            else:
                sys.exit("Invalid input.")
    except EOFError:
        print(
            emoji.emojize(
                "Ctrl+D pressed. Goodbye. :smiley:",
                language="alias",
                variant="emoji_type",
            )
        )


def check_cmdline():
    """
    Checks if at least one argument is given when running the programme.
    Checks if the user is using the programme correctly.
    Offers the user guidance on how to use the program
    :raise SysExit: if too few arguments.
    """
    if len(sys.argv) < 2:
        sys.exit("Too few arguments. Type{python3 journal.py -h] for help}")


def greet(message: str) -> None:
    """
    Greets the user

    :param message: message to greet the user.
    :type entry: str
    :raise TypeError: if message is not a str
    :return: Nothing to be returned.
    """
    if isinstance(message, int) == True:
        raise TypeError("Message must be a str.")
    cowsay.cow(message)
    engine.say(message)
    engine.runAndWait()
    engine.stop()

def interact(feedback: str) -> None:
    """
    Interacts with the user when they have made a new entry

    :param message: message to update the user after making a new entry.
    :type entry: str
    :raise TypeError: if message is not a str
    :return: Nothing to be returned.
    """
     
    if  isinstance(feedback, int) == True:
        raise TypeError("Message must be a str.")
    cowsay.cow(feedback)
    engine.say(feedback)
    engine.runAndWait()
    engine.stop()

def interact1(message2: str) -> None:
    """
    Interacts with the user when they choose to view journal entries

    :param message: message to update the user on what they are viewing.
    :type entry: str
    :raise TypeError: if message is not a str
    :return: Nothing to be returned.
    """
    if isinstance(message2, int) == True:
        raise TypeError("Message must be a str.")
    cowsay.cow(message2)
    engine.say(message2)
    engine.runAndWait()
    engine.stop()

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
    with open("journal.txt", "a") as file:
        file.write(f"{date}\nDear journal\n{entry}\n")
    return emoji.emojize("Your entry as been entered successfully. :thumbs_up:")


def view_entry(file_path: str) -> None:
    """
    Allows the user to view entries made.

    :param file_path: path to file to be opened
    :type file_path: path to a .txt file
    :raise FileNotFoundError: if "journal.txt" does not exist.
    :return: None
    """
    if not file_path:
        raise FileNotFoundError
    with open(file_path, "r") as file:
        for line in file:
            print(line.rstrip())


if __name__ == "__main__":
    main()
