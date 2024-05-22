class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def diff(start: int, end: int) -> int:
            if start == end:
                return nums[start]
            
            choose_start = nums[start] - diff(start + 1, end)
            choose_end = nums[end] - diff(start, end - 1)
            
            return max(choose_start, choose_end)
        
        return diff(0, len(nums) - 1) >= 0