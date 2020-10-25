from flask import *
import sqlite3

app = Flask(__name__)


#Home
@app.route('/')
def hello():
	return 'Hello \n', 200

#Deal
@app.route('/deal/<idSender>/<idReceiver>/<amount>', methods=['POST'])
def addDeal (idSender, idReceiver, amount):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = "INSERT INTO deal (amount, sender, receiver) VALUES (?,?,?)"
	cur.execute(sql,[amount, idSender, idReceiver])
	connexion.commit()
	return 'Deal Done.\n', 200

@app.route('/deal/<idPerson>', methods=['GET'])
def getDealPerson (idPerson):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = "SELECT * FROM deal WHERE sender  = ? OR receiver = ? ORDER BY moment DESC"
	cur.execute(sql,[idPerson, idPerson])
	result = "<table style='border:1px solid red'>"   
	for row in cur:
		result = result + "<tr>"
		for x in row:
			result = result + "<td>" + str(x) + "</td>"
	result = result + "</tr>" 
	connexion.commit()
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
	return 'Balance = ' + result + ' €\n', 200


#Person

@app.route('/user/<name>/<surname>', methods=['POST'])
def addUser (name, surname):
	connexion = sqlite3.connect("DataBase/tchai.db")
	cur = connexion.cursor()
	sql = "INSERT INTO person (name, surname) VALUES (?,?)"
	cur.execute(sql,[name, surname])
	connexion.commit()
	return 'User created.\n', 200

app.run(host='0.0.0.0', debug=True)

#commande curl pour ajout d'un user 
#curl -X POST "http://localhost:5000/user/sow/samba"

#pour la supression
#curl -X DELETE "http://localhost:5000/user/edouard"
