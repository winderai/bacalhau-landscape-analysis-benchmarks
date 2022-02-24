

# Hadoop 3.3.1

## Single-node

```bash
sudo apt -y update
sudo apt install -y ssh pdsh
sudo apt install -y openjdk-8-jdk-headless
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

cd ~
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz &>/dev/null
export HADOOP_HOME="/home/ubuntu/hadoop-3.3.1"
```

Reference: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html

## Multi-node

- all: run command in all host machines
- master
- slave(s)

### Install requirements (all)

```bash
sudo apt -y update
sudo apt install -y ssh
sudo apt-get install -y pdsh
sudo apt install -y openjdk-8-jdk-headless
sudo apt install -y openjdk-8-jre-headless
```

### Set rcmd module to SSH (all)

```bash
vim .bashrc
```

Append: `export PDSH_RCMD_TYPE=ssh`

### Configure SSH (all)

```bash
ssh-keygen -t rsa -P ""

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```


### Check Java version (all)

```bash
java -version
```

Expected output:
```
openjdk version "1.8.0_312"
OpenJDK Runtime Environment (build 1.8.0_312-8u312-b07-0ubuntu1~20.04-b07)
OpenJDK 64-Bit Server VM (build 25.312-b07, mixed mode)
```

### Download Hadoop (all)

```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz
mv hadoop-3.3.1 hadoop
sudo mv hadoop /usr/local/hadoop
```


### Pass JAVA_HOME to Hadoop variables (all)

```bash
vim ~/hadoop/etc/hadoop/hadoop-env.sh
```

Append: `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/`


### Append Hadoon binaries (all)

```bash
sudo vim /etc/environment
```

Replace content with:

```bash
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"

JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"
```

### Configure Hadoop user (all)

```bash
sudo adduser hadoopuser
sudo usermod -aG hadoopuser hadoopuser
sudo chown hadoopuser:root -R /usr/local/hadoop/
sudo chmod g+rwx -R /usr/local/hadoop/
sudo adduser hadoopuser sudo
```

### Modify host name (master)

```bash
sudo vim /etc/hostname
```

Replace content with: `hadoop-master` 

### Modify host name (slaves)

```bash
sudo vim /etc/hostname
```

Replace content with: `hadoop-slave1`

### Add cluster nodes to host file (all)

```bash
sudo vim /etc/hosts
```

Add:

```
<MASTER_IP>   hadoop-master
<SLAVE_IP>   hadoop-slave1
```

Note: in case of a `ConnectionRefused` refused error, remove the `127.0.0.1    localhost` entry as suggested [here](https://cwiki.apache.org/confluence/display/HADOOP2/ConnectionRefused).

### Create an SSH key (master)

```bash
su - hadoopuser
ssh-keygen -t rsa
```

### Enable password auth in SSH (all)

```bash
sudo vim /etc/ssh/sshd_config
```

Change this line: `PasswordAuthentication no` to `PasswordAuthentication yes`

```bash
sudo systemctl restart sshd
```

### Copy SSH key to all hosts (master)

```bash
ssh-copy-id hadoopuser@hadoop-master
ssh-copy-id hadoopuser@hadoop-slave1
```


### Configure NameNode location (master)

```bash
sudo vim /usr/local/hadoop/etc/hadoop/core-site.xml
```

Add:

```xml
<configuration>
   <property>
      <name>fs.defaultFS</name>
      <value>hdfs://hadoop-master:9000</value>
   </property>
</configuration>
```

### Configure settings for HDFS daemons (master)

```bash
sudo vim /usr/local/hadoop/etc/hadoop/hdfs-site.xml
```

Add:

```xml
<configuration>
   <property>
      <name>dfs.namenode.name.dir</name>
      <value>/usr/local/hadoop/data/nameNode</value>
   </property>
   <property>
      <name>dfs.datanode.data.dir</name>
      <value>/usr/local/hadoop/data/dataNode</value>
   </property>
   <property>
      <name>dfs.replication</name>
      <value>2</value>
   </property>
</configuration>
```

### Configure worker list (master)

```bash
sudo vim /usr/local/hadoop/etc/hadoop/workers
```

Add: `hadoop-slave1`

### Distribute Hadoop master configuration to slaves (master)

```bash
scp /usr/local/hadoop/etc/hadoop/* hadoop-slave1:/usr/local/hadoop/etc/hadoop/
```

### Format HDFS (master)

```bash
source /etc/environment
hdfs namenode -format
```

### Start HDFS (master)

```bash
start-dfs.sh
jps
```

If `jps` does not list a `DataNode`, run `hadoop datanode` in a separate terminal.

### Start HDFS (slave)

```bash
start-dfs.sh
jps
```

Note: in case of `Permission denied` error run `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
` as described [here](https://stackoverflow.com/questions/48978480/hadoop-permission-denied-publickey-password-keyboard-interactive-warning/49960886).
    

### Set environment variables (all)

```bash
export HADOOP_HOME="/usr/local/hadoop"
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
```

### Configure YARN (slave)

```bash
sudo vim /usr/local/hadoop/etc/hadoop/yarn-site.xml
```

Add:

```xml
<property>
   <name>yarn.resourcemanager.hostname</name>
   <value>hadoop-master</value>
</property>
```

### Launch YARN (master)

```bash
start-yarn.sh
```

### That's all! 🎉

Reference: https://medium.com/@jootorres_11979/how-to-set-up-a-hadoop-3-2-1-multi-node-cluster-on-ubuntu-18-04-2-nodes-567ca44a3b12


## Optional: Test Hadoop installation (master)

```bash
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