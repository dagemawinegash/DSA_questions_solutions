class Solution:
    def swap(self, arr, max_idx, i):
        arr[max_idx], arr[i] = arr[i], arr[max_idx]

    def heapify(self, arr, n, i):
        max_idx = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[max_idx]:
            max_idx = left
        if right < n and arr[right] > arr[max_idx]:
            max_idx = right

        if i != max_idx:
            self.swap(arr, max_idx, i)
            self.heapify(arr, n, max_idx)

    def buildHeap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n - 1, 0, -1):
            self.swap(arr, i, 0)
            self.heapify(arr, i, 0)
            
        

