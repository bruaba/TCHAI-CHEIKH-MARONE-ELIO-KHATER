# Tchaï - Chain of transactions

Advanced Information Systems Project

## Table of contents
* [General info](#general-info)
* [Technology](#technology)
* [Diagram](#diagram)
* [Setup](#setup)
* [Transaction](#transaction)
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

## Transaction

You can perform a transaction directly using a CURL request
example

````
$ curl -X POST "http://0.0.0.0:5000/deal/1/2/34"

````

Here user 1 sends 34 to user 2

To authenticate the user, we first encrypt the message by doing

For example if 1 wants to send 450 to 2

````
$ python3 signature.py "1|2|450"

````
He returns the signature to us.


We can check if the encryption went well by making the message followed by the signature
Here the signature is equal to 1efdf2d99bedeea5a7a99720ea711662958d0c75300c4c68d2bad3d1888069cb358978238313d34b50e7c931ae6b9f273727662b35e7385cb85a25670bfd3925523f5a9bccd4ede47c33af0592b2021fd33247df2677e9ad6806e7235b836f7a88293a14d32f7266949f93f2d64ea68e8754e265811116477484af391a0a1126

````
$ Python3 signature.py "1|2|450" "1efdf2d99bedeea5a7a99720ea711662958d0c75300c4c68d2bad3d1888069cb358978238313d34b50e7c931ae6b9f273727662b35e7385cb85a25670bfd3925523f5a9bccd4ede47c33af0592b2021fd33247df2677e9ad6806e7235b836f7a88293a14d32f7266949f93f2d64ea68e8754e265811116477484af391a0a1126"

````
Before sending the request with the signature to save it

````
$ Curl -X POST "http://0.0.0.0:5000/deal/1/2/450/1efdf2d99bedeea5a7a99720ea711662958d0c75300c4c68d2bad3d1888069cb358978238313d34b50e7c931ae6b9f273727662b35e7385cb85a25670bfd3925523f5a9bccd4ede47c33af0592b2021fd33247df2677e9ad6806e7235b836f7a88293a14d32f7266949f93f2d64ea68e8754e265811116477484af391a0a1126"
````

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

