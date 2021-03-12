class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicti = {}
        heap = []
        for num in words:
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