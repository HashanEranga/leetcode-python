import unittest
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximumAmount = 0
        for personalWealth in accounts:
            currentAmount = 0
            for amount in personalWealth:
                currentAmount += amount

            if currentAmount > maximumAmount:
                maximumAmount = currentAmount

        return maximumAmount

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maximumWealth_passingAccountDetails_returnMaximumWealth(self):
        # Arrange
        accounts = [[1,2,3],[4,5,6],[7,8,9]]
        expectedAns = 24

        # Act
        ans = self.solution.maximumWealth(accounts)

        # Assert
        self.assertEqual(ans, expectedAns)

if __name__ == '__main__':
    unittest.main()
