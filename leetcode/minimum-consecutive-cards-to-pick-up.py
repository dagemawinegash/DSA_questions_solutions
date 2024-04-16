from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        last_seen = defaultdict(int)
        min_consecutive = float('inf')

        for end, card in enumerate(cards):
            if card in last_seen:
                min_consecutive = min(min_consecutive, end - last_seen[card] + 1)
            last_seen[card] = end
        
        return min_consecutive if min_consecutive != float('inf') else -1