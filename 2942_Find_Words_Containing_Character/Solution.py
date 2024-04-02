import unittest
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findWordsContaining_inputWordsThatContainCharacter_returnIndexesArray(self):
        # Arrange
        words = ["hello", "hashan", "eee"]
        x = "e"
        expectedAns = [0,2]

        # Act
        ans = self.solution.findWordsContaining(words, x)

        # Assert
        self.assertEqual(ans, expectedAns)

    def test_findWordsContaining_inputWordsThatNotContainCharacter_returnEmptyArray(self):
        # Arrange 
        words = ["hello", "hashan", "eee"]
        x = "i"
        expectedAns = []

        # Act
        ans = self.solution.findWordsContaining(words, x)

        # Assert
        self.assertEqual(ans, expectedAns)

if __name__ == '__main__':
    unittest.main()
