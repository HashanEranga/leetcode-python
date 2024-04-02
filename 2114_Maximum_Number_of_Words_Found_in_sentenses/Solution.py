import unittest
from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxCount = 0
        for sentence in sentences:
            count = len(sentence.split(" "))
            if count > maxCount:
                maxCount = count
        return maxCount

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mostWordsFound_inputSentences_returnMostWordsCount(self):
        # Arrange
        sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
        expectedAns = 6

        # Act
        ans = self.solution.mostWordsFound(sentences)

        # Assert
        self.assertEqual(ans, expectedAns)


if __name__ == '__main__':
    unittest.main()



