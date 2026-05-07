from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)
        self.user_follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        
        following = self.user_follows[userId] | {userId}
        
        for fid in following:
            if self.user_tweets[fid]:
                index = len(self.user_tweets[fid]) - 1
                count, tweet_id = self.user_tweets[fid][index]
                heap.append((count, tweet_id, fid, index - 1))
        heapq.heapify(heap)
        
        while heap and len(res) < 10:
            count, tweet_id, fid, index = heapq.heappop(heap)
            res.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.user_tweets[fid][index]
                heapq.heappush(heap, (count, tweet_id, fid, index - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)