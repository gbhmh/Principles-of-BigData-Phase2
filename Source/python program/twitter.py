#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2219941182-hJEd5re1y7lbZmVlyZySZvVsJf88fP6um3SsC3r"
access_token_secret = "BntHym97rzCisKS3BFXqrBgQbgokklZEBcqHXixGJQtX8"
consumer_key = "187ztf3hxmT3Nm3YonFzcAvEB"
consumer_secret = "hTqPaSjNXw21GXmPCey6CZBCZRoO1EbTkbVO4zMv77kN8Ikq0P"



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        saveFile = open(r'twitdb1.json','a')
        saveFile.write(data)
        saveFile.close()
        

    def on_error(self, status):
        print (status)
		
 

if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Baseball', 'Cricket', 'Football', 'Tennis', 'Golf', 'WWE', 'Badminton', 'Tennis', 'Baseball', 'Hockey', 'Volleyball', 'Rugby', 'Athletics', 'Boxing', 'MotoGP ', 'Cycling', 'Swimming', 'Snooker', 'Gymnastics', 'Handball', 'Skiing', 'Hurling', 'Bowling', 'Lacrosse', 'Archery', 'Bocce', 'Broomball', 'Croquet', 'Diving', 'Fencing', 'Darts', 'Dodgeball', 'Fishing', 'Foosball', 'Kayaking', 'Kickball', 'Racquetball', 'Powerlifting', 'Shooting', 'Sailing', 'Rowing'])
