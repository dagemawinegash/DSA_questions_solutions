class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge(nums, low, mid, high):
            temp = []
            i = low
            j = mid + 1

            while i <= mid and j <= high:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= high:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[low + i] = temp[i]

        def count_pairs(nums, low, mid, high):
            right = mid + 1
            cnt = 0
            for i in range(low, mid + 1):
                while right <= high and nums[i] > 2 * nums[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt

        def mergeSort(nums, low, high):
            cnt = 0
            if low >= high:
                return 0
            mid = (low + high) // 2
            cnt += mergeSort(nums, low, mid)
            cnt += mergeSort(nums, mid + 1, high)
            cnt += count_pairs(nums, low, mid, high)
            merge(nums, low, mid, high)
            return cnt

        return mergeSort(nums, 0, len(nums) - 1)
