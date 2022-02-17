export HADOOP_HOME="/Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/hadoop/hadoop-3.3.1"

export PATH=${JAVA_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar




$HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main HeadTxtFile.java && jar cf headfile.jar HeadTxtFile*.class && $HADOOP_HOME/bin/hadoop jar headfile.jar HeadTxtFile /Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/hadoop/test_data/file.txt $(echo $(mktemp -d -t ci-XXXXXXXXXX)/out)

$HADOOP_HOME/bin/hadoop fs -cat /Users/enricorotundo/winderresearch/ProtocolLabs/sample-code-benchmark/sample-code/derivative-dataset/hadoop/out/part-r-00000