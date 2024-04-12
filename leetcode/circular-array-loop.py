class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_index(current_index):
            return (current_index + nums[current_index]) % n

        for i in range(n):
            slow = i
            fast = next_index(i)
            while nums[i] * nums[fast] > 0 and nums[i] * nums[next_index(fast)] > 0:
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
                slow = next_index(slow)
                fast = next_index(next_index(fast))
                
        return False
