# Tchaï - Chain of transactions

Advanced Information Systems Project

## Table of contents
* [General info](#general-info)
* [Technology](#technology)
* [Diagram](#diagram)
* [Setup](#setup)
* [Test](#test)
* [Hash](#hash)
* [Tag](#tag)
* [School](#school)
* [Authors](#authors)

## General info
Design an electronic transaction system with guaranteed integrity, accessible by the HTTP protocol+


## Summary

The project was composed of 3 big tasks that needed to be done:
* Define a transaction and all its elements.
* add hash to transaction and creating a secure environment.
* add asymmetrical cryptography to ensure user authenticity.




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
1°) That changes the amount value by 8000 for example
So for that i change execute() function of tchai.py by executescript(). Because execute() execute one statement at a time.

2°) Delete transaction

## Hash
Hash function : BLAKE2b()

[BLAKE2](https://docs.python.org/fr/3.7/library/hashlib.html#blake2) is a cryptographic hash function defined in RFC 7693 that comes in two flavors:

* BLAKE2b, optimized for 64-bit platforms and produces digests of any size between 1 and 64 bytes,

* BLAKE2s, optimized for 8- to 32-bit platforms and produces digests of any size between 1 and 32 bytes.

BLAKE2 supports keyed mode (a faster and simpler replacement for HMAC), salted hashing, personalization, and tree hashing.

Contrary SHA256 was based on SHA1 (which is weak), BLAKE was based on ChaCha20 (which is strong).

BLAKE2 is resisted collision, Preimage, Chosen prefix collision attack, ... 

[BLAKE2b](https://fr.qaz.wiki/wiki/BLAKE_(hash_function)) is faster than MD5, SHA-1, SHA-2 and SHA-3, on 64-bit x86-64 and ARM architectures. BLAKE2 offers greater security than SHA-2 and similar to that of SHA-3: immunity to length extension, undifferentiability of a random oracle, etc.


## Tag
The tag complete (1.0), correspond to the end of the exercises.
During the exercise we use a 0.5 tag for example and at the end of the version as stipulated in the subject we tag with 1.0

## Authors
Cheikh Ahmet Tidiane Chérif MARONE 
* maronho16@gmail.com 
* https://bitbucket.org/bruaba/

Elio Khater
* eliokhater@gmail.com




## School
* ESIREM https://esirem.u-bourgogne.fr/
* Year: 2020
* With Sergey KIRGIZOV sergey.kirgizov@u-bourgogne.fr
* Source : https://kirgizov.link/teaching/esirem/advanced-information-systems-2020/TP-PROJET.pdf

