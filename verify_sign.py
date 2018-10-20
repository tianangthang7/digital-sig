from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256, SHA, MD5
from Crypto.PublicKey import RSA
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




if __name__ == "__main__":
    hashAlg=sys.argv[2].upper()
    fileName=sys.argv[3]
    fileSigName=sys.argv[4]

    fileIn = open(fileName,'r')
    mess = fileIn.read();
    fileIn.close()
    mess_hashed = hash_mess(hashAlg,mess)

    fileSigIn = open(fileSigName,'rb')
    signature = fileSigIn.read();
    fileSigIn.close()
    

    key = RSA.importKey(open('mykey.pem').read())
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(mess_hashed, signature):
        print('The signature is authentic.')
    else:
        print ('The signature is not authentic.')