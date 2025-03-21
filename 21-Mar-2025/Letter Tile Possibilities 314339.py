# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def helper(perms):
            nonlocal ans
            if perms:
                ans += 1
            
            for i in range(n):
                if checked[i]:
                    continue
                
                if i > 0 and tiles[i] == tiles[i - 1] and not checked[i - 1]:
                    continue
                
                # choose the current character
                checked[i] = True
                perms.append(tiles[i])
                helper(perms)
                # backtrack to the previous decision point
                checked[i] = False
                perms.pop()
        
        ans = 0
        n = len(tiles)
        tiles = sorted(tiles)
        checked = [False] * n
        helper([])
        return ans




        

