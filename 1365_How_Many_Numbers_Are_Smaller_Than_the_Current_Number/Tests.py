import unittest
import Problem

class Test_Solution(unittest.TestCase):
    def setUp(self):
        self.solution = Problem.Solution()

    def test_smallerNumbersThanCurrent_directSolution_average_case1(self):
        # Arrange
        nums = [8,1,2,2,4]
        expectedAns = [4,0,1,1,3]

        # Act
        result = self.solution.smallerNumbersThanCurrent_directSolution(nums)

        # Assert
        self.assertEqual(result, expectedAns)

    def test_smallerNumbersThanCurrent_directSolution_average_case2(self):
        # Arrange
        nums = [6,5,4,8]
        expectedAns = [2,1,0,3]

        # Act
        result = self.solution.smallerNumbersThanCurrent_directSolution(nums)

        # Assert
        self.assertEqual(result, expectedAns)

    def test_smallerNumbersThanCurrent_directSolution_average_case3(self):
        # Arrange
        nums = [7,7,7,7]
        expectedAns = [0,0,0,0]

        # Act
        result = self.solution.smallerNumbersThanCurrent_directSolution(nums)

        # Assert
        self.assertEqual(result, expectedAns)

if __name__ == '__main__':
    unittest.main()
