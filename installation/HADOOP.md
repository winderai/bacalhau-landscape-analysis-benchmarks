# Hadoop 3.3.1 (Multi-node)

This page contains step-by-step instructions to install Hadoop on a multi-node cluster.
At the end of the process you'll be able to access relevant binaries by using `$HADOOP_HOME`, for example `$HADOOP_HOME/bin/hdfs`.


### Install requirements (all)

```bash
sudo apt -y update
sudo apt install -y ssh pdsh
sudo apt install -y openjdk-8-jdk-headless
sudo apt install -y openjdk-8-jre-headless

echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/' | tee -a ~/.bashrc
source ~/.bashrc
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

### Configure SSH (all)

```bash
ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

### Download Hadoop (all)

```bash
cd ~
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz &>/dev/null
mv hadoop-3.3.1 hadoop
sudo mv hadoop /usr/local/hadoop
```


### Pass JAVA_HOME to Hadoop variables (all)

```bash
echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/' >>  /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```

### Append Hadoop binaries to PATH (all)

```bash
echo 'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"' | sudo tee /etc/environment
```


### Modify host name (master)

```bash
echo 'hadoop-master' | sudo tee /etc/hostname
```

### Modify host name (slaves)

```bash
echo 'hadoop-slave1' | sudo tee /etc/hostname
```

:warning: Run the command above on each slave node, make sure you replace the node numbering accordingly (e.g., 1st slave is `hadoop-slave1`, 2nd is `hadoop-slave2`, etc.).

### Reboot all hosts (all)

```bash
sudo reboot
```

### Add cluster nodes to host file (all)

```bash
echo '<MASTER_IP>      hadoop-master
<1st_SLAVE_IP>   hadoop-slave1
<2nd_SLAVE_IP>   hadoop-slave2' | sudo tee /etc/hosts
```

Use `Private IPv4 addresses` from the AWS console.

:warning: Add an entry for each slave node in your cluster.

### Configure Hadoop user (all)

```bash
sudo adduser hadoopuser # !IMPORTANT: don't leave the password blank, you'll need it later on.
sudo usermod -aG hadoopuser hadoopuser
sudo chown hadoopuser:root -R /usr/local/hadoop/
sudo chmod g+rwx -R /usr/local/hadoop/
sudo adduser hadoopuser sudo
```

### Create an SSH key (all)

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

### Copy SSH key to all hosts (all)

```bash
ssh-copy-id hadoopuser@hadoop-master
ssh-copy-id hadoopuser@hadoop-slave1
ssh-copy-id hadoopuser@hadoop-slave2
...
```

:warning: Copy the key to each slave node in your cluster.

### Configure NameNode location (master)


```bash
echo '<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
   <property>
      <name>fs.defaultFS</name>
      <value>hdfs://hadoop-master:9000</value>
   </property>
</configuration>' | sudo tee /usr/local/hadoop/etc/hadoop/core-site.xml
```

### Configure settings for HDFS daemons (master)

```bash
echo '<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
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
</configuration>' | sudo tee /usr/local/hadoop/etc/hadoop/hdfs-site.xml
```

### Configure mapred-site.xml (master)

```bash
echo '<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
   <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
   </property>
   <property>
      <name>mapreduce.application.classpath</name>
      <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*,$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*,$HADOOP_MAPRED_HOME/share/hadoop/common/*,$HADOOP_MAPRED_HOME/share/hadoop/common/lib/*,$HADOOP_MAPRED_HOME/share/hadoop/yarn/*,$HADOOP_MAPRED_HOME/share/hadoop/yarn/lib/*,$HADOOP_MAPRED_HOME/share/hadoop/hdfs/*,$HADOOP_MAPRED_HOME/share/hadoop/hdfs/lib/*</value>
   </property>
   <property>
      <name>yarn.app.mapreduce.am.env</name>
      <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
   </property>
   <property>
      <name>mapreduce.map.env</name>
      <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
   </property>
   <property>
      <name>mapreduce.reduce.env</name>
      <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
   </property>
</configuration>' | sudo tee /usr/local/hadoop/etc/hadoop/mapred-site.xml
```

### Configure YARN (master)

```bash
echo '<?xml version="1.0"?>
<configuration>
   <property>
      <name>yarn.resourcemanager.hostname</name>
      <value>hadoop-master</value>
   </property>
   <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
   </property>
   <property>
      <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
      <value>org.apache.hadoop.mapred.ShuffleHandler</value>
   </property>
</configuration>' | sudo tee /usr/local/hadoop/etc/hadoop/yarn-site.xml
```

