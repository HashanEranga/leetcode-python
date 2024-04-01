from typing import List
import unittest

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            ans.append(nums[i])

        return ans


class TestSolution(unittest.TestCase):
    def test_buildArray_inputSequenceArray_returnSameArray(self):

        # Arrange
        solution = Solution()
        nums = [0,1,2,3,4]
        expectedAns = [0,1,2,3,4]

        # Act
        ans = solution.buildArray(nums)
        
        # Assert
        self.assertEqual(ans, expectedAns)

    def test_buildArray_inputRandomArray_returnExpectedResult(self):

        # Arrange
        solution = Solution()
        nums = [3,1,4,0,2]
        expectedAns = [0,1,2,3,4]

        # Act
        ans = solution.buildArray(nums)
        
        # Assert
        self.assertEqual(ans, expectedAns)

    def test_buildArray_inputRandomArray_returnExpectedResult_2(self):

        # Arrange
        solution = Solution()
        nums = [0,2,1,5,3,4] 
        expectedAns = [0,1,2,4,5,3]

        # Act
        ans = solution.buildArray(nums)
        
        # Assert
        self.assertEqual(ans, expectedAns)

    def test_buildArray_inputRandomArray_returnExpectedResult_3(self):

        # Arrange
        solution = Solution()
        nums = [5,0,1,2,3,4]
        expectedAns = [4,5,0,1,2,3]

        # Act
        ans = solution.buildArray(nums)
        
        # Assert
        self.assertEqual(ans, expectedAns)

    def test_buildArray_inputWrongFormattedArray_throwAnError(self):

        # Arrange
        solution = Solution()
        nums = [5,0,6,2,3,4]
        expectedAns = [4,5,0,1,2,3]

        # Act
        with self.assertRaises(IndexError):
            solution.buildArray(nums)


if __name__ == '__main__':
    unittest.main()
