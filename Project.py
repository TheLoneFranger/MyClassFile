# class from tweepy module that allows us to listen to tweets
from tweepy.streaming import StreamListener

#
from tweepy import OAuthHandler


from tweepy import Stream


class TwittAccess():

    def AuthFileRead(self):
        listData = []
        # userfilestr = input("what is the name of your file: ")
        objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Project/twitter_cred.txt", "r")
        for line in objFile:
            strData = line.split(': ')
            listData.append(strData[1].strip())
        api_key = listData[0]
        api_secret = listData[1]
        access_tkn = listData[2]
        access_secret = listData[3]
        return api_key, api_secret, access_tkn, access_secret


class StdOutListener(StreamListener):

    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)
        return True

if __name__ == "__main__":

    access = TwittAccess()
    api_key = access.AuthFileRead()[0]
    api_secret = access.AuthFileRead()[1]
    access_tkn = access.AuthFileRead()[2]
    access_secret = access.AuthFileRead()[3]

    listener = StdOutListener()
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_tkn, access_secret)

    stream = Stream(auth, listener)

    stream.filter(track=["Donlad Trump", "Hillary Clinton", "Barack Obama"])