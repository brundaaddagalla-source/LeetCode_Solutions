class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxi=c=nums[0]
        # for i in range(1,len(nums)):
        #     c=max(nums[i],c*nums[i])
        #     maxi=max(c,maxi)
        # return maxi
        cmax=nums[0]
        cmin=nums[0]
        ans=nums[0]

        for i in range(1, len(nums)):
            temp=cmax
            cmax=max(nums[i], nums[i]*cmax, nums[i]*cmin)
            cmin=min(nums[i], nums[i]*temp, nums[i]*cmin)
            ans=max(cmax, ans)
        return ans