import unittest
from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
    	result = []
    	while len(nums) > 0:
    		tempList = []
    		tempList.append(min(nums))
    		nums.remove(min(nums))
    		tempList.insert(0, min(nums))
    		nums.remove(min(nums))
    		result += tempList
    	return result

    def numberGame_alter(self, nums: List[int]) -> List[int]:
    	nums.sort()
    	for i in range(0, len(nums), 2):
    		nums[i], nums[i+1] = nums[i+1], nums[i]

    	return nums	


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_numberGame_ex1(self):
		# Arrange
		nums = [5,4,2,3]
		expectedAns = [3,2,5,4]

		# Act
		result = self.solution.numberGame_alter(nums)

		# Assert
		self.assertEqual(result, expectedAns)


	def test_numberGame_ex2(self):
		# Arrange
		nums = [2,5]
		expectedAns = [5,2]

		# Act
		result = self.solution.numberGame_alter(nums)

		# Assert
		self.assertEqual(result, expectedAns)


if __name__ == "__main__":
	unittest.main()
