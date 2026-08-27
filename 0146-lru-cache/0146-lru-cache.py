from collections import deque

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.q = deque()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.q.remove(key)
        self.q.append(key)

        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.q.remove(key)

        self.cache[key] = value

        self.q.append(key)

        if len(self.q) > self.capacity:
            old = self.q.popleft()
            del self.cache[old]