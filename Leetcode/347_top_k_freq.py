import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        ditn = {}
        pq = []
        for i in nums :
            ditn[i] = ditn.get(i, 0) + 1

        for key , val in ditn.items() :
            heapq.heappush(pq,(-val,key))

        while k > 0 :
            res.append(heapq.heappop(pq)[1])
            k -= 1
        
        return res
        