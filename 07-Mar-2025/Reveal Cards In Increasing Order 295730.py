# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [0] * n
        deck.sort()
        q = deque()
        for i in range(n):
            q.append(i)
        
        for num in deck:
            ans[q.popleft()] = num
            if q:
                i = q.popleft()
                q.append(i)
        return ans
        