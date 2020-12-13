#librairie
import sqlite3
import binascii
from flask import *
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import BLAKE2b
from hashlib import blake2b


app = Flask(__name__)

#Home
@app.route('/')
def hello():
	return 'Hello \n', 200

#exercice 7
#integrity
#cette fonction nous permet de verifier l'integrité d'une transaction.
#elle nous dit que la transcation a été modifier ou non

@app.route('/integrity/v2/<idTransaction>', methods=['GET'])
def verifIntegrity(idTransaction):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = 'SELECT amount, hash, sender, receiver  FROM deal WHERE id_transaction = ?;'
	cur.execute(sql,[idTransaction])

	result = "<table style='border:1px solid red'>"   
	for row in cur:
		result = result + "<tr>"
		amount = row[0]
		idSender = row[2]
		idReceiver = row[3]
		key = str(idSender) + '|' + str(idReceiver)   + '|' +  str(amount)
		newHash = blake2b(key.encode()).hexdigest()
		oldHash = row[1]
	
	result = result + "</tr>" 
	connexion.commit()
	cur.close()
	connexion.close()
	if newHash == oldHash:
		return '<html><body> C\'est bon</body></html>', 200
	else :
		return '<html><body> Donnée corrompu </body></html>', 500
	

#exercice 10
#integrity

@app.route('/integrity/v3/<idTransaction>', methods=['GET'])
def verifIntegrityV3(idTransaction):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = 'SELECT hash FROM deal WHERE id_transaction = ?;'
	oldHashP = int(idTransaction) - 1
	cur.execute(sql,[oldHashP])
	for row in cur:
		oldHashP = row[0]

	oldHashP = str(oldHashP)
	sql = 'SELECT amount, hash, sender, receiver FROM deal WHERE id_transaction = ?;'
	cur.execute(sql,[idTransaction])

	result = "<table style='border:1px solid red'>"   
	for row in cur:
		result = result + "<tr>"
		amount = row[0]
		idSender = row[2]
		idReceiver = row[3]
		key = str(idSender) + '|' + str(idReceiver)   + '|' + str(amount)
		key = key + '|' + oldHashP
		newHash = blake2b(key.encode()).hexdigest()
		oldHash = row[1]
	
	result = result + "</tr>" 
	connexion.commit()
	cur.close()
	connexion.close()
	if newHash == oldHash:
		return '<html><body> C\'est bon</body></html>', 200
	else :
		return '<html><body> Donnée corrompu </body></html>', 500
	



#Deal
@app.route('/deal/<idSender>/<idReceiver>/<amount>/<signature>', methods=['POST'])
def addDealWithSign (idSender, idReceiver, amount, signature):


	key = str(idSender) + '|' + str(idReceiver)  + '|' + str(amount)

	signature = binascii.unhexlify(signature.encode())

	#importer des clés à partir d'un fichier
	with open('publiccheikhmarone.pem','r') as fp:
		pub = fp.read()
		fp.close()

	public = RSA.importKey(pub)


	# Verify valid PKCS#1 v1.5 signature (RSAVP1)
	hash = BLAKE2b.new()
	hash.update(key.encode())
	verifier = PKCS115_SigScheme(public)

	try:
		verifier.verify(hash, signature)
		#print("Signature is valid.")
		connexion = sqlite3.connect("DataBase/tchai.db")
		cur = connexion.cursor()
		#1er methode avec seulement le montant
		sql = 'SELECT id_transaction, hash FROM deal;'
		cur.execute(sql)

		for row in cur:
			oldHash = row[1]
			lastId = row[0]

		amountFloat = float(amount)
		key = str(idSender) + '|' + str(idReceiver)  + '|' + str(amountFloat)	
		key = key + '|' + oldHash 
		#hash
		ahash = blake2b(key.encode()).hexdigest()
		idSender = int(idSender,  16)
		sql = "INSERT INTO deal (amount, sender, receiver, hash) VALUES (?,?,?,?)"
		cur.execute(sql,[amount, idSender, idReceiver, ahash])
		connexion.commit()
		cur.close()
		connexion.close()
		return 'Deal Done.\n', 200

	except:
		#print("Signature is invalid.")
		return 'Vous n\'êtes pas '+ idSender +' .\n', 403


