# Tchaï - Chain of transactions

Advanced Information Systems Project

## Table of contents
* [General info](#general-info)
* [Technology](#technology)
* [Diagram](#diagram)
* [Setup](#setup)
* [Test](#test)
* [School](#school)
* [Authors](#authors)

## General info
Design an electronic transaction system with guaranteed integrity, accessible by the HTTP protocol


## Technology
Project is created with:
* Python version: 3.8
* Flask
* Sqlite3

## Diagram
![Class Diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/bruaba/TCHAI-CHEIKH-MARONE-ELIO-KHATER/main/UML/diagram.puml)
	
## Setup
To run this project, install it locally using:

```
$ apt-get install python3-pip
$ pip3 install flask
$ apt-get install sqlite3
$ python3 tchai.py

```

## Test
1st test it's changing amount value

```
$ cd /Test
$ chmod +x modifyTransaction.sh
$ ./modifyTransaction.sh

```
That changes the amount value by 8000 for example
So for that i change execute() function of tchai.py by executescript(). Because execute() execute one statement at a time.

## Authors
Cheikh Ahmet Tidiane Chérif MARONE 
* maronho16@gmail.com 
* https://bitbucket.org/bruaba/

Elio KHATER

## School
* ESIREM https://esirem.u-bourgogne.fr/
* Year: 2020
* With Sergey KIRGIZOV sergey.kirgizov@u-bourgogne.fr
* Source : https://kirgizov.link/teaching/esirem/advanced-information-systems-2020/TP-PROJET.pdf

