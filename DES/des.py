# DES Algorithm for Encryption and Decryption using pyDes library

import pyDes
print("\n--------------------------------------")
data = str(input("Enter the text : "))
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
e = k.encrypt(data)
d = k.decrypt(e)
print("\n--------------------------------------")
print ("Encrypted: %r" % e)
print("\n--------------------------------------")
print ("Decrypted: %r" % d)
print("\n--------------------------------------")

'''
safir@safir-Predator-PH315-51:~/Desktop/IS/DES$ python3 des.py

--------------------------------------
Enter the text : Hello World

--------------------------------------
Encrypted: b'\xc2\xe6~Y&\x96K\xbd\x06\xa5\x00{\xf2\xd7\xafP'

--------------------------------------
Decrypted: b'Hello World'

--------------------------------------
'''