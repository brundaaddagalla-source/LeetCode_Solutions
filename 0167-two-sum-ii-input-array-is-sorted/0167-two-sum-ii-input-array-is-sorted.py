class Solution:
    def twoSum(self, a: list[int], target: int) -> list[int]:
        i=0
        j=len(a)-1
        while i<=j:
            if a[i]+a[j]<target:
                i+=1
            elif a[i]+a[j]>target:
                j-=1
            else:
                return [i+1,j+1]
        return []