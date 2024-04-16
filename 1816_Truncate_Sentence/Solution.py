import unittest
from typing import List

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
    	return " ".join(s.split(" ")[0:k])


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_truncateSentence_ex1(self):
		# Arrange
		s = "Hello how are you Contestant"
		k = 4
		expectedAns = "Hello how are you"

		# Act
		result = self.solution.truncateSentence(s, k)

		# Assert
		self.assertEqual(result, expectedAns)

	def test_truncateSentence_ex2(self):
		# Arrange
		s = "What is the solution to this problem"
		k = 4
		expectedAns = "What is the solution"

		# Act
		result = self.solution.truncateSentence(s, k)

		# Assert
		self.assertEqual(result, expectedAns)


if __name__ == "__main__":
	unittest.main()