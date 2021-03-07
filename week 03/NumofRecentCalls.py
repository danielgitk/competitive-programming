class RecentCounter:
    

    def __init__(self):
        self.queue = deque()
        self.window = 3000
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - self.queue[0] > self.window:
            self.queue.popleft()
        return len(self.queue)