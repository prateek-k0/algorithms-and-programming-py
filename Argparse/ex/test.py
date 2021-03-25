##from concurrent import futures
from contextlib import AbstractContextManager
from threading import Thread
import argparse
import asyncio
import functools
import hashlib
import os
import random
import sys


def async_wrap(func):
    @functools.wraps(func)
    async def wrapper():
        return func()
    return wrapper


class Namespace():
    client_id = hashlib.sha1(str(random.randint(1,1)).encode()).hexdigest()
    local_file_list = []
    exchange_server = '192.168.43.96'
    path = 'C:\\Users\\Public\\Documents\\'

    @staticmethod
    def get_client_id():
        return Namespace.client_id

    @staticmethod
    def get_file_list():
        return Namespace.local_file_list

    @staticmethod
    def update_local_file_list():
        if not os.path.exists(Namespace.path+Namespace.client_id):
            os.mkdir(Namespace.path+Namespace.client_id)
            Namespace.local_file_list = []
            return
            

        else:
            path = Namespace.path+Namespace.client_id
            Namespace.local_file_list = []
            for _, _, files in os.walk(path):
                for file in files:
                    Namespace.local_file_list.append(file)
            return



class local_server(Thread, AbstractContextManager):

    def __init__(self, name):
        Thread.__init__(self, daemon = True, name = name)

    def __enter__(self):
        return self

    def __exit__(*exception_details):
        return None

    @staticmethod
    async def server_daemon(reader, writer):
        while True:
            data = await reader.read(1024)
            if data.decode() == 'exit' or not data:
                #print('Disconnected from ', writer.get_extra_info('peername')[0])
                break
##            print(data)
            writer.write(data)
            await writer.drain()
        writer.close()

    @staticmethod
    async def init_server_daemon():
        server = await asyncio.start_server(local_server.server_daemon,'192.168.43.96',9990)
        print('[+] Starting server locally on port 9990 . . .')
        async with server:
            await server.serve_forever()

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(local_server.init_server_daemon())



class p2p_client():
    #_loop = asyncio.get_event_loop()

    @staticmethod
    async def connect_ex():
        #p2p_client.ex_serv = Namespace.exchange_server
        while True:
            es_port = random.choice(range(4000,4001))
            try:
                reader_ex, writer_ex = await asyncio.open_connection(Namespace.exchange_server, es_port)
                print('[+] Connected to the Exchange Server')
                return reader_ex, writer_ex

            except:
                print('[-] Could not connect to the exchange server')
                print('[-] Retrying in 5. . .')
                await asyncio.sleep(5)


    @staticmethod
    async def client_console():
        print('[+] Welcome to sPynet!')
        print('[+] Node ID : {}'.format(Namespace.get_client_id()),end = '\n')
        print('[+] Enter your command')

        while True:

            cmd = input('>!< ')
            if cmd == 'start':
                start_task = asyncio.create_task(p2p_client.connect_ex())
                with local_server('_server_thread') as serv_obj:
                    serv_task = asyncio.create_task(async_wrap(serv_obj.start))
                    await asyncio.wait([start_task, serv_task])
                    reader_ex, writer_ex = start_task.result()
                continue

                #serv_daemon = asyncio.ensure_future(local_server.last())
                #pool = futures.ThreadPoolExecutor(max_workers=1)
                #server_thread = asyncio.get_event_loop().run_in_executor(pool, p2p_client.start_server_daemon)
                #await asyncio.wait([start_task, server_thread])
                #await asyncio.wait([start_task, serv_daemon])

                #completed, _ = await asyncio.wait([start_task])
                #for i in completed:
                   #print(i.result())


            elif cmd == 'query file':
                fname = input('Enter the file name to be queried : ')
                writer_ex.write(fname.encode())
                await writer_ex.drain()
                data_read = await reader_ex.read(1024)
                print(data_read.decode())



##if __name__ == '__main__':
##    asyncio.run(p2p_client.client_console())
