class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        # Bubble Sort
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        answer = (nums[-1] - 1) * (nums[-2] - 1)
        
        return answer