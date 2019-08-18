import unittest
from test1 import sum, multi, minus
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(1,2), 0, "Should be 3")

    def test_minus(self):
        self.assertEqual(minus(3,2), 1, "Should be 1")

    def test_multi(self):
        self.assertEqual(multi(2,3), 6, "Should be 6")

if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
