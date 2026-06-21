class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        t=0
        for i in costs:
            t+=i
            if t>coins:
                return c
            c+=1
        return c