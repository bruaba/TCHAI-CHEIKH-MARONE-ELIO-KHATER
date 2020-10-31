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
	cur.close()
	connexion.close()
	return 'Deal Done.\n', 200

@app.route('/deal/<idPerson>', methods=['GET'])
def getDealPerson (idPerson):

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
	return '<html><body>' + sql + '</body></html>', 200

#etat actuel du test d'injection sql
#mais marche pas 
#curl -X GET "http://0.0.0.0:5000/deal/1'%20;%20--%20UPDATE%20DEAL%20SET%20amount%20=%2012000%20WHERE%20sid_deal=1;%20select%20true;"
#curl -X GET "http://0.0.0.0:5000/deal/'1%20UNION%20\%20UPDATE%20DEAL%20SET%20amount%20=%20800%20WHERE%20sender%20=%201%20;%20--"

#curl -X GET "http://0.0.0.0:5000/deal/''%20;%20UPDATE%20DEAL%20SET%20amount%20=%208000%20WHERE%20ssender=1;--%20"

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

#commande curl pour ajout d'un user 
#curl -X POST "http://localhost:5000/user/sow/samba"

