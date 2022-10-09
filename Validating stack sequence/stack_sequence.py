class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        size = len(popped)
        i=0
        for n in pushed:
            stack.append(n)
            while stack and i<size and stack[-1] == popped[i]:
                i+=1
                stack.pop()
        return stack==[]
