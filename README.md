# feedr: RSS Bot for Twitter!

feedr will read RSS feed(s) that you specify and then it will determine if there's new content since last checked. If there is, then it will publish a post on your Twitter account on your behalf for each new content update.

As is, feedr will add the following information to a tweet:
* Title of the new content entry
* URL to the new content entry
* Relevant hashtag(s)
* Relevant image

Here's [an example of feedr in action](https://twitter.com/ValveTime/status/552918907053674496)...

![Feedr tweet example](https://raw.githubusercontent.com/housed/feedr/master/doc/img/example_tweet.png)

## Required Packages ##

* [Python 2.7](https://www.python.org/downloads/)
* [Tweepy 3.1.0](http://www.tweepy.org/)
* [feedparser 5.1.3](https://pypi.python.org/pypi/feedparser)

## Getting Started is Easy ##

You need to setup a [Twitter App](https://apps.twitter.com/) with your desired Twitter account. You must enable **Read and Write** permissions. Then generate your **Consumer and Access keys**, and add them to their respective variables in [**src/feedr.py**](https://github.com/housed/feedr/blob/master/src/feedr.py#L19). 

Next, you can specify your feeds by editing the **feedr.py** file. At the top of said file, there's a list structure called **FEEDS** that will store all of your RSS feeds. Add your feed while following the format [in the example](https://github.com/housed/feedr/blob/master/src/feedr.py#L10).

The image is not some outside resource. It's something that you have to create. To fit perfectly in Twitter's viewing window, it's recommended that an image be at least **520 x 210** in dimension. And, by default, images need to go into the **media folder**. *If you don't want images in your tweets, then you can easily change & remove a few lines of code in bot.py.*

One more thing... Before going live, first run **feedr.py** with **api.update_with_media()** *commented-out*. If you don't, then you're likely to flood your Twitter feed because your **database/rss_entries.db** is empty. After that, go ahead and run feedr.py as normal. Maybe setup a cronjob so that it runs periodically.

Follow me on Twitter [@TheDylanHouse](twitter.com/TheDylanHouse).
