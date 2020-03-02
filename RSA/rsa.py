# RSA Algorithm for Encryption and Decryption
from decimal import Decimal 

e = 0
d = 0
t = 0
n = 0

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 

def get_data():
    global t
    global n
    p = int(input('Enter the value of p = ')) 
    q = int(input('Enter the value of q = ')) 
    no = int(input('Enter the value of text = ')) 
    n = p*q
    t = (p-1)*(q-1)
    print("n = ",n)
    print("t = ",t)
    return no

def generate_key():
    global e, d, t

    for e in range(2,t): 
	    if gcd(e,t)== 1: 
		    break
    print("e = ", e)
    for i in range(1,10): 
        x = 1 + i*t 
        if x % e == 0: 
            d = int(x/e) 
            break
    print("d = ", d)


def enc_dec(no):
    global n
    ctt = Decimal(0) 
    ctt =pow(no,e) 
    ct = ctt % n 

    dtt = Decimal(0) 
    dtt = pow(ct,d) 
    dt = dtt % n

    print("Cipher Text = "+str(ct))
    print("Decrypted Text = "+str(dt))

if __name__ == '__main__':
    no = get_data()
    generate_key()
    enc_dec(no)

'''
safir@safir-Predator-PH315-51:~/Desktop/IS/RSA$ python3 rsa.py
Enter the value of p = 6
Enter the value of q = 4
Enter the value of text = 1234
n =  24
t =  15
e =  2
d =  8
Cipher Text = 4
Decrypted Text = 16
'''