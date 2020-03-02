import unittest
import task
import datetime


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testArea(self):
        pi = 3.14159265359
        expected = pi * (4 * 4)
        self.assertEqual(expected, task.area(4))

    def testFirstAndLast(self):
        collection = ['a', 'b', 'c']
        expected = ['a', 'c']
        self.assertListEqual(expected, task.firstAndLast(collection))

    def testDateDifference(self):
        date1 = datetime.date(2020, 1, 5)
        date2 = datetime.date(2020, 1, 3)
        expected = 2
        self.assertEqual(expected, task.dateDifference(date1, date2))


if __name__ == "__main__":
    unittest.main()
