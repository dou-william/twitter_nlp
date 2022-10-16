import tweepy
import configparser
import pandas as pd

def get_tweets(keywords,limit,api):
    tweets = tweepy.Cursor(api.search_tweets,
                           q=keywords,
                           count=100,
                           tweet_mode='extended').items(limit)
    return tweets
def main():
    # read configs
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Set key variables
    api_key = config['twitter']['api_key']
    api_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    # Create authentication
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Api instance
    api = tweepy.API(auth)

    # Executing Each Call
    call_1 = get_tweets("Covid",300,api)
    call_2 = get_tweets("Long Covid",300,api)

    # dataframe creation
    columns = ['User', 'Tweet']
    data = []
    data_2 = []
    for tweet in call_1:
        data.append([tweet.user.screen_name, tweet.full_text])
    for tweet in call_2:
        data_2.append([tweet.user.screen_name, tweet.full_text])
    df = pd.DataFrame(data, columns=columns)
    df_2 = pd.DataFrame(data_2, columns=columns)

    # Inspect the dataframe
    print(df)
    print(df_2)

    # Output data
    df.to_csv('Twitter_info.csv')
    df_2.to_csv('Twitter_info_2.csv')

# Run
if __name__ == "__main__":
    main()

