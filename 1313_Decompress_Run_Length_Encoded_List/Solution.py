import unittest
from typing import List

class Solution:
	def decompressRLElist(self, nums: List[int]) -> List[int]:

		result = []
		for i in range(0, len(nums), 2):
			freq = nums[i]
			val = nums[i+1]

			tempList = []

			for _ in range(freq):
				tempList.append(val)

			result += tempList

		return result


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_decompressRLElist_ex1(self):
		# Arrange
		nums = [1,2,3,4]
		expectedAns = [2,4,4,4]

		# Act	
		result = self.solution.decompressRLElist(nums)

		# Assert
		self.assertEqual(result, expectedAns)


	def test_decompressRLElist_ex2(self):
		# Arrange 	
		nums = [1,1,2,3]
		expectedAns = [1,3,3]

		# Act
		result = self.solution.decompressRLElist(nums)

		# Assert
		self.assertEqual(result, expectedAns)

if __name__ == '__main__':
	unittest.main()



