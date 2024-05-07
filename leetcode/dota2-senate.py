from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        arr = list(senate)
        R_queue = deque()
        D_queue = deque()

        for i in range(len(arr)):
            if arr[i] == "R":
                R_queue.append(i)
            else:
                D_queue.append(i)
        
        while R_queue and D_queue:
            R_chance = R_queue.popleft()
            D_chance = D_queue.popleft()

            if R_chance < D_chance:
                R_queue.append(R_chance + len(arr))
            else:
                D_queue.append(D_chance + len(arr))
        
        return "Dire" if D_queue else "Radiant"