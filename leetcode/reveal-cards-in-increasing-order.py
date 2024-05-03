from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        ans = [0] * len(deck)

        for num in deck:
            idx = queue.popleft()
            ans[idx] = num

            if queue:
                j = queue.popleft()
                queue.append(j)

        return ans
        