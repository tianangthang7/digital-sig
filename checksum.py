from Crypto.Hash import SHA256, SHA, MD5
import sys

#create checksum

def create_checksum(hashAlg, fileName):
    if (hashAlg == "SHA-1"):
        hash_object = SHA.new()
    elif (hashAlg == "SHA-256"):
        hash_object = SHA256.new()
    else :
        hash_object = MD5.new()

    with open(fileName, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_object.update(chunk)

    return  hash_object

def check_checksum(hashAlg,fileName,checksum):
    hash_object=create_checksum(hashAlg,fileName)
    hashStr=hash_object.hexdigest()
    
    print('hash string: '+ hashStr)
    print('checksum: '+ checksum)
    if(hashStr==checksum):
        print('checksum and hash string are equal')
    else:
        print('checksum and hash string are not equal')



if __name__ == "__main__":
    hashAlg=sys.argv[2].upper()
    checksum=''
    fileName=''
    if(len(sys.argv)==6):
        checksum=sys.argv[4]
        fileName=sys.argv[5]
    else:
        fileName=sys.argv[3]


    # create checksum
    if(len(sys.argv)==4):
        print(create_checksum(hashAlg, fileName).hexdigest())
    else: #check 
        check_checksum(hashAlg,fileName,checksum)
        
