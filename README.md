
# AI-Chat-Assistant 


Meet the AI Chat Assistant – your go-to Discord chat bot! 😎 Tired of handling user questions in your server? This bot has got you covered. 🤖 It provides community details and helpful commands to tackle common Discord issues. Plus, stay in the loop with event updates from Twitter every three hours. 📅 Discord management made easy! 🚀

# Demo
How the tool works:

![Aichatassistant-ezgif com-video-to-gif-converter (2)](https://github.com/Asinsayedali/AI-ChatAssistant/assets/85584914/b8d12b08-15ef-4aa1-8de7-0e813c802f66)


# How to Use the Tool
## Prerequisites:
1. Install [Python](https://www.python.org/downloads/) 3.10 or above on your machine.
2. Install [Pip](https://pip.pypa.io/en/stable/installation/).
3. Obtain an OpenAI API key:
   - Log in to the [OpenAI](https://openai.com/) website.
   - Go to the "API keys" section.
   - Generate your API key.
4. (Optional) Obtain a Twitter bearer key:
   - Go to the [Twitter Developer Platform](https://developer.twitter.com/en).
   - Create a developer account and create a Twitter App.
   - Obtain the bearer key from the App's Keys and Tokens section.
5. Now, follow the steps below to install packages and run the app.
---
## There are two ways you can run this project
### I. Run using Docker:
1. Rename the `.env_example` file in the root directory of the project to `.env`. Replace the `OPENAI_API_TOKEN` configuration value with your key `{OPENAI_API_KEY}`. You can also edit max tokens and other options if you wish.


2. Run the `Communitydata.py` to get basic data about your community. You can also add more details according to your need by editing the file `/Data/Basic_community_details.txt`


3. (OPTIONAL) If you want to incorporate the latest updates from Twitter/X, you need to replace '<your_bearer_token>' with your `Bearer Key` obtained and '<Community_twitter_Id>' with your Twitter Id.  You can also modify the number of tweets available.


4. (OPTIONAL) Run the `Tweetsscrap.py` to fetch data from Twitter/X tweets; the tweets get updated every 3 hours.

5. From the project root folder, open your terminal and run `docker compose build`.



7. After the build is complete, run `docker compose up` to start the app.

8. Visit `localhost:8501` on your browser after docker containers are up.


### II. Alternative Method:

#### Step 1: Clone the repository:

```bash
git clone https://github.com/Asinsayedali/AI-ChatAssistant.git
```

 Navigate to the project folder:

 ```bash
cd AI-ChatAssistant
```

#### Step 2: Set environment variables

Rename the `.env_example` file in the root directory of the project to `.env`. Replace the `OPENAI_API_TOKEN` configuration value with your key `{OPENAI_API_KEY}`.You can also edit max tokens and other options if you wish.

#### Step 3: Install the app dependencies

Install the required packages to run the app:

```bash
pip install --upgrade -r requirements.txt
```

#### Step 4: Run the Communitydata.py

```bash
python Communitydata.py
```

Enter the Data according to questions asked. You can also add more details according to your need by editing the file `/Data/Basic_community_details.txt`

#### (OPTIONAL) Step 5: Run the Tweetsscrap.py

Before running the script ensure to replace '<your_bearer_token>' with your `Bearer Key` obtained and '<Community_twitter_Id>' with your Twitter Id. You can also modify the number of tweets available. The script is scheduled to run every 3 hours, fetching the most recent tweets from the platform.

```bash
python Tweetsscrap.py
```

#### Step 6: Run main.py

You can start the application by running `main.py`:

```bash
python main.py
```

#### Step 7: Run Streamlit UI

You can run the UI by running Streamlit app:
```bash
streamlit run ui.py
```
It connects to the Pathway's backend API automatically and you will see the UI running on your browser at `localhost:8501`.

NOTE:
- To retrieve tweet data from the Twitter API, please note that, due to recent policy updates, access to tweets data now requires a Basic plan subscription. The free plan no longer provides the capability to fetch tweets data. Consider upgrading to the Basic plan for uninterrupted access to this feature.
  
- Include only essential and relevant data in the app; unnecessary information should be omitted.




