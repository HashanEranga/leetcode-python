from typing import List


class Solution:
    @staticmethod
    def countMatches(self, items: List[List[str]], rule_key: str, rule_value: str) -> int:
        c = 0
        if rule_key == "type":
            for i in items:
                if i[0] == rule_value:
                    c += 1

        elif rule_key == "color":
            for i in items:
                if i[1] == rule_value:
                    c += 1

        elif rule_key == "name":
            for i in items:
                if i[2] == rule_value:
                    c += 1

        return c
