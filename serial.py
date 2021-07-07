class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Creates a serial generator from the number start"""

        self.start = start
        self.counter = -1

    def __repr__(self):
        """Describes this instance of SerialGenerator"""

        return f"<SerialGenerator start={self.start}, next={self.start + self.counter + 1}>"

    def generate(self):
        """Returns next sequential number of start"""

        self.counter += 1
        return self.start + self.counter

    def reset(self):
        """Resets start back to the original start number"""

        self.counter = -1
