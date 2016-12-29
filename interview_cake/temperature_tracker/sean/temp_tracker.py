import sys
from collections import defaultdict


class TempTracker:
    def __init__(self):
        self.num_inserted = 0
        self.mean = 0
        self.maximum = -sys.maxsize - 1
        self.minimum = sys.maxsize
        self.count_dict = defaultdict(int)

    def insert(self, temp):
        if temp not in range(0, 111):
            raise ValueError("Temperature not in range [0, 110]")
        self._update_bounds(temp)
        self._update_mean(temp)
        self._update_count_dict(temp)
        self._update_median()
        self._update_mode()

    def _update_bounds(self, temp):
        if temp < self.minimum:
            self.minimum = temp
        elif temp > self.maximum:
            self.maximum = temp

    def _update_mean(self, temp):
        self.total = self.mean * self.num_inserted
        self.mean = (self.total + temp) / (self.num_inserted + 1)
        self.num_inserted += 1

    def _update_count_dict(self, temp):
        self.count_dict[temp] += 1

    def _update_median(self):
        total_points = self.num_inserted
        index = self.minimum
        running_total = 0
        while running_total < self.num_inserted // 2:
            running_total += self.count_dict[index]
            index += 1
        self.median = index

    def _update_mode(self):
        self.mode = max(
            self.count_dict,
            key = lambda x: self.count_dict[x],
        )
