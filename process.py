import tweepy

#user application credentials
consumer_key="YWEorhFFtIsluvyhkBngEyxVD"
consumer_secret="sA1H4CIjYEchOdw1hVHyjWyjonpwdTi9wcNjbCpFvriZHzhjsH"

access_token="709775213-JMsM39wQImVihbdyWE0qNcdVPadaAsHyhH1KHRfF"
access_token_secret="8skFfSjx7nPNmtpQWLwxXAS7XLsct7iqavX4v0v5ZveVb"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

    def on_status(self, status):
        print status.text , "\n"

    #handle errors without closing stream:
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True 

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True 

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=['dog'])

