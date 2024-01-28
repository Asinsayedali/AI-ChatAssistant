import tweepy
import schedule
import time
import os

# Replace with your actual Twitter API credentials
bearer_token = '<your_bearer_token>'

# Target Twitter account screen name
target_screen_name = '<Community_twitter_Id>'

# Authenticate with Twitter API using bearer token
client = tweepy.Client(bearer_token=bearer_token)

# Function to fetch and save tweets
def fetch_and_save_tweets():
    try:
        # Use the appropriate v2 endpoint for user timeline
        tweets = client.get_users_tweets(id=target_screen_name, max_results=6)
        os.makedirs("Data", exist_ok=True)

        # Save tweets to a text file inside the "Data" directory
        file_path = os.path.join("Data", "Tweets_data.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            for tweet in tweets:
                file.write(f"{tweet.user.screen_name}: {tweet.text}\n")
    except Exception as e:  # Catch any general exception
        print(f"An error occurred: {e}")

fetch_and_save_tweets()

# Schedule the script to run every 3 hours
schedule.every(3).hours.do(fetch_and_save_tweets)

# Run the script continuously
while True:
    schedule.run_pending()
    time.sleep(1)
