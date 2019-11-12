# Sentiment Analysis using Kafka

This task helps to find the sentiment of a particular word.<br> 
It retrieves the tweets though a Kafka pipeline to retrieve tweets and on the spot calculates the Sentiment Score using AFINN. The Sentiment Score along with the tweet is then sent to a SQL table maintained by Pyspark SQL. <br>
The table helps to calculate the average of the scores which is being stored and gives us the result as Positive, Negative or Neutral based on the score. 


## Instructions 

Install Zookeeper and Kafka and make sure the path for JAVA_HOME is set as jre e.g. D:\Program Files\Java\jdk\jre
https://youtu.be/OJKesEpO6ok	

(in the video, set any path name inside the files with ‘\\’ e.g. D:\\kafka\\data)

After the installation, head over to kafka folder from cmd and execute this command

	.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties


Open up a new cmd and cd into kafka again and execute:

	.\bin\windows\kafka-server-start.bat .\config\server.properties

Place the 3 python files into spark installation folder to avoid any permission issues.
Open up cmd in admin, and cd into spark installation folder, and execute:

	spark-submit tweet_listener.py <ANY WORD>

Preferably without any delay, open up another cmd in admin, and cd into spark installation folder and execute:

	spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4 twitter_topic_avg_sentiment_val.py


