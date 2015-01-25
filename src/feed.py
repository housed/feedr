class Feed:
    def __init__(self, name, url, media, hashtag):
        self.name = name
        self.url = url
        self.media = media
        self.hashtag = hashtag

    def display_feed(self):
        print " Name    : ", self.name, "\n URL     : ", self.url, "\n Media   : ", self.media, "\n Hashtag : ", self.hashtag, "\n"

    def get_url(self):
        return self.url

    def get_media(self):
        return self.media

    def get_hashtag(self):
        return self.hashtag
