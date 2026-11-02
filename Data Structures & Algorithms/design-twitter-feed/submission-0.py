import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.followers = defaultdict(set)   # followerId -> set of followeeIds
        self.tweets = defaultdict(list)     # userId -> list of [count, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # include the user’s own tweets + their followees’ tweets
        users = self.followers[userId] | {userId}

        for uid in users:
            for tweet in self.tweets[uid]:
                heapq.heappush(heap, tweet)

        # get up to 10 most recent tweets
        for i in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
