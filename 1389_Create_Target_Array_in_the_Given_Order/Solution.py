import unittest
from typing import List
class Solution:
	def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
		result = []
		for num, indice in zip(nums, index):
			result.insert(indice, num)
		return result


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_createTargetArray_ex1(self):
		# Arrange
		nums = [0,1,2,3,4]
		index = [0,1,2,2,1]
		expectedAns = [0,4,1,3,2]

		# Act
		result = self.solution.createTargetArray(nums, index)

		# Assert
		self.assertEqual(result, expectedAns)


	def test_createTargetArray_ex2(self):
		# Arrange
		nums = [1,2,3,4,0]
		index = [0,1,2,3,0]
		expectedAns = [0,1,2,3,4]

		# Act
		result = self.solution.createTargetArray(nums, index)

		# Assert
		self.assertEqual(result, expectedAns)


if __name__ == "__main__":
	unittest.main()
