class Solution:
    def isValid(self, s: str) -> bool:
        # stack 선언
        stack = []
        # 한글자씩 stack에 push
        if len(s)%2 != 0:
            return False
        for ch in s:
            if ch == "(":
                stack.append(")")
            elif ch == "{":
                stack.append("}")
            elif ch == "[":
                stack.append("]")
            elif not stack or stack.pop() != ch:
                return False
        return not stack

sol = Solution()

input = "{()[]}"
print(sol.isValid(s=input))