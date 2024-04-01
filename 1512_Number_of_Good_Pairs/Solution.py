import unittest
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count +=1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numIdenticalPairs_passArrayWithDuplicates_returnNumofDuplicates(self):
        # Arrange
        nums = [1,2,3,1,1,3]
        expectedAns = 4

        # Act
        ans = self.solution.numIdenticalPairs(nums)

        # Assert
        self.assertEqual(ans, expectedAns)

    def test_numIdenticalPairs_passArrayWithNoDuplicates_returnZero(self):
        # Arrange
        nums = [1,2,3,4,5,6]
        expectedAns = 0

        # Act
        ans = self.solution.numIdenticalPairs(nums)

        # Assert
        self.assertEqual(ans, expectedAns)

if __name__ == '__main__':
    unittest.main()
