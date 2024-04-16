import unittest
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
        	if nums[i] >= k:
        		return i
        return len(nums)

class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_minOperations_ex1(self):
		# Arrange
		nums = [2,11,10,1,3]
		k = 10
		expectedResult = 3

		# Act
		result = self.solution.minOperations(nums, k)

		# Assert
		self.assertEqual(result, expectedResult)

	def test_minOperations_ex2(self):
		# Arrange
		nums = [1,1,2,4,9]
		k = 1
		expectedResult = 0

		# Act
		result = self.solution.minOperations(nums, k)

		# Assert
		self.assertEqual(result, expectedResult)


if __name__ == "__main__":
	unittest.main()