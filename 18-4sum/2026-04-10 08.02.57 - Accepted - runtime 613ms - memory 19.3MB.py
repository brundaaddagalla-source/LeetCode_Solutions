class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        r=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            for l in range(i+1,len(nums)):
                if l>i+1 and nums[l]==nums[l-1]:
                    continue
                j,k=l+1, len(nums)-1
                while j<k:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        r.append([nums[i],nums[l], nums[j], nums[k]])
                        while j<k and nums[j]==nums[j+1]:
                            j+=1
                        while k>j and nums[k]==nums[k-1]:
                            k-=1
                        j+=1
                        k-=1
                    elif nums[i]+nums[j]+nums[k]+nums[l]<target:
                        j+=1
                    else:
                        k-=1
        return r