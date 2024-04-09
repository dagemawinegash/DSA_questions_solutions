class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        ans = 0
        hashmap = {}
        start = 0
        
        for end in range(len(fruits)):
            fruit = fruits[end]
            hashmap[fruit] = hashmap.get(fruit, 0) + 1

            while len(hashmap) > 2:
                left_fruit = fruits[start]
                hashmap[left_fruit] -= 1
                if hashmap[left_fruit] == 0:
                    del hashmap[left_fruit]
                start += 1

            ans = max(ans, end - start + 1)
            
        return ans
