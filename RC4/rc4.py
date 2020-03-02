# RC4 Algorithm for Encryption and Decryption

def get_message(choice):
    if choice=="1":
        fo = open("plaintext.txt","r")
        s = fo.read()
        s=str(s)
        fo.close()

    if choice=="2":
        fo = open("ciphertext.txt","r")
        s = fo.read()
        s=str(s)
        print(s)
        fo.close()

    return s

def get_key():
    print("Enter your key:")
    key = input()
    if key == '':
        key = 'none_public_key'
    return key

def init_box(key):
    s_box = list(range(256)) 
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    return s_box

def encoder(text,box):

    res = []
    i = j =0
    for s in text:
        i = (i + 1) %256
        j = (j + box[i]) %256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j])% 256
        k = box[t]
        res.append(chr(ord(s)^k))
    cipher = "".join(res)

    fo=open("ciphertext.txt","wb+")    
    print("\n--------------------------------------------------------")       
    print("Encoded Text:")
    print(cipher)
    cipher = cipher.encode()
    fo.seek(0)
    fo.write(cipher)
    fo.seek(0)

    fo.close()


def decoder(text,box):

    res = []
    i = j =0
    for s in text:
        i = (i + 1) %256
        j = (j + box[i]) %256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j])% 256
        k = box[t]
        res.append(chr(ord(s)^k))
    plain = "".join(res)

    fo=open("plaintext.txt","wb+")      
    print("\n--------------------------------------------------------")     
    print("Decoded Text : ")
    print(plain)
    plain = plain.encode()
    fo.seek(0)
    fo.write(plain)
    fo.seek(0)

    fo.close()
    

def get_choice():
    print("\n--------------------------------------------------------")
    print("Please select Encryption or Decryption")
    print("1. Encrypt")
    print("2. Decode")
    choice = input()
    if choice == '1':
        message = get_message(choice)
        key = get_key()
        box = init_box(key)
        encoder(message,box)
    elif choice == '2':
        message = get_message(choice)
        key = get_key()
        box = init_box(key)
        decoder(message, box)
    else:
        print("Incorrect input!")

if __name__ == '__main__':
    while True:
        get_choice()

'''
safir@safir-Predator-PH315-51:~/Desktop/IS$ python3 rc4.py

--------------------------------------------------------
Please select Encryption or Decryption
1. Encrypt
2. Decode
1
Enter your key:
5

--------------------------------------------------------
Encoded Text:
þ&aåi¼ô¥¨¸Q

--------------------------------------------------------
Please select Encryption or Decryption
1. Encrypt
2. Decode
2
þ&aåi¼ô¥¨¸Q
Enter your key:
5

--------------------------------------------------------
Decoded Text : 
Hellow World


--------------------------------------------------------
'''