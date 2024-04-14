import unittest
from typing import List
class Solution:
	def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
		sum = 0
		for i in range(len(nums)):
			bin = self.decToBin(i)
			isWithKSetBits = self.isWithKSetBits(bin, k)
			if isWithKSetBits:
				sum += nums[i]
		return sum
		
	def decToBin(self, num) -> str:
		binNum = []
		while num > 1:
			binNum.append(num % 2)
			num = num // 2
		binNum.append(num)
		
		return "".join(map(str, binNum[::-1]))
	
	def isWithKSetBits(self, bin: str, k: int) -> bool:
		count = 0
		for i in bin:
			if i == '1':
				count += 1
		if k == count:
			return True
		else:
			return False
	
	def sumIndicesWithKSetBits_alter(self, nums: List[int], k: int) -> int:
		sum = 0
		for i in range(len(nums)):
			index = i
			countOnes = 0
			while i > 1:
				if i % 2 == 1:
					countOnes+=1
				i = i // 2

			if i == 1:
				countOnes += 1

			if k == countOnes:
				sum += nums[index]
		return sum
		

class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_sumIndicesWithSetBits_ex1(self):
		# Arrange
		nums = [5,10,1,5,2]
		k = 1
		expectedAns = 13

		# Act
		result = self.solution.sumIndicesWithKSetBits(nums, k)

		# Assert
		self.assertEqual(result, expectedAns)
	
	def test_sumIndicesWithSetBits_ex2(self):
		# Arrange
		nums = [4,3,2,1]
		k = 2
		expectedAns = 1

		# Act
		result = self.solution.sumIndicesWithKSetBits(nums, k)

		# Assert
		self.assertEqual(result, expectedAns)
	
	def test_sumIndicesWithKSetBits_alter_ex1(self):
		# Arrange
		nums = [5,10,1,5,2]
		k = 1
		expectedAns = 13

		# Act
		result = self.solution.sumIndicesWithKSetBits_alter(nums, k)

		# Assert
		self.assertEqual(result, expectedAns)
	
	def test_sumIndicesWithKSetBits_alter_ex2(self):
		# Arrange
		nums = [4,3,2,1]
		k = 2
		expectedAns = 1

		# Act
		result = self.solution.sumIndicesWithKSetBits_alter(nums, k)

		# Assert
		self.assertEqual(result, expectedAns)


if __name__ == "__main__":
	unittest.main()