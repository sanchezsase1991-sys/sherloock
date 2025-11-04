import unittest
from src.sherloock import Sherloock

class TestSherloock(unittest.TestCase):
    def test_rules(self):
        sh = Sherloock()
        sh.add_rule(r'foo', 'bar')
        self.assertIn('bar', sh.reason("foo"))

    def test_forecast(self):
        sh = Sherloock()
        result = sh.reason("forecast [1,2,3,4,5]")
        self.assertIn("FORECAST", result)

if __name__ == "__main__":
    unittest.main()
