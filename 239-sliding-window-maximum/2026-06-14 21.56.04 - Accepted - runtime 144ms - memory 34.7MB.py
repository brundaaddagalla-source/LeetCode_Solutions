from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l=[]
        # for i in range(len(nums)-k+1):
        #     s=nums[i:i+k]
        #     l.append(max(s))
        # return l
        n=len(nums)
        dq=deque()
        r=[]
        for i in range(k):
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
        r.append(nums[dq[0]])
        for i in range(k,n):
            if dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            r.append(nums[dq[0]])
        return r

#https://youtu.be/WcTMo1SHV_s?si=2LWCq2MVxGB14Gc1
        