@app.route('/deal/<idSender>/<idReceiver>/<amount>', methods=['POST'])
def addDeal (idSender, idReceiver, amount):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	#1er methode avec seulement le montant
	sql = 'SELECT id_transaction, hash FROM deal;'
	cur.execute(sql)

	for row in cur:
		oldHash = row[1]
		lastId = row[0]

	amountFloat = float(amount)
	key = str(idSender) + '|' + str(idReceiver) + '|' +str(amountFloat)
	key = key + '|' + oldHash 
	#hash
	ahash = blake2b(key.encode()).hexdigest()
	sql = "INSERT INTO deal (amount, sender, receiver, hash) VALUES (?,?,?,?)"
	cur.execute(sql,[amount, idSender, idReceiver, ahash])
	connexion.commit()
	cur.close()
	connexion.close()
	return 'Deal Done.\n', 200

@app.route('/deal/<idPerson>', methods=['GET'])
def getDealPerson (idPerson):

	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = 'SELECT * FROM deal WHERE sender  = '+idPerson+' or receiver = '+idPerson+' ORDER BY moment ASC'
	cur.executescript(sql)
	rows = cur.fetchall()
	result = "<table style='border:1px solid red'>"   
	for row in rows:
		result = str(row) + "<tr>"
		for x in row:
			result = result + "<td>" + str(x) + "</td>"
	result = result + "</tr>" 
	connexion.commit()

	cur.close()
	connexion.close()
	return '<html><body>' + result + '</body></html>', 200

@app.route('/test/<idPerson>', methods=['GET'])
def verif(idPerson):

	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = 'SELECT * FROM deal WHERE sender  = '+idPerson+' or receiver = '+idPerson+' ORDER BY moment ASC'
	cur.executescript(sql)
	result = "<table style='border:1px solid red'>"   
	for row in cur:
		result = result + "<tr>"
		for x in row:
			result = result + "<td>" + str(x) + "</td>"
	result = result + "</tr>" 
	connexion.commit()

	cur.close()
	connexion.close()
	return '<html><body>' + result + '</body></html>', 200


@app.route('/deal', methods=['GET'])
def getDeal ():
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = "SELECT p1.name, p1.surname, d.amount, p2.name, p2.surname, d.moment FROM deal as d INNER JOIN person as p1 on d.sender = p1.id_person INNER JOIN person as p2 on d.receiver = p2.id_person ORDER BY d.moment ASC"
	cur.execute(sql)
	result = "<table style='border:1px solid red'>"   
	for row in cur:
		result = result + "<tr>"
		for x in row:
			result = result + "<td>" + str(x) + "</td>"
	result = result + "</tr>" 
	connexion.commit()
	cur.close()
	connexion.close()
	return '<html><body>' + result + '</body></html>', 200


#Account
@app.route('/account/<idOwner>', methods=['GET'])
def getBalance (idOwner):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = "SELECT sum(amount) FROM Deal WHERE sender  = ?"
	cur.execute(sql,[idOwner])
	for row in cur:
		result = ""
		for x in row:
			result = str(x)

	connexion.commit()
	cur.close()
	connexion.close()
	return 'Balance = ' + result + ' €\n', 200


#Person

@app.route('/user/<name>/<surname>', methods=['POST'])
def addUser (name, surname):
	#creation d´un couple de clés
	key = RSA.generate(1024)

	#afficher ses clés:
	k = key.exportKey('PEM')
	p = key.publickey().exportKey('PEM')

	k_name = 'private'+name+surname+'.pem'
	p_name = 'public'+name+surname+'.pem'

	#sauvegarder ses clés dans des fichiers:
	with open(k_name,'w') as kf:
		kf.write(k.decode())
		kf.close()

	with open(p_name,'w') as pf:
		pf.write(p.decode())
		pf.close()

	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = "INSERT INTO person (name, surname, public_key) VALUES (?,?, ?)"
	cur.execute(sql,[name, surname, hex(key.n)])
	connexion.commit()
	cur.close()
	connexion.close()
	

	return 'User created your private key is '+ str(k) +'.\n', 200


#Person

@app.route('/sign/<sender>/<receiver>/<amount>', methods=['POST'])
def addUserWithSign (sender, receiver, amount):
	#creation d´un couple de clés
	key = RSA.generate(1024)

	#afficher ses clés:
	k = key.exportKey('PEM')
	p = key.publickey().exportKey('PEM')

	k_name = 'private'+name+surname+'.pem'
	p_name = 'public'+name+surname+'.pem'

	#sauvegarder ses clés dans des fichiers:
	with open(k_name,'w') as kf:
		kf.write(k.decode())
		kf.close()

	with open(p_name,'w') as pf:
		pf.write(p.decode())
		pf.close()

	leHash = blake2b(msg.encode()).hexdigest()
	signature = pow(leHash, key.d, key.n)
	print("Signature:", hex(signature))

	return 'Signature '+ str(hex(signature)) +'.\n', 200

app.run(host='0.0.0.0', debug=True)

