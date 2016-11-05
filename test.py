import unittest

def IsOdd(n):
    
    if n % 2 == 0:
        return False
    else:
        return True

# Here's our "unit tests".


class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))


def main():

    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(IsOddTests)
        unittest.TextTestRunner(verbosity=2).run(suite)

main()
