import hashlib


buf_size = 65536    #a bhunk of 64kb

with open("hash_ex.txt",'rb') as file:
    file_hash = hashlib.sha3_512()
    while True:
        data = file.read(buf_size)
        if not data:
          break
        file_hash.update(data)
    print('Hash of the file: {}'.format(file_hash.hexdigest()))



