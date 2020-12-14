import sys
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import BLAKE2b
from hashlib import blake2b

import binascii


transaction = sys.argv[1]
name_file = sys.argv[2]
"""
#creation d´un couple de clés
key = RSA.generate(1024)
pubKey = key.publickey()
"""

"""
print(f"Public key:  (n={hex(key.n)}, e={hex(key.e)})"+'\n')
print(f"Private key: (n={hex(key.n)}, d={hex(key.d)})"+'\n')

"""

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
"""
#afficher ses clés:
k = key.exportKey('PEM')
p = key.publickey().exportKey('PEM')

name = 'cheikh'
surname = 'marone'

p_name = 'public'+name+surname+'.pem'

#sauvegarder ses clés dans des fichiers:

with open(p_name,'w') as pf:
	pf.write(p.decode())
	pf.close()
"""

#importer des clés à partir d'un fichier

with open(name_file,'r') as fp:
	pub = fp.read()
	fp.close()

key = RSA.importKey(pub)
print(key)

hash = BLAKE2b.new()
hash.update(transaction.encode())
signer = PKCS115_SigScheme(key)
signature = signer.sign(hash)


print("Signature hexlify :", binascii.hexlify(signature))
#print("publickey", pubKey)