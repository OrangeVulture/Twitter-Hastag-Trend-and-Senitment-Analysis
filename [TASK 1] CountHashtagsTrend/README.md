# Count Hashtag Trends

This task involves in counting the hastags in a tweet related to a word. After every batch, the hastags are map-reduced and the count is found out. The Python Notebook has proper explanation to each line of code. 

## Instructions

### Using Python Notebook 

Install findspark from anaconda prompt

	conda install -c conda-forge findspark

Install tweepy 

	conda install -c conda-forge tweepy


Execute getStreamingTweets.ipynb first, then countHashTags.ipynb


### Using spark-submit

Install tweepy 

	pip install tweepy

From spark directory in cmd using spark-submit,
Open up cmd and change Directory to spark installation folder

Execute this and wait till Port shows up,

	spark-submit getTweetStream.py <ANY WORD>

On a different cmd window, cd into spark installation folder and execute,

	spark-submit hashtagTrend.py
