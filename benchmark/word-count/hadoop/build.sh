#!/bin/bash

set -x

$HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main WordCount.java

jar cf wc.jar WordCount*.class

ls -la wc.jar