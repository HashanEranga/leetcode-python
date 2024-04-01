from typing import List
from parameterized import parameterized, parameterized_class
import unittest

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums


class TestSolution(unittest.TestCase):
    def test_getConcatenation(self):
        test_cases = [
            [[1,2,1], [1,2,1,1,2,1]],
            [[1,1,1], [1,1,1,1,1,1]]
        ]
        solution = Solution()

        for inputList, expectedList in test_cases:
            with self.subTest(inputList=inputList, expectedList=expectedList):
                print("Input")
                print(inputList)

                result = solution.getConcatenation(inputList)

                print("Expected")
                print(expectedList)

                print("Result")
                print(result)
                self.assertEqual(result, expectedList)

    @parameterized.expand([
                                   [[1,2,1], [1,2,1,1,2,1]]
    ])
    def test_parameterized(self, inputList, expectedList):
        print(inputList)
        print(expectedList)

        solution = Solution()
        result = solution.getConcatenation(inputList)

        self.assertEqual(result, expectedList)



if __name__ == '__main__':
    unittest.main()
