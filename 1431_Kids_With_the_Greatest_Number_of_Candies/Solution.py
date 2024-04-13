import unittest
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNumOfCandies = 0
        for candy in candies:
            if candy > maxNumOfCandies:
                maxNumOfCandies = candy
            
        print(maxNumOfCandies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxNumOfCandies:
                candies[i] = True
            else:
                candies[i] = False
        
        return candies


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kidsWithCandies_generalCase_provideGeneralResult(self):
        # Arrange
        candies = [2,3,5,1,3]
        extraCandies = 3
        expectedResult = [True,True,True,False,True]

        # Act 
        result = self.solution.kidsWithCandies(candies, extraCandies)

        # Assert 
        self.assertEqual(result, expectedResult)

    def test_kidsWithCandies_generalCase_provideGeneralResult2(self):
        # Arrange
        candies = [4,2,1,1,2]
        extraCandies = 1
        expectedResult = [True,False,False,False,False]

        # Act 
        result = self.solution.kidsWithCandies(candies, extraCandies)

        # Assert 
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
