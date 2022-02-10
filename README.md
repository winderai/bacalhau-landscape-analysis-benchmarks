# sample-code-benchmark

# AWS
❯ aws --version
aws-cli/2.4.17 Python/3.8.8 Darwin/20.6.0 exe/x86_64 prompt/off


AWS_PROFILE=winder
AWS_REGION=eu-central-1
aws --profile $AWS_PROFILE --region $AWS_REGION ec2 describe-instances


aws ec2 create-security-group \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --group-name ProtocolLabsDEV \
    --description "ProtocolLabs dev security group" \
    --tag-specifications 'ResourceType=security-group,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'

aws ec2 authorize-security-group-ingress \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --group-name ProtocolLabsDEV \
    --protocol tcp \
    --port 0-65535 \
    --cidr 0.0.0.0/8 \
    --tag-specifications 'ResourceType=security-group-rule,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'

aws ec2 authorize-security-group-ingress \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --group-name ProtocolLabsDEV \
    --protocol tcp \
    --port 0-65535 \
    --cidr 0.0.0.0/0 \
    --tag-specifications 'ResourceType=security-group-rule,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'

aws ec2 run-instances \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --image-id ami-0d527b8c289b4af7f \
    --count 2 \
    --instance-type t2.xlarge \
    --key-name wr-enrico-aws-ec2 \
    --security-group-ids ProtocolLabsDEV \
    --block-device-mapping DeviceName=/dev/sda1,Ebs={VolumeSize=120} \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]' 'ResourceType=volume,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'


aws ec2 describe-instances \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --filters "Name=tag-value,Values=ProtocolLabs-dev" \
    --query "Reservations[*].Instances[*].PublicIpAddress" \
    --output text


ssh -i "~/.ssh/wr-enrico-aws-ec2.pem" ubuntu@3.127.170.62
ssh -i "~/.ssh/wr-enrico-aws-ec2.pem" ubuntu@3.70.193.251


# Hadoop 

https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html


sudo apt -y update
sudo apt install -y openjdk-8-jre-headless
sudo apt-get install -y pdsh

wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz
#cd hadoop-3.3.1/
mv hadoop-3.3.1 hadoop
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export HADOOP_HOME=/home/ubuntu/hadoop-3.3.1/

$HADOOP_HOME/bin/hadoop version


$HADOOP_HOME/bin/hdfs namenode -format dev1

$HADOOP_HOME/bin/hdfs --daemon start namenode

$HADOOP_HOME/bin/hdfs --daemon start datanode



$HADOOP_HOME/bin/yarn --daemon start resourcemanager

$HADOOP_HOME/bin/yarn --daemon start nodemanager

$HADOOP_HOME/bin/yarn --daemon start proxyserver
$HADOOP_HOME/bin/mapred --daemon start historyserver

