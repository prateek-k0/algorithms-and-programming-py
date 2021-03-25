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
        
        with futures.ThreadPoolExecutor(max_workers = 10) as Pool:
            for root, dirs, files in os.walk(directory):
            
                if len(files):
                    filepaths = [os.path.join(root,file) for file in files]

                    f_objects = [functools.partial(LocalNodeFiles.file_hasher, self, filepath) for filepath in filepaths]
                    tasks = [self.loop.run_in_executor(Pool, fobj) for fobj in f_objects]
                    await asyncio.wait(tasks)

##                    tasks = [self.loop.run_in_executor(Pool, functools.partial(LocalNodeFiles.file_hasher, self, filepath)) for filepath in filepaths]          
##                    await asyncio.wait(tasks)
                    
##                    await asyncio.wait([self.loop.run_in_executor(Pool, functools.partial(LocalNodeFiles.file_hasher, self, filepath)) for filepath in filepaths])
                    
##                    await asyncio.wait([self.loop.run_in_executor(Pool, functools.partial(LocalNodeFiles.file_hasher, self, os.path.join(root,file))) for file in files])
                    
                       
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

        self.file_hash[filepath] = str(f_hash.hexdigest())
        return
    
    

    def calc_hash(self, directory):
        self.loop.run_until_complete(self.hash_dir(directory))
        return


if __name__ == '__main__':

    obj = LocalNodeFiles(1)
    a = time.time()
    obj.calc_hash(b'C:\Users\Prateek\Desktop\NULL')
##    print(obj.file_hash)
    print()
    print(time.time()-a)
    
        
