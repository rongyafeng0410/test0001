import unittest


def divid(num1, num2):
    return num1 / num2


class MyTest(unittest.TestCase):
    def test1(self):
        assert (divid(1, 1) == 1)

    def test2(self):
        assert (divid(0, 1) == 0)

    def test3(self):
        assert (divid(2, 3) == 0)
print("hello")
if __name__ == "__main__":
    unittest.main()
