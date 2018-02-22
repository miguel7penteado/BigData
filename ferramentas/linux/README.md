# Ferramentas

## 1. Java 8

```bash
# Instalar Oracle Java 8 em DEBIAN, DEVUAN ou UBUNTU
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer

```

## 2. Scala

```bash
# Instalar Scala em DEBIAN, DEVUAN ou UBUNTU
wget www.scala-lang.org/files/archive/scala-2.11.7.deb
sudo dpkg -i scala-2.11.7.deb

# git install
sudo apt-get install git
```

## 3. SBT

```bash

# Instalar o sbt em DEBIAN, DEVUAN ou UBUNTU
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
sudo apt-get update
sudo apt-get install sbt



```
