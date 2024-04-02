import unittest
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            result.append(count)
        return result

class TestSection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_smallerNumbersThanCurrent_inputAcceptedArray_returnAcceptedArray(self):
        # Arrange
        nums = [1,2,3,4,5]
        expected = [0,1,2,3,4]

        # Act
        ans = self.solution.smallerNumbersThanCurrent(nums)

        # Assert
        self.assertEqual(ans, expected)

if __name__ == '__main__':
    unittest.main()
