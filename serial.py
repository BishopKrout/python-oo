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
    def __init__(self, start):
    """Is the starting number absed off input. Has two methods for going up or reset"""
        self.start = start
        self.current = start
    
    def generate(self):
    """Running this will add one to the starting input value"""
        self.current += 1
        return self.current

    def reset(self):
    """Running this will reset value to original input"""
        self.current = self.start
        return self.current

    def __repr__(self):
    """Will display the current readible value in the terminal"""
        return f"{self.current}"


