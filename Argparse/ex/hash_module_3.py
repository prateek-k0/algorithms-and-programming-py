from concurrent import futures
from threading import Thread
##from threading import RLock as Lock
import asyncio
import functools
import hashlib
import os
import time
    

class LocalNodeFiles():

    def __init__(self,nodeid):
        self.file_hash = {}
        self.directories = []
##        self.dir_hasher = hashlib.sha3_384()
        self.buf_size = 1048576 
        self._loop = asyncio.get_event_loop()
##        self._lock = Lock()


    async def hash_dir(self, directory):
        if not os.path.exists(directory):
            return -1

        for root, dirs, files in os.walk(directory):
            
                if len(files):
                    filepaths = [os.path.join(root,file) for file in files]

                    for fp in filepaths:
                        Thread(target = LocalNodeFiles.file_hasher, args = (self,fp), daemon = True).start()

                if len(dirs):
                    for d in dirs:
                        self.directories.append(d)
            
        
    def file_hasher(self, filepath):
        f_hash = hashlib.sha3_384()
        with open(filepath,'rb') as file:
            while True:
                data = file.read(self.buf_size)
                if not data:
                    break

                f_hash.update(data)
##                self.dir_hasher.update(data)
##        with self._lock: 
        self.file_hash[filepath] = str(f_hash.hexdigest())
        return
    
    

    def calc_hash(self, directory):
        self._loop.run_until_complete(self.hash_dir(directory))
        return


if __name__ == '__main__':

    obj = LocalNodeFiles(1)
    a = time.time()
    obj.calc_hash(b'C:\Users\Prateek\Desktop\NULL')
##    print(obj.file_hash)
    print()
    print(time.time()-a)
    
        