## tes
mkdir input
cp etc/hadoop/*.xml input
$HADOOP_HOME/bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar grep input output 'dfs[a-z.]+'grep input output 'dfs[a-z.]+'
cat output/*

## check
http://3.71.187.47:9870/
http://3.71.187.47:8088/
3.71.187.47:19888
http://3.123.254.115:8088
3.123.254.115:19888


## shutdown

$HADOOP_HOME/bin/hdfs --daemon stop namenode
$HADOOP_HOME/bin/hdfs --daemon stop datanode
$HADOOP_HOME/bin/yarn --daemon stop resourcemanager
$HADOOP_HOME/bin/yarn --daemon stop nodemanager
$HADOOP_HOME/bin/yarn stop proxyserver

# Hadoop 2

https://medium.com/@jootorres_11979/how-to-set-up-a-hadoop-3-2-1-multi-node-cluster-on-ubuntu-18-04-2-nodes-567ca44a3b12

[all]
sudo apt -y update
sudo apt install -y ssh
sudo apt-get install -y pdsh
sudo apt install -y openjdk-8-jdk-headless
sudo apt install -y openjdk-8-jre-headless

4) [all]
vim .bashrc

export PDSH_RCMD_TYPE=ssh

5) [all]
ssh-keygen -t rsa -P ""

6) [all]
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

7) [all]
ssh localhost
exit

9) [all]
java -version

openjdk version "1.8.0_312"
OpenJDK Runtime Environment (build 1.8.0_312-8u312-b07-0ubuntu1~20.04-b07)
OpenJDK 64-Bit Server VM (build 25.312-b07, mixed mode)


10) [all]
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz

12) [all]
mv hadoop-3.3.1 hadoop

13) [all]
vim ~/hadoop/etc/hadoop/hadoop-env.sh

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

14) [all]
sudo mv hadoop /usr/local/hadoop

15) [all]
sudo vim /etc/environment

PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"

JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"


16) [all]
sudo adduser hadoopuser

17) [all]
sudo usermod -aG hadoopuser hadoopuser
sudo chown hadoopuser:root -R /usr/local/hadoop/
sudo chmod g+rwx -R /usr/local/hadoop/
sudo adduser hadoopuser sudo

18) [all]
sudo vim /etc/hosts

...remove 127.0.0.1...

3.127.170.62   hadoop-master
3.70.193.251   hadoop-slave1


20) [all]
sudo vim /etc/hostname

hadoop-master
hadoop-slave1

21) [master]
su - hadoopuser

22) [master]
ssh-keygen -t rsa

23) [all]
    Log in as root Edit ssh config: 
        sudo vim /etc/ssh/sshd_config 
        Change this line: PasswordAuthentication no to PasswordAuthentication yes 
        sudo systemctl restart sshd

22) [master]
ssh-copy-id hadoopuser@hadoop-master
ssh-copy-id hadoopuser@hadoop-slave1



24) [master]
sudo vim /usr/local/hadoop/etc/hadoop/core-site.xml

<configuration>
<property>
<name>fs.defaultFS</name>
<value>hdfs://hadoop-master:9000</value>
</property>
</configuration>

25) [master]
sudo vim /usr/local/hadoop/etc/hadoop/hdfs-site.xml

<configuration>
<property>
<name>dfs.namenode.name.dir</name><value>/usr/local/hadoop/data/nameNode</value>
</property>
<property>
<name>dfs.datanode.data.dir</name><value>/usr/local/hadoop/data/dataNode</value>
</property>
<property>
<name>dfs.replication</name>
<value>2</value>
</property>
</configuration>

26) [master]
sudo vim /usr/local/hadoop/etc/hadoop/workers

hadoop-slave1

27) [master]
scp /usr/local/hadoop/etc/hadoop/* hadoop-slave1:/usr/local/hadoop/etc/hadoop/


28) [master]
source /etc/environment
hdfs namenode -format

29) [master]
start-dfs.sh
jps

... sudo apt install -y openjdk-8-jdk-headless ?

... `hadoop datanode` in a separate terminal

29) [slave]
start-dfs.sh
jps

    https://stackoverflow.com/questions/48978480/hadoop-permission-denied-publickey-password-keyboard-interactive-warning/49960886

<!-- 29) [master]
export PDSH_RCMD_TYPE=ssh -->


31) [both]
export HADOOP_HOME="/usr/local/hadoop"
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME

32) [slave]
sudo vim /usr/local/hadoop/etc/hadoop/yarn-site.xml

<property>
<name>yarn.resourcemanager.hostname</name>
<value>hadoop-master</value>
</property>


32) [master]
start-yarn.sh




## Test Hadoop processing [master]

### https://github.com/iv-stpn/hadoop-mapreduce-examples

git clone https://github.com/makayel/hadoop-examples-mapreduce
cd hadoop-examples-mapreduce
sudo apt install -y maven
mvn install -DskipTests
wget https://raw.githubusercontent.com/makayel/hadoop-examples-mapreduce/main/src/test/resources/data/trees.csv
hdfs dfs -mkdir -p /user/hadoopuser
hdfs dfs -put trees.csv
yarn jar ~/hadoop-examples-mapreduce/target/hadoop-examples-mapreduce-1.0-SNAPSHOT-jar-with-dependencies.jar wordcount trees.csv count
hdfs dfs -cat count/part-r-00000


# Cleanup EC2

aws ec2 terminate-instances --profile $AWS_PROFILE --region $AWS_REGION --instance-ids $(aws ec2 describe-instances --profile $AWS_PROFILE --region $AWS_REGION --query 'Reservations[].Instances[].InstanceId' --filters "Name=tag:Name,Values=ProtocolLabs-dev" --output text)