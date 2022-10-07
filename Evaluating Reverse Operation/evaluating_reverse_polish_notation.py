class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        size = len(tokens)
        result=0
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                r,l=stack.pop(),stack.pop()
                if i == "+":
                    stack.append(l+r)
                elif i == "-":
                    stack.append(l-r)
                elif i == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop()
