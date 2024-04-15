import unittest
from typing import List
class Solution:
	def leftRightDifference(self, nums: List[int]) -> List[int]:
		leftSum = [0]
		rightSum = [0]
		for i in range(len(nums)-1):
			if i == 0:
				leftSum = leftSum + [nums[i]]
				rightSum = [nums[len(nums)-1]] + rightSum
			else:
				leftSum = leftSum + [nums[i] + leftSum[i]]
				rightSum = [rightSum[len(rightSum)- i - 1] + nums[len(nums) - i - 1]] + rightSum
		
		return [abs(x-y) for x, y in zip(leftSum, rightSum)]

class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_leftRightDifference_ex1(self):
		# Arrange
		nums = [10,4,8,3]
		expectedAns = [15,1,11,22]

		# Act
		result = self.solution.leftRightDifference(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_leftRightDifference_ex2(self):
		# Arrange
		nums = [1]
		expectedAns = [0]

		# Act
		result = self.solution.leftRightDifference(nums)

		# Assert
		self.assertEqual(result, expectedAns)


if __name__ == "__main__":
	unittest.main()