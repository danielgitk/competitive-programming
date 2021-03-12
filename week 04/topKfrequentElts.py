class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = collections.Counter(nums)
#         print(count)
#         return [x for x, c in count.most_common()[:k]]
        
        dicti = {}
        heap = []
        for num in nums:
            if num in dicti:
                dicti[num] += 1
            else:
                dicti[num] = 1
        for x,y in dicti.items():
            heapq.heappush(heap,(-y,x))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer