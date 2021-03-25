import os
import hashlib

file_hash = {}
directories = []
dir_hasher = hashlib.sha3_512()
buf_size = 32768

def hash_dir(directory):
    if not os.path.exists(directory):
        return -1
    
    global file_hash, dirs, dir_hasher
    for root, dirs, files in os.walk(directory):

       
        for file in files:
            file_hasher = hashlib.sha3_512()
            filepath = os.path.join(root, file)
            with open(filepath,'rb') as f:
           
                while True:
                    data = f.read(buf_size)
                    if not data:
                        break
                    dir_hasher.update(data)
                    file_hasher.update(data)
                
                file_hash[filepath] = str(file_hasher.hexdigest())
                    
        if len(dirs):
            for i in dirs:
                directories.append(i)
        
hash_dir('.vscode')
print('Directory hash:{}'.format(dir_hasher.hexdigest()))
print(file_hash)
print()
print(directories)
    
            
            

