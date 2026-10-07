class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def valid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        level = {s}

        while True:
            result = []

            for x in level:
                if valid(x):
                    result.append(x)

            if result:
                return result

            new_level = set()

            for x in level:
                for i in range(len(x)):
                    if x[i] == '(' or x[i] == ')':
                        new_level.add(x[:i] + x[i+1:])

            level = new_level