class Twitter:

    def __init__(self):
        self.tweets = []  
        self.follows = {}      

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId,tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        followed = self.follows.get(userId, set())

        for author, tweetId in reversed(self.tweets):
            if author == userId or author in followed:
                feed.append(tweetId)
                if len(feed) == 10:
                    break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows.keys():
            self.follows[followerId].add(followeeId)
        else :
            self.follows[followerId] = set({followeeId})

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)            
