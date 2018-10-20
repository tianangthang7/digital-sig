from Crypto.Hash import SHA256, SHA, MD5
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import sys



def hash_mess(hashAlg, mess):
    mess=mess.encode() # string to byte
    if (hashAlg == "SHA-1"):
        hash_object = SHA.new()
    elif (hashAlg == "SHA-256"):
        hash_object = SHA256.new()
    else :
        hash_object = MD5.new()
    hash_object.update(mess)
    return  hash_object


def newkeys(keysize):
    random_generator = Random.new().read
    key = RSA.generate(keysize,random_generator)
    f = open('mykey.pem','wb')
    f.write(key.exportKey('PEM'))
    f.close()
    return key


def sign(mess_hashed, priv_key):
    signer = PKCS1_v1_5.new(priv_key)
    signature = signer.sign(mess_hashed)
    return signature

if __name__ == "__main__":


    hashAlg=sys.argv[2].upper()
    fileName = sys.argv[3]
    fileIn = open(fileName,'r')
    mess = fileIn.read();
    fileIn.close()


    priv_key = newkeys(2048)
    mess_hashed = hash_mess(hashAlg,mess)
    signature=sign(mess_hashed, priv_key)
    f = open(fileName+'.sig','wb')
    f.write(signature)
    f.close()
    print('Signed to file ' + fileName+'.sig')