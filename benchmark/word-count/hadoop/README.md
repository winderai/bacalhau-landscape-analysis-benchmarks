export PATH=${JAVA_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
export HADOOP_HOME=<YOUR_HADOOP_HOME>


# create JAR file
$HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main WordCount.java
jar cf wc.jar WordCount*.class

# launch job
$HADOOP_HOME/bin/hadoop jar wc.jar WordCount ./data ./out

# print wordcout output
$HADOOP_HOME/bin/hadoop fs -cat ./out/part-r-00000



