# bai 1
tao chu ky so dung RSA
cau lenh:
python sign.py -h <hash> <file name>
vi du: 
python sign.py -h MD5 text.txt

# bai 3 
kiem tra chu ky so 
cau lenh:
python verify_sign.py -h <hash> <file name> <file name.sig>
vidu:
python verify_sign.py -h MD5 text.txt text.txt.sig

# bai 2 
tao checksum va kiem tra
cau lenh tao checksum:
python checksum.py -h <hash> <file name>
vi du:
python checksum.py -h md5 text.txt

cau lenh kiem tra checksum
python checksum.py -h <hash> -c <checksum> <input_file>
vi du:
python checksum.py -h md5 -c 863598052ffeddc550ed4e5310382600  text.txt