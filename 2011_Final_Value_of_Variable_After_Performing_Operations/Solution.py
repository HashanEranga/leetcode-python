import unittest
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for operation in operations:
            if operation == 'X--' or operation == '--X':
                count -=1
            elif operation == 'X++' or operation == '++X':
                count +=1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_finalValueAfterOperations_enterOperationSet_returnFinalValue(self):
        # Arrange
        operations = ['X--', 'X++']
        expectedAns = 0

        # Act
        ans = self.solution.finalValueAfterOperations(operations)

        # Assert
        self.assertEqual(ans, expectedAns)

if __name__ == '__main__':
    unittest.main()
