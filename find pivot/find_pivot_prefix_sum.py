class Solution(object):
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftSum=0
        for i in range(len(nums)):
            total-=nums[i]
            if total==leftSum:
                return i
            leftSum+=nums[i]
        return -1
