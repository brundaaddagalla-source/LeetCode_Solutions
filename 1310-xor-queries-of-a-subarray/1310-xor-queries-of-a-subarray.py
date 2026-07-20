class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        r=[]
        # for i in queries:
        #     a=arr[i[0]]
        #     for j in range(i[0]+1, i[1]+1):
        #         a=a^arr[j]
        #     r.append(a)
        # return r
        prefix=[0]
        for i in arr:
            prefix.append(prefix[-1]^i) 
        for i in queries:
            r.append(prefix[i[0]]^prefix[i[1]+1])
        return r
