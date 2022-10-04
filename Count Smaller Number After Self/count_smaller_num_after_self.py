class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size = len(nums)
        k=[0]*size
        for i in range(size):            
            for j in range(size):
                if nums[j]<nums[i]:
                    k[i]=k[i]+1
        return k
