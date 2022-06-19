"""
Oraculum is the softwware part of the oraculum machine.

See it at sub divo festival!
"""

from argostranslate import translate
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
            sp = line.strip().split(" ")
            cutoff = 1 if ")" in sp[0] else 2
            print(sp[cutoff:], cutoff)
            text += " ".join(sp[cutoff:]) + "\n"
        print(text)
        with open(f"{file_name}_fixed", 'w') as f:
            f.write(text)


class Oraculum:
    """
    Oraculum is the softwware part of the oraculum machine.
    """
    def __init__(self):
        self.filepath_DE = "weisheiten_DE"
        self.filepath_LAT = "weisheiten_LAT"
        with open(self.filepath_DE, 'r', encoding="utf-8") as f:
            lines_DE = f.readlines()
        with open(self.filepath_LAT, 'r', encoding="utf-8") as f:
            lines_LAT = f.readlines()

        self.quotes = {}
        for de, lat in zip(lines_DE, lines_LAT):
            self.quotes[de.strip()] = lat.strip()


    def get_random_quote(self):
        """
        Get a random quote.
        """
        return random.choice(list(self.quotes.items()))

    def __len__(self):
        return len(self.quotes)

    def __getitem__(self, key):
        return self.quotes[key]

    def __setitem__(self, key, value):
        self.quotes[key] = value

    def __delitem__(self, key):
        del self.quotes[key]

    def __contains__(self, key):
        return key in self.quotes

    def __iter__(self):
        return iter(self.quotes)

    def __reversed__(self):
        return reversed(self.quotes)

    def __str__(self):
        return str(self.quotes)

    def __repr__(self):
        return repr(self.quotes)




