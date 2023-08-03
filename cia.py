import pyaes
from pyDes import *
from cryptography.fernet import Fernet


def AES():
    aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    plaintext = input("Enter plain text for aes: ")
    ciphertext = aes.encrypt(plaintext)
    print(ciphertext)
    aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    plaintext = aes.decrypt(ciphertext)
    print(plaintext)

AES()

def DES():
    data = input("Enter plain text for des: ")
    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5) 
    d=k.encrypt(data)
    print("Encrypted: %r" % d)
    print("Decrypted: %r" % k.decrypt(d))
      
DES()

def symmetric():

    plaintext = input("Enter plain text: ")

    key = Fernet.generate_key()

    f = Fernet(key)

    token = f.encrypt(b"hello")

    print(token)

    d = f.decrypt(token)

    print(d)


symmetric()






# cryptography = input("Enter type of cryptgraphy: ")


