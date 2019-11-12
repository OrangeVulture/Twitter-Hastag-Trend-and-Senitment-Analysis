import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import sys
import twitter_config

consumer_key = twitter_config.consumer_key
consumer_secret = twitter_config.consumer_secret
access_token = twitter_config.access_token
access_secret = twitter_config.access_secret

class TweetsListener(StreamListener):
    def __init__(self,csocket):
        self.client_socket = csocket
    def on_data(self,data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s " % str(e))
        return True
    
    
    def on_error(self,status):
        print(status)
        return True

def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_secret)
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    word = sys.argv[1]                                              # word can be tweaked
    twitter_stream.filter(track=[word])



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: spark-submit getTweetStream.py \"<YOUR WORD>\"", file=sys.stderr)
        exit(-1)    

        
    s = socket.socket()                          # Create a Socket Object
    host = "127.0.0.1"                           # Localhost IP
    port = 7911                                  # Reserve a port
    s.bind((host,port))                          # Bind to the port
    print("Listening on port: %s" % str(port))

    s.listen(5)                          # Wait for client connection
    c, addr = s.accept()                 # Establish connection  with client
    print("Recieved request from: ",str(addr))


    sendData(c)



