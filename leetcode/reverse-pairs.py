class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge(nums, s, mid, e):
            temp = []
            i = s
            j = mid + 1

            while i <= mid and j <= e:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= e:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[s + k] = temp[k]  

        def count_pairs(nums, left, mid, right):
            j = mid + 1
            cnt = 0
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += (j - (mid + 1))
            return cnt

        def mergeSort(nums, l, r):
            cnt = 0
            if l >= r:
                return 0
            mid = (l + r) // 2
            cnt += mergeSort(nums, l, mid)
            cnt += mergeSort(nums, mid + 1, r)
            cnt += count_pairs(nums, l, mid, r)
            merge(nums, l, mid, r)
            return cnt

        return mergeSort(nums, 0, len(nums) - 1)