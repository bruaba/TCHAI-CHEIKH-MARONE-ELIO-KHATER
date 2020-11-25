from flask import *
import sqlite3
from hashlib import blake2b

app = Flask(__name__)

#Home
@app.route('/')
def hello():
	return 'Hello \n', 200

#integrity
#cette fonction nous permet de verifier l'integrité d'une transaction.
#elle nous dit que la transcation a été modifier ou non

@app.route('/integrity/<idTransaction>', methods=['GET'])
def verifIntegrity(idTransaction):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = 'SELECT amount, hash FROM deal WHERE id_transaction = ?;'
	cur.execute(sql,[idTransaction])

	result = "<table style='border:1px solid red'>"   
	for row in cur:
		result = result + "<tr>"
		amount = row[0]
		key = str(amount)
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
@app.route('/deal/<idSender>/<idReceiver>/<amount>', methods=['POST'])
def addDeal (idSender, idReceiver, amount):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	amountFloat = float(amount)
	key = str(amountFloat)
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
	sql = "SELECT balance FROM account WHERE owner  = ?"
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
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = "INSERT INTO person (name, surname) VALUES (?,?)"
	cur.execute(sql,[name, surname])
	connexion.commit()
	cur.close()
	connexion.close()
	return 'User created.\n', 200

app.run(host='0.0.0.0', debug=True)

