from typing import List
import unittest

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getConcatenation_inputNormalArray_returnDuplicateArray(self):
        # Arrange 
        nums = [1,2,1]
        expectedResult = [1,2,1,1,2,1]

        # Act
        ans = self.solution.getConcatenation(nums)

        # Assert
        self.assertEqual(ans, expectedResult)

    def test_getConcatenation_inputNormalArray_returnDuplicateArray_2(self):
        # Arrange 
        nums = [1,3,2,1]
        expectedResult = [1,3,2,1,1,3,2,1]

        # Act
        ans = self.solution.getConcatenation(nums)

        # Assert
        self.assertEqual(ans, expectedResult)

if __name__ == '__main__':
    unittest.main()
