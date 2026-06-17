class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        min_heap=[]
        for i in d:
            heapq.heappush(min_heap, (d[i],i))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [j for i,j in min_heap]