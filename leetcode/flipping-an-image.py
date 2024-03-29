class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])
        ans = []
        for x in image:
            arr = x.reverse()
            inverted_row = []
            for value in x:
                if value == 0:
                    inverted_row.append(1)
                else:
                    inverted_row.append(0)
            ans.append(inverted_row)
        return ans