import unittest
from collections import defaultdict
from temp_tracker import TempTracker


class TempTrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_tracker = TempTracker()

    def test_count_dict(self):
        temps_list = [1,4,2,3,4,110,4]
        for point in temps_list:
            self.temp_tracker.insert(point)
        test_dict = defaultdict(
            int,
            {
                1:1,
                2:1,
                3:1,
                4:3,
                110:1,
            },
        )
        self.assertEqual(self.temp_tracker.count_dict, test_dict)

    def test_median(self):
        temps_list = [1,4,2,3,4,110,4]
        for point in temps_list:
            self.temp_tracker.insert(point)
        target = 4
        self.assertEqual(self.temp_tracker.median, target)

    def test_mean(self):
        temps_list = [1,4,2,3,4,110,4]
        for point in temps_list:
            self.temp_tracker.insert(point)
        target = sum(temps_list) / len(temps_list)
        self.assertEqual(self.temp_tracker.mean, target)

    def test_mode(self):
        temps_list = [1,4,2,3,4,110,4]
        for point in temps_list:
            self.temp_tracker.insert(point)
        target = 4
        self.assertEqual(self.temp_tracker.mode, target)

    def test_min(self):
        temps_list = [-110,1,4,2,3,4,110,4]
        for point in temps_list:
            self.temp_tracker.insert(point)
        target = -110
        self.assertEqual(self.temp_tracker.minimum, target)

    def test_max(self):
        temps_list = [1,4,2,3,4,110,4]
        for point in temps_list:
            self.temp_tracker.insert(point)
        target = 110
        self.assertEqual(self.temp_tracker.maximum, target)


if __name__ == '__main__':
    unittest.main()
