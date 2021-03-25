from concurrent import futures
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
        self.loop = asyncio.get_event_loop()

    async def hash_dir(self, directory):
        if not os.path.exists(directory):
            return -1

        for root, dirs, files in os.walk(directory):
            for file in files:
                await self.file_hasher(os.path.join(root,file))
                
            if len(dirs):
                for d in dirs:
                    self.directories.append(d)


    async def file_hasher(self, filepath):
        f_hash = hashlib.sha3_384()
        with open(filepath,'rb') as file:
            while True:
                data = file.read(self.buf_size)
                if not data:
                    break
                f_hash.update(data)
##                self.dir_hasher.update(data)

        self.file_hash[filepath] = str(f_hash.hexdigest())
        return
    

    def calc_hash(self, directory):
        self.loop.run_until_complete(self.hash_dir(directory))
        return


if __name__ == '__main__':
    a = time.time()
    obj = LocalNodeFiles(1)
    obj.calc_hash(b'C:\Users\Prateek\Desktop\NULL')
    print(obj.file_hash)
    print()
    print(time.time()-a)
        
