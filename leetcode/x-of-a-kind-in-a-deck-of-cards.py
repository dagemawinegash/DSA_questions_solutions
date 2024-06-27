from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        counter = Counter(deck)
        counts = list(counter.values())
        
        def gcd_of_list(arr):
            cur_gcd = arr[0]
            for count in arr[1:]:
                cur_gcd = gcd(cur_gcd, count)
                if cur_gcd == 1:
                    return 1
            return cur_gcd
        
        return gcd_of_list(counts) > 1