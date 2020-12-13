import sys
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import BLAKE2b
from hashlib import blake2b

import binascii


transaction = sys.argv[1]
signature = sys.argv[2]

signature = binascii.unhexlify(signature.encode())


#importer des clés à partir d'un fichier
with open('publiccheikhmarone.pem','r') as fp:
	pub = fp.read()
	fp.close()

public = RSA.importKey(pub)

print(public)
# Verify valid PKCS#1 v1.5 signature (RSAVP1)
hash = BLAKE2b.new()
hash.update(transaction.encode())
verifier = PKCS115_SigScheme(public)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")
