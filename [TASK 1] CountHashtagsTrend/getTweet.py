import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

consumer_key = 'exFpGOeTIYfwIN2ZdHHfDzG2y'
consumer_secret = 'by0X5jyZXrawJn82uuGY9a8ymJ0YffezakJ9FhNO95GsxsTkdx'
access_token = '3317958877-KbuPexMO5vVVWa6EKsgh4fWkxP2K7CqRI4Fhrql'
access_secret = 'i5UGN5T4zePg1D7xfTRVLyFgPKAI6wD1k3eAaJUDcast9'

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
    word = 'Trump'                                              # word can be tweaked
    twitter_stream.filter(languages=['en'], track=[word])


s = socket.socket()                          # Create a Socket Object
host = "127.0.0.1"                           # Localhost IP
port = 7918                                  # Reserve a port
s.bind((host,port))                          # Bind to the port
print("Listening on port: %s" % str(port))

s.listen(5)                          # Wait for client connection
c, addr = s.accept()                 # Establish connection  with client
print("Recieved request from: ",str(addr))


sendData(c)



