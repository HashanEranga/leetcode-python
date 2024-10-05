from problem import Problem
import unittest

class Test_Solution(unittest.TestCase):
    def setUp(self):
        self.solution = Problem()

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

        # Arrange
        self.assertEqual(result, expectedAns)
