class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        closest=float("inf")
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            j,k=i+1, len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if abs(target-s)<abs(target-closest):
                    closest=s
                    # while j<k and nums[j]==nums[j+1]:
                    #     j+=1
                    # while k>j and nums[k]==nums[k-1]:
                    #     k-=1
                elif s<target:
                    j+=1
                elif s>target:
                    k-=1
                else:
                    return s
        return closest