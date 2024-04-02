import unittest
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_shuffle_inputValidArray_returnShuffledArray(self):
        # Arrange 
        nums = [1,2,3,4,5,6]
        expectedResult = [1,4,2,5,3,6]
        n = 3

        # Act
        ans = self.solution.shuffle(nums, n)
        
        # Assert
        self.assertEqual(ans, expectedResult)


if __name__ == '__main__':
    unittest.main()

        