### Configure worker list (master)

```bash
echo 'hadoop-slave1
hadoop-slave2' | sudo tee /usr/local/hadoop/etc/hadoop/workers
```

:warning: Add an entry for each slave node in your cluster.

### Distribute Hadoop master configuration to slaves (master)

```bash
scp /usr/local/hadoop/etc/hadoop/* hadoop-slave1:/usr/local/hadoop/etc/hadoop/
scp /usr/local/hadoop/etc/hadoop/* hadoop-slave2:/usr/local/hadoop/etc/hadoop/
...
```

:warning: Repeat the last command for each slave you spun up.


### Set environment variables (all)

```bash
su - hadoopuser

echo 'export HADOOP_HOME="/usr/local/hadoop"' >> ~/.bashrc
echo 'export HADOOP_COMMON_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop' >> ~ ~/.bashrc
echo 'export HADOOP_HDFS_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_MAPRED_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_YARN_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export PDSH_RCMD_TYPE=ssh' | tee -a ~/.bashrc

source ~/.bashrc
```

### Format HDFS (master)

```bash
source /etc/environment
$HADOOP_HOME/bin/hdfs namenode -format
```

Reminder: make sure you're impersonating `hadoopuser`.

### Start HDFS (master)

```bash
$HADOOP_HOME/sbin/start-dfs.sh
```

If you run into `rcmd: socket: Permission denied` error:

- Make sure you've copied each node's SSH key to all other nodes (see step above with `ssh-copy-id`)
- Run `export PDSH_RCMD_TYPE=ssh` on each node.

<!-- :warning: Now, run `jps` and check if its output includes `SecondaryNameNode` and `DataNode`. If the latter is not on the list: 

1. Open a separate terminal
1. Ssh into master
1. Impersonate `hadoopuser`
1. `source /etc/environment`
1. Run `$HADOOP_HOME/bin/hdfs datanode` -->

<!-- ### Start HDFS (slave)

```bash
$HADOOP_HOME/sbin/start-dfs.sh
jps
```

Note: in case of `Permission denied` error run `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
` as described [here](https://stackoverflow.com/questions/48978480/hadoop-permission-denied-publickey-password-keyboard-interactive-warning/49960886). -->
    

### Launch YARN (master)

```bash
$HADOOP_HOME/sbin/start-yarn.sh
```

At this point you can use `jps` to double check the right JVM processes are running, on master:

```bash
hadoopuser@hadoop-master:~$ jps
1765 NameNode
2487 Jps
2012 SecondaryNameNode
2206 ResourceManager
```

On slave:

```bash
hadoopuser@hadoop-slave1:~$ jps
1986 Jps
1892 NodeManager
1711 DataNode
```

### That's all folks! 🎉

Just make sure you run hadoop jobs impersonating `hadoopuser`.

You can access the web UIs at:

- http://<MASTER_PUBLIC_IP>:9870/ # hdfs
- http://<MASTER_PUBLIC_IP>:8088/ # hadoop nodes & jobs

Use `Public IPv4 address` from the AWS console.

---

## Optional: Test Hadoop installation (master)

```bash
git clone https://github.com/enricorotundo/hadoop-examples-mapreduce
cd hadoop-examples-mapreduce
sudo apt install -y maven
mvn install -DskipTests
wget https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/trees.csv

# Tiny dataset
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hadoopuser
$HADOOP_HOME/bin/hdfs dfs -put trees.csv
$HADOOP_HOME/bin/yarn jar ~/hadoop-examples-mapreduce/target/hadoop-examples-mapreduce-1.0-SNAPSHOT-jar-with-dependencies.jar wordcount trees.csv count
$HADOOP_HOME/bin/hdfs dfs -cat count/part-r-00000

# 100MB dataset
sudo apt install unzip
wget https://www3.stats.govt.nz/2018census/Age-sex-by-ethnic-group-grouped-total-responses-census-usually-resident-population-counts-2006-2013-2018-Censuses-RC-TA-SA2-DHB.zip
unzip Age-sex-by-ethnic-group-grouped-total-responses-census-usually-resident-population-counts-2006-2013-2018-Censuses-RC-TA-SA2-DHB.zip
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hadoopuser
$HADOOP_HOME/bin/hdfs dfs -put Data8277.csv
$HADOOP_HOME/bin/yarn jar ~/hadoop-examples-mapreduce/target/hadoop-examples-mapreduce-1.0-SNAPSHOT-jar-with-dependencies.jar wordcount hdfs:///user/hadoopuser/Data8277.csv count
```
