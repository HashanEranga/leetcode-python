import unittest
from typing import List

class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		count = 0
		for i in range(len(nums)):
			count +=nums[i]
			nums[i] = count
		
		return nums
	
	def runningSum_alter(self, nums: List[int]) -> List[int]:
		for i in range(len(nums)):
			if i ==0:
				continue
			nums[i] += nums[i-1]
		return nums
	
	def runningSum_recursion(self, nums: List[int], index: int = None) -> List[int]:
		if index == None:
			index = len(nums) - 1

		if index == 0:
			return nums[0]

		else:
			prev_sums = self.runningSum_recursion(nums, index - 1)
			prev_sum = prev_sums[index -1]
			return prev_sums + [nums[index] + prev_sum] 


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_runningSum_ex1(self):
		# Arrange
		nums = [1,2,3,4]
		expectedAns = [1,3,6,10]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_runningSum_ex2(self):
		# Arrange
		nums = [1,1,1,1,1]
		expectedAns = [1,2,3,4,5]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_runningSum_ex3(self):
		# Arrange
		nums = [3,1,2,10,1]
		expectedAns = [3,4,6,16,17]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def setUp(self):
		self.solution = Solution()

	def test_runningSum_alter_ex1(self):
		# Arrange
		nums = [1,2,3,4]
		expectedAns = [1,3,6,10]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_runningSum_alter_ex2(self):
		# Arrange
		nums = [1,1,1,1,1]
		expectedAns = [1,2,3,4,5]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_runningSum_alter_ex3(self):
		# Arrange
		nums = [3,1,2,10,1]
		expectedAns = [3,4,6,16,17]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_runningSum_recursion_ex1(self):
		# Arrange
		nums = [1,2,3,4]
		expectedAns = [1,3,6,10]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_runningSum_recursion_ex2(self):
		# Arrange
		nums = [1,1,1,1,1]
		expectedAns = [1,2,3,4,5]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_runningSum_recursion_ex3(self):
		# Arrange
		nums = [3,1,2,10,1]
		expectedAns = [3,4,6,16,17]

		# Act
		result = self.solution.runningSum(nums)

		# Assert
		self.assertEqual(result, expectedAns)	

if __name__ == "__main__":
	unittest.main()