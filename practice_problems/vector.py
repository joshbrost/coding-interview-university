class Vector:
    def __init__(self, capacity = 16):
        self._capacity = max(capacity, 16)
        self._size = 0
        self._data = None * self._capacity
    def size(self):
        return self._size
    def capacity(self):
        return self._capacity
    def is_empty(self):
        return self._size == 0
    def at(self, index):
        if index < 0 or index > self._size:
            raise IndexError('Index is out of bounds')
        else:
            return self._data[index]
    def push(self, item):
        """
        Append an item to the end of the vector.
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = item
        self._size += 1

    def insert(self, index, item):
        """
        Insert an item at the given index, shifting elements to the right.
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = item
        self._size += 1

    def prepend(self, item):
        """
        Prepend an item to the vector.
        """
        self.insert(0, item)

    def pop(self):
        """
        Remove and return the last item of the vector.
        """
        if self._size == 0:
            raise IndexError("Pop from empty vector")
        item = self._data[self._size - 1]
        self._data[self._size - 1] = None  # Clean up the reference
        self._size -= 1
        if self._size > 0 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        return item

    def delete(self, index):
        """
        Delete an item at the given index, shifting elements left.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None  # Clean up the reference
        self._size -= 1
        if self._size > 0 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)

    def remove(self, item):
        """
        Remove all occurrences of an item from the vector.
        """
        i = 0
        while i < self._size:
            if self._data[i] == item:
                self.delete(i)
            else:
                i += 1

    def find(self, item):
        """
        Return the index of the first occurrence of the item, or -1 if not found.
        """
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def _resize(self, new_capacity):
        """
        Resize the internal storage to a new capacity.
        """
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
        
    

    