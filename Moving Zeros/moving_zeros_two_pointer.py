class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right_bound = len(nums) - 1

        while left < right_bound:
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                right_bound -= 1
            else:
                left += 1

        return nums
