class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        jumps = 0
        bricks = bricks
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                if len(heap) < ladders:
                    heapq.heappush(heap,diff)
                    # jumps += 1
                elif ladders and diff > heap[0]:
                    val = heapq.heapreplace(heap, diff)
                    bricks -= val
                else:
                    bricks -= diff
                    # jumps += 1           
            if bricks < 0:
                break
            jumps += 1
        return jumps