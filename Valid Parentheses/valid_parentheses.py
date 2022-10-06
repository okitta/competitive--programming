class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket={'(':')','[':']','{':'}'}
        for character in s:
            if character in bracket:
                stack.append(bracket[character])
            elif not stack or stack.pop() != character:
                return False
        return not stack
