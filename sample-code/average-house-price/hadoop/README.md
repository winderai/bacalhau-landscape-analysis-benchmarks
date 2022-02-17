export HADOOP_HOME="/Users/enricorotundo/hadoop-3.3.1"
export PATH=${JAVA_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar



$HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main WordCount.java
jar cf wc.jar WordCount*.class


$HADOOP_HOME/bin/hadoop jar wc.jar WordCount /Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/data /Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/hadoop/out



javac -classpath "$($HADOOP_HOME/bin/yarn classpath)" -d . AvgPrice.java
jar -cvf AvgPrice.jar -C . .
$HADOOP_HOME/bin/hadoop jar AvgPrice.jar AvgPrice
$HADOOP_HOME/bin/hadoop fs -cat average_prices/part-r-00000