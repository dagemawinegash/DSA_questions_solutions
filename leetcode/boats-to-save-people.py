class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boats = 0
        p1,p2 = 0,len(people)-1
        while p1<=p2:
            remain = limit - people[p2]
            p2-=1
            boats+=1
            if p1<=p2 and remain >= people[p1]:
                p1+=1   
        return boats
            