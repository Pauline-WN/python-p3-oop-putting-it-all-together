class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Old"  # Default condition when shoe is created

    # Getter and Setter for size with validation
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Sets condition to "New" after repair
