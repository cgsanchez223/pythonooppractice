"""Python serial number generator."""

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

    def __init__(self, start=0):
        """Starting point"""

        self.start = self.next = start

    def __repr__(self):
        """Returns representation of starting object"""

        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """Generates the next number"""

        self.next += 1
        return self.next - 1
    
    def reset(self):
        """To reset the number back to start"""

        self.next = self.start


serial = SerialGenerator(start=100)
serial.generate() # 100
serial.generate() # 101
serial.reset()
serial.generate() # 100