import unittest
from solution import Solution


class testCountMatches(unittest.TestCase):

    def test_countMatches_passingValidInput_returnResult(self):
        # Arrange
        test_data = [
            [[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color",
             "silver", 1],
            [[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type",
             "phone", 2]
        ]

        # Act
        sol = Solution()

        for i, data in enumerate(test_data):
            with self.subTest(case=i + 1):
                itemList, ruleKey, ruleValue, expectedValue = data
                result = sol.countMatches(itemList, ruleKey, ruleValue)

                # Assert
                self.assertEqual(expectedValue, result)


if __name__ == '__main__':
    unittest.main()
