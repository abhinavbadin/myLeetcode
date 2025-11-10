class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set) #{user:{followers}}
        self.tweets = defaultdict(list) #{user:[(time,tweets)]}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        users = self.follow_map[userId] | {userId} #include self

        for u in users:
            for (t,tw) in self.tweets[u][-10:]:
                heapq.heappush(maxheap,(-t,tw))
        
        feed = []
        for _ in range(10):
            if maxheap:
                feeds = heapq.heappop(maxheap)
                feed.append(feeds[1])
        
        return feed
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower = followerId
        self.followee = followeeId
        
        self.follow_map[self.follower].add(self.followee)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower = followerId
        self.followee = followeeId
        
        if self.followee in self.follow_map[self.follower]:
            self.follow_map[self.follower].remove(self.followee)


        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)