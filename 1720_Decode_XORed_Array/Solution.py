import unittest
from typing import List
class Solution:
	def decode(self, encoded: List[int], first: int) -> List[int]:
		decodedList = []
		decodedList.append(first)
		for item in encoded:
			decodedList.append(item ^ first)
			first = item ^ first
		return decodedList
	
	def decode_recursive(self, encoded: List[int], first: int) -> List[int]:
		if not encoded:
			return [first]
		else:
			decodedList = self.decode_recursive(encoded[1:], encoded[0] ^ first)
			return [first] + decodedList


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_decode_ex1(self):
		# Arrange
		encoded = [1,2,3]
		first = 1
		expectedAns = [1,0,2,1]

		# Act
		result = self.solution.decode(encoded, first)

		# Assert
		self.assertEqual(result, expectedAns)
	
	def test_decode_ex2(self):
		# Arrange
		encoded = [6,2,7,3]
		first = 4
		expectedAns = [4,2,0,7,4]

		# Act
		result = self.solution.decode(encoded, first)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_decode_recursive_ex1(self):
		# Arrange
		encoded = [1,2,3]
		first = 1
		expectedAns = [1,0,2,1]

		# Act
		result = self.solution.decode_recursive(encoded, first)

		# Assert
		self.assertEqual(result, expectedAns)
	
	def test_decode_recursive_ex2(self):
		# Arrange
		encoded = [6,2,7,3]
		first = 4
		expectedAns = [4,2,0,7,4]

		# Act
		result = self.solution.decode_recursive(encoded, first)

		# Assert
		self.assertEqual(result, expectedAns)


if __name__ == "__main__":
	unittest.main()