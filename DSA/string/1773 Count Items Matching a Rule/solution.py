from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], rule_key: str, rule_value: str) -> int:
        listCountItems = []
        for item in items:
            obj = CountItem(item[0], item[1], item[2])
            listCountItems.append(obj)

        return self.countByValue(listCountItems, rule_key, rule_value)

    @staticmethod
    def countByValue(listCountItems: List['CountItem'], rule_key: str, rule_value: str) -> int:
        count = 0
        if rule_key == 'type':
            for item in listCountItems:
                if item.typeName == rule_value:
                    count += 1

        elif rule_key == 'color':
            for item in listCountItems:
                if item.color == rule_value:
                    count += 1

        else:
            for item in listCountItems:
                if item.name == rule_value:
                    count += 1

        return count


class CountItem:
    def __init__(self, typeName, color, name):
        self.typeName = typeName
        self.color = color
        self.name = name


if __name__ == '__main__':
    itemList = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"

    sol = Solution()
    print(sol.countMatches(itemList, ruleKey, ruleValue))

    itemList = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"

    sol = Solution()
    print(sol.countMatches(itemList, ruleKey, ruleValue))
