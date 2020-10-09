import json
import tweepy

class TwitterAPI:

    def __init__(self, consumer_key, consumer_secret):
        self.credentials = {}
        self.credentials['CONSUMER_KEY'] = consumer_key
        self.credentials['CONSUMER_SECRET'] = consumer_secret
        self.credentials['ACCESS_TOKEN'] = '2497057112-o5ZWfhpVTJxv6E8jWjxsfSsiVTRdklU48DcN4Nc'
        self.credentials['ACCESS_SECRET'] = 'mk4ezKoGkl5WLrKUT5AqcGBGPBmFXF9S7uOGFziNR6C2P'

        self.api = tweepy.API(self.authenticate_to_twitter(),
                              wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)
        self.verify_credentials()

    def create_credential_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.credentials, file)
        print("File created")

    def authenticate_to_twitter(self):
        auth = tweepy.OAuthHandler(self.credentials['CONSUMER_KEY'], self.credentials['CONSUMER_SECRET'])
        auth.set_access_token(self.credentials['ACCESS_TOKEN'], self.credentials['ACCESS_SECRET'])
        return auth

    def verify_credentials(self):
        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

