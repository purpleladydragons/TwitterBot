import random
import time
import twitter

#This is Mark Chitsky, the twitter fellow.

#Search for "I wish it was/were easier"
#Search for "I wish there was/were"

#OMG implement MAB with "#genius" and "#brilliant"


API = twitter.Api(consumer_key = "",
                   consumer_secret = "",
                   access_token_key = "",
                   access_token_secret = "")

def search(word):
    print "SEARCHING FOR: %s" % word
    results = API.GetSearch(word)
    if results:
        return random.choice(results)
    return None


def main():
    words = ['I wish it was easier','I wish it were easier', "#genius", "#brilliant"]
    for x in range(100):
        word = random.choice(words)
        post = search(word)
        print ""
        print post.text
        print ""
        time.sleep(3)
    print "I be sleepin for a tiddle"
    time.sleep(180)
    main()


def sixdegrees():
#pick one random person
#pick another
#find shortest path between the two through followers/following
    pass

if __name__ == '__main__':
    main()
