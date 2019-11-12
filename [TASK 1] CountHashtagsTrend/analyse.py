from __future__ import print_function

# import findspark
# findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext(appName = "Joseph's Testing")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc,4)

socket_stream = ssc.socketTextStream("127.0.0.1",7918)	

lines = socket_stream.window(60)

hashtags = lines.flatMap(lambda text: text.split(" ")).filter(lambda word: word.lower().startswith("#")).map(lambda word: (word.lower(),1)).reduceByKey(lambda a,b:a+b)

author_counts_sorted_dstream = hashtags.transform(lambda foo: foo.sortBy(lambda x:x[0].lower()).sortBy(lambda x:x[1],ascending=False))

author_counts_sorted_dstream.pprint()




ssc.start()

ssc.awaitTermination()