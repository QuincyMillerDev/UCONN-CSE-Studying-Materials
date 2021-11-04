class CustomSet:
    def __init__(self):
        self.n_buckets = 100
        self._buckets = [[] for i in range(self.n_buckets)]
        self._length = 0

    def __len__(self):
        return self._length

    def __contains__(self, item):
        bucket = self.hash(item)
        for i in self._buckets[bucket]:
            if i == item:
                return True
        return False

    def hash(self, item):
        return hash(item) % self.n_buckets

    def rehash(self):
        self.n_buckets *= 2
        new_L = [[] for i in range(self.n_buckets)]
        
        # move all items to new list
        for bucket in self._buckets:
            for i in bucket:
                new_bucket = self.hash(i)
                new_L[new_bucket].append(i)

        self._buckets = new_L[:]

    def add(self, item):
        # If item is already in set, do nothing (so there are no duplicates)
        bucket = self.hash(item)
        if item in self._buckets[bucket]:
            return
        else:
            self._buckets[bucket].append(item)
            self._length += 1
            if self._length > self.n_buckets:
                self.rehash()

    def remove(self, item):
        # Raise ValueError if user tries to delete object not in our class
        bucket = self.hash(item)
        if item in self._buckets[bucket]:
            self._buckets[bucket].remove(item) 
            self._length -= 1
        else:
            raise(ValueError)