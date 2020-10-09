import json
import tweepy
import pandas as pd
import config

states = {  'AL': 'alabama',
            'AK': 'alaska',
            'AZ': 'arizona',
            'AR': 'arkansas',
            'CA': 'california',
            'CO': 'colorado',
            'CT': 'connecticut',
            'DE': 'delaware',
            'DC': 'district of columbia',
            'FL': 'florida',
            'GA': 'georgia',
            'HI': 'hawaii',
            'ID': 'idaho',
            'IL': 'illinois',
            'IN': 'indiana',
            'IA': 'iowa',
            'KS': 'kansas',
            'KY': 'kentucky',
            'LA': 'louisiana',
            'ME': 'maine',
            'MD': 'maryland',
            'MA': 'massachusetts',
            'MI': 'michigan',
            'MN': 'minnesota',
            'MS': 'mississippi',
            'MO': 'missouri',
            'MT': 'montana',
            'NE': 'nebraska',
            'NV': 'nevada',
            'NH': 'new hampshire',
            'NJ': 'new jersey',
            'NM': 'new mexico',
            'NY': 'new york',
            'NC': 'north carolina',
            'ND': 'north dakota',
            'OH': 'ohio',
            'OK': 'oklahoma',
            'OR': 'oregon',
            'PA': 'pennsylvania',
            'RI': 'rhode island',
            'SC': 'south carolina',
            'SD': 'south dakota',
            'TN': 'tennessee',
            'TX': 'texas',
            'UT': 'utah',
            'VT': 'vermont',
            'VA': 'virginia',
            'WA': 'washington',
            'WV': 'west virginia',
            'WI': 'wisconsin',
            'WY': 'wyoming'
           }


class TwitterAPI:

    def __init__(self):
        self.credentials = {}
        self.credentials['CONSUMER_KEY'] = config.consumer_key
        self.credentials['CONSUMER_SECRET'] = config.consumer_secret
        self.credentials['ACCESS_TOKEN'] = config.access_token
        self.credentials['ACCESS_SECRET'] = config.access_secret

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

    def retrieve_tweets(self, count):
        return tweepy.Cursor(self.api.search, q="mask", lang="en").items(count)

    def organize_tweets_by_state(self):
        tweets = self.retrieve_tweets(10)
        dataframe = self.create_dataframe(tweets)

    def create_dataframe(self, results):
        data = {'id': [tweet.id for tweet in results],
                'text': [tweet.text for tweet in results],
                'created_at': [tweet.created_at for tweet in results],
                'user_location': [tweet.user.location for tweet in results]}
        data = pd.DataFrame
