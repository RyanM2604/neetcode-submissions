class Twitter:

    def __init__(self):
        self.time = 0 # signifies time for maxheap
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.time])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetsArray = self.tweets[userId]
        heap = []
        res = []

        for tweetId, time in self.tweets[userId]:
            heapq.heappush(heap, [time, tweetId])

        for followeeId in self.followers[userId]:
            for tweetId, time in self.tweets[followeeId]:
                heapq.heappush(heap, [time, tweetId])
        
        for i in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
