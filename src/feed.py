class Feed:
    def __init__(self, name, url, media_root, hashtag):
        self.name = name
        self.url = url
        self.media_root = media_root
        self.hashtag = hashtag

    def display_feed(self):
        print " Name    : ", self.name, "\n URL     : ", self.url, "\n Media   : ", self.media_root, "\n Hashtag : ", self.hashtag, "\n"

    def get_name(self):
    return self.name

    def get_name(self):
        return self.name
        
    def get_url(self):
        return self.url

    def get_media_root(self):
        return self.media_root

    def get_hashtag(self):
        return self.hashtag
