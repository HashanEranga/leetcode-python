import unittest
from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = set()
        for point in points:
            x.add(point[0])

        x = sorted(x)

        widestArea = 0
        for i in range(len(x)-1):
            newWidestArea = x[i+1] - x[i]
            if widestArea < newWidestArea:
                widestArea = newWidestArea

        return widestArea

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxWidthOfVerticalArea_AddPoints_ReturnVerticalArea(self):
        # Arrange
        points = [[8,7],[9,9],[7,4],[9,7]]
        expectedAns = 1

        # Act
        ans = self.solution.maxWidthOfVerticalArea(points)

        # Assert
        self.assertEqual(ans, expectedAns)

    def test_maxWidthOfVerticalArea_AddPoints_ReturnVerticalArea2(self):
        # Arrange
        points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
        expectedAns = 3

        # Act
        ans = self.solution.maxWidthOfVerticalArea(points)

        # Assert
        self.assertEqual(ans, expectedAns)

if __name__ == '__main__':
    unittest.main()
