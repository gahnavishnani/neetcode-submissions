class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        curr_sum = 0
        min_length = float('inf')
        for high in range(len(nums)):
            curr_sum += nums[high]
            while curr_sum >= target:
                min_length = min(min_length, high - low + 1)
                curr_sum -= nums[low]
                low += 1
        if min_length == float('inf'):
                return 0

        return min_length


        