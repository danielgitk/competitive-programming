class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksD = Counter(tasks)
        maxi = max(tasksD.values())
        
        result = (maxi - 1) * (n + 1)
        for count in tasksD.values():
            if count == maxi:
                result += 1
        return max(result,len(tasks))