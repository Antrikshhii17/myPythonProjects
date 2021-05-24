import tweepy
# from time import sleep
import csv

# Twitter API setup from Twitter Developer Portal. App name- data_source1
consumer_api_key = 'hMFTnumHTmgKKsumXHnSfQA6L'
consumer_secret = 'sg6pKoBHrX65wyKaXQcc****7vJzzcv6CAdTb6kNeBy'
access_token = '2255488675-G1OrKxps5trlXFnBcpUH0xSVtUrMp0hWfXWZnb1'
access_token_secret = '7jiqB7XqreMLAJCciuyEvHH****wQUJhRfOv8QmqThZZ'

# Creating authentication object
auth = tweepy.OAuthHandler(consumer_api_key, consumer_secret)
print('✎ Authenticating...')

# Setting up access token and secret key
auth.set_access_token(access_token, access_token_secret)
print('✎ Setting up access...')

# Creating the API object
api = tweepy.API(auth)

# Creating a csv file to which extracted data will be written
csvFile = open('Twitter_data_extracted.csv', 'w')
csvWriter = csv.writer(csvFile, delimiter=',')
header1 = ['ID', 'CREATED_AT', 'LOCATION', 'FOLLOWERS_COUNT', 'SCREEN_NAME', 'TWEET']
print('...created a new csv file ✔')


def fetch_twitter_data():       # Function to get twitter data
    query = '#Chhattisgarh AND #Covid-19'    # Enter the keywords to search for
    language = 'en'
    count = 20
    result = api.search(q=query, lang=language, count=count)
    csvWriter.writerow(header1)
    for words in result:
        # res = str(words.id_str)       Uncomment if we wish to print the result on screen
        # res += '|'
        # res += str(words.created_at)
        # res += '|'
        # res += str(words.user.location)
        # res += '|'
        # res += str(words.user.followers_count)
        # res += '|'
        # res += str(words.user.screen_name)
        # res += '|'
        # res += str(words.text)
        # print(res)
        csvWriter.writerow([words.id_str, words.created_at, words.user.location.encode('utf-8'),
                            words.user.followers_count, words.user.screen_name.encode('utf-8'),
                            words.text.encode('utf-8')])


fetch_twitter_data()
print('Success!✅ ✦A new csv file has been created ✔')
# def delay(interval):            # Sleep function to avoid too many requests to the server
#     while True:
#         fetch_twitter_data()
#         sleep(interval)
# delay(60 * 5)                   # Using delay in minutes. Currently 5
