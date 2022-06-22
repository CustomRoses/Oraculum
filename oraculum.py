"""
Oraculum is the softwware part of the oraculum machine.

See it at sub divo festival!+
"""
import sys
import random
from collections import deque
from escpos.printer import Usb


def fix_file(file_name):
    """
    Fix a file.
    """
    text = ""
    with open(file_name, "r") as f:
        lines = f.readlines()
    if file_name == "quotes_lienying.txt":
        for line in lines:
            sp = line.strip().split(" ")
            cutoff = 1 if ")" in sp[0] else 2
            print(sp[cutoff:], cutoff)
            text += " ".join(sp[cutoff:]) + "\n"
        print(text)
        with open(f"{file_name}_fixed", "w") as f:
            f.write(text)


class Oraculum:
    """
    Oraculum is the softwware part of the oraculum machine.
    """

    def __init__(
        self,
        quotes_file_de="weisheiten_DE",
        quotes_file_lat="weisheiten_LAT",
        repeat_limit=10,
    ):
        self.filepath_DE = quotes_file_de
        self.filepath_LAT = quotes_file_lat
        self.repeat_buffer = deque(maxlen=repeat_limit)
        self.quotes = []
        with open(self.filepath_DE, "r", encoding="utf-8") as f:
            lines_DE = f.readlines()
        with open(self.filepath_LAT, "r", encoding="utf-8") as f:
            lines_LAT = f.readlines()
        for de, lat in zip(lines_DE, lines_LAT):
            self.quotes.append((de.strip(), lat.strip()))

    def get_random_quote(self):
        """
        Get a random quote.
        """
        wisdom = random.choice(list(self.quotes))
        # prevent repeating the same quote if it is in the buffer
        if wisdom in self.repeat_buffer:
            return self.get_random_quote()
        self.repeat_buffer.appendleft(wisdom)
        return wisdom

    def __sizeof__(self):
        return (
            sys.getsizeof(self.quotes)
            + sys.getsizeof(self.repeat_buffer)
            + sys.getsizeof(self.filepath_DE)
            + sys.getsizeof(self.filepath_LAT)
            + sys.getsizeof(self.__dict__)
        )

    def _send_to_device(self, quote):
        """
        Send a quote to the device.
        """
        printer = Usb(0x1b8d, 0x0202)
        printer.set(align="center", font="a")
        printer.text(quote[0])
        printer.set(align="center", font="b")
        printer.text(quote[1])
        printer.cut()
        printer.close()


if __name__ == "__main__":
    oraculum = Oraculum()
    for _ in range(3):
        print(oraculum.get_random_quote())
