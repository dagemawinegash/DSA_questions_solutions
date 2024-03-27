class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        win_dict = {}
        lose_dict = {}
        ans1 = []
        ans2 = []
        for win,lose in matches:
            lose_dict[lose] = lose_dict.get(lose,0) + 1
        for arr in matches:
            if arr[0] not in lose_dict and arr[0] not in ans1:
                ans1.append(arr[0])
        for key, value in lose_dict.items():
            if value == 1:
                ans2.append(key)
        ans1.sort()
        ans2.sort()
        return [ans1,ans2]
        

        