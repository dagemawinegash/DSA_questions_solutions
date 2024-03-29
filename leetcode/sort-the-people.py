class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        #using insertion sort
        for i in range(1, len(heights)):
            j = i
            while j > 0 and heights[j-1] < heights[j]:
                heights[j-1], heights[j] = heights[j], heights[j-1]
                names[j-1], names[j] = names[j], names[j-1]
                j -= 1
        return names