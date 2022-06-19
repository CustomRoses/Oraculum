"""
Oraculum is the softwware part of the oraculum machine.

See it at sub divo festival!
"""

import translators as ts
import random


def fix_file(file_name):
    """
    Fix a file.
    """
    text = ""
    with open(file_name, 'r') as f:
        lines = f.readlines()
    if file_name == "quotes_lienying.txt":
        for line in lines:
            line = " ".join(line.split()[1:])
            text += line
        print(text)
        with open(f"{file_name}_fixed", 'w') as f:
            f.write(text)



def translate(text):
    """
    Translate quotes.
    """
    return ts.deepl(text)




def get_random_quote():
    """
    Get a random quote.
    """
    return random.choice(open("quotes_lienying.txt").readlines())