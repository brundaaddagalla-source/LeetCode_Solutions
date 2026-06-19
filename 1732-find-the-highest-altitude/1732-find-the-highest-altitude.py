class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=0
        r=0
        for i in gain:
            s+=i
            r=max(r,s)
        return r