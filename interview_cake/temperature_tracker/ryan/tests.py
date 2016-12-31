import unittest
from tracker import Tracker


class TemperatureTrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.tracker = Tracker()
        temps = [1, 1, 17, 85, 2, 85, 85, 102, 4, 56]
        [self.tracker.insert(temp) for temp in temps]

    def test_min(self):
        self.assertEqual(self.tracker.get_min(), 1)

    def test_max(self):
        self.assertEqual(self.tracker.get_max(), 102)

    def test_mean(self):
        self.assertEqual(self.tracker.get_mean(), 43.8)

    def test_mode(self):
        self.assertEqual(self.tracker.get_mode(), 85)


if __name__ == '__main__':
    unittest.main()
