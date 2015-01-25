#!/usr/bin/env python

from feed import Feed
import tweepy, feedparser, sqlite3, time

DATABASE = '../database/rss_entries.db' 

# Initialize the list of desired feeds
# Feed(Name, XML, Media, Hashtags)
FEEDS = [ Feed('TechCrunch', 'http://techcrunch.com/feed/', '../media/techcrunch.jpg', '#Technology #Business'),
          Feed('Rock, Paper, Shotgun', 'http://www.rockpapershotgun.com/feed/', '../media/rockpapershotgun.jpg', '#Gaming') ]

# Define the net max length of the text portion of a tweet
TWEET_MAX_LENGTH = 140
TWEET_URL_LENGTH = 22
TWEET_IMG_LENGTH = 23
TWEET_NET_LENGTH = TWEET_MAX_LENGTH - TWEET_URL_LENGTH - TWEET_IMG_LENGTH

# Twitter Account Keys 
CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
ACCESS_KEY = 'access_key'
ACCESS_SECRET = 'access_secret'

# Main Code Implementation
def init_twitter():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api

def post_tweet(api):
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS RSSContent (`url`, `title`, `dateAdded`)')

	for feed in FEEDS:
		parsed_feed = feedparser.parse(feed.get_url())

		for entry in parsed_feed.entries:
			c.execute('SELECT * FROM RSSContent WHERE url=?', (entry.link,))
			
			if not c.fetchall():
				data = (entry.link, entry.title, time.strftime("%Y-%m-%d %H:%M:%S", entry.updated_parsed))
        			c.execute('INSERT INTO RSSContent (`url`, `title`, `dateAdded`) VALUES (?,?,?)', data)

                		hashtag_length = len(feed.get_hashtag())                		
				body_length = TWEET_NET_LENGTH - hashtag_length

                		tweet_body = entry.title.encode('utf-8')[:body_length - 2] # Minus 2 to take into account the 2 spaces in the tweet format "%s %s %s"
				tweet_url = entry.link.encode('utf-8')
		                tweet_hashtag = feed.get_hashtag()

                		tweet_text = "%s %s %s" % (tweet_body, tweet_url, tweet_hashtag)
                		tweet_media = feed.get_media()

				api.update_with_media(tweet_media, tweet_text)
                		print " ", time.strftime("%c"), "-", tweet_text

	conn.commit()
	conn.close()

if __name__ == '__main__':
	api = init_twitter()	
	post_tweet(api)
