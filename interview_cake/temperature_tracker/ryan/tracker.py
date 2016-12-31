import sys
from collections import defaultdict


class Tracker:
    def __init__(self):
        self._min = sys.maxsize
        self._max = -sys.maxsize
        self._mean = 0
        self._count = 0
        self._mode = 0
        self.temps = defaultdict(int)

    def insert(self, temp):
        self._min = min(self._min, temp)
        self._max = max(self._max, temp)
        self._mean = (self._mean * self._count + temp) / (self._count + 1)
        self.temps[temp] += 1
        if self.temps[temp] > self.temps[self._mode]:
            self._mode = temp
        self._count += 1

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def get_mean(self):
        return self._mean

    def get_mode(self):
        return self._mode
