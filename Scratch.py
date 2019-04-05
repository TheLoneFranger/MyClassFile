# class from tweepy module that allows us to listen to tweets
from tweepy.streaming import StreamListener

#
from tweepy import OAuthHandler

from tweepy import Stream

# create class that allows us to print tweets
class AuthAPI(OAuthHandler):

    def AuthFileRead(self, file):
        userfilestr = input("what is the name of your file: ")
        objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Project/HomeInventory.txt", "r")


class StdOutListener(StreamListener):

    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)
        return True

# create object from StdOutListener class

if __name__ == "__main__":

    listener = StdOutListener()
    auth = OAuthHandler()

