class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hashmap = {} # char -> last_index
        for i,c in enumerate(s):
            hashmap[c] = i
        arr = []
        end,size = 0,0
        for i,c in enumerate(s):
            size+=1
            end = max(end, hashmap[c])
            if i == end:
                arr.append(size)
                size = 0
        return arr


        