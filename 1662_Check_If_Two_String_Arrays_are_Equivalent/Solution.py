import unittest
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        compStr1 = "".join(word1)
        compStr2 = "".join(word2)

        if compStr1 == compStr2:
            return True
        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_arrayStringAreEqual_inputSuccessWords_returnTrue(self):
        # Arrange
        word1 = ["ab", "c"]
        word2 = ["a", "bc"]
        expectedAns = True

        # Act
        ans = self.solution.arrayStringsAreEqual(word1, word2)

        # Assert
        self.assertEqual(ans, expectedAns)


if __name__ == '__main__':
    unittest.main()
