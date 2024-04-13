import unittest
from typing import List
class Solution:
	def countPairs(self, nums: List[int], target: int) -> int:
		count = 0
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] < target:
					count +=1
		return count


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_countPairs_generalCase_returnGeneralResult(self):
		# Arrange
		nums = [-1,1,2,3,1]
		target = 2
		expectedAns = 3

		# Act
		result = self.solution.countPairs(nums, target)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_countPairs_generalCase_returnGeneralResult2(self):
		# Arrange
		nums = [-6,2,5,-2,-7,-1,3]
		target = -2
		expectedAns = 10

		# Act
		result = self.solution.countPairs(nums, target)

		# Assert
		self.assertEqual(result, expectedAns)


if __name__ == "__main__":
	unittest.main()