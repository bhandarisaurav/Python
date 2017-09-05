import unittest

def isVowel(a):
    if a.lower() in ('a','e','i','o','u'):
        return True
    else:
        return False


class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(isVowel("b"),False)

    def test2(self):
        self.assertEqual(isVowel("a"), True)
    #

    # def test2(self):
    #     self.assertEqual(6,7)

if __name__ == '__main__':
    unittest.main()