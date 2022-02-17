# Hadoop word count


```
cd ~
git clone https://github.com/enricorotundo/hadoop-examples-mapreduce
cd hadoop-examples-mapreduce
sudo apt install -y maven
mvn install -DskipTests
wget https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/trees.csv


$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hadoopuser
$HADOOP_HOME/bin/hdfs dfs -put trees.csv
$HADOOP_HOME/bin/yarn jar ~/hadoop-examples-mapreduce/target/hadoop-examples-mapreduce-1.0-SNAPSHOT-jar-with-dependencies.jar wordcount trees.csv count
$HADOOP_HOME/bin/hdfs dfs -cat count/part-r-00000
```


Alternative wordcount:

https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html


```
export HADOOP_HOME="/Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/hadoop/hadoop-3.3.1"

export PATH=${JAVA_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar



$HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main WordCount.java
jar cf wc.jar WordCount*.class


$HADOOP_HOME/bin/hadoop jar wc.jar WordCount /Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/data /Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/hadoop/out



$HADOOP_HOME/bin/hadoop fs -cat /Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/hadoop/out/part-r-00000
```