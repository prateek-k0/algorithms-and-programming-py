import argparse

parser = argparse.ArgumentParser(prog = 'Ncat Dummy', description = 'Ncat like tool')
parser.add_argument('-l','--listen',dest = 'Listen' ,action = 'count', help = 'Set up Ncat Listener')
parser.add_argument('-v','--verbose',dest = 'Verbose', action = 'count', help = 'Add to increase verbosity of the outpout')
parser.add_argument('-p','--port', dest = 'lport' ,nargs = '?', metavar = 'zzzz', default = '8080', help = 'Use the given local Port')
parser.add_argument('--proxy',dest = 'Proxychain', nargs = 1, metavar = 'File', type = argparse.FileType('r'), help = 'Provide ProxyChains File')
parser.add_argument('--ssl',  action = 'store_true', help = 'Use for encrypted connections')
parser.add_argument('Destination Address',  action = 'store', help = 'Address of the destination')
parser.add_argument('Destination Port',action = 'store', help = 'Port number of the destination')

'''
For inputing file types:
we can use type = open
    parser.add_argument('bar', nargs=1 ,type=open)

or for better control over the options, we can use FileType method
    parser.add_argument('bar', type=argparse.FileType('w')) #opening a file in write mode

the argparse module provides the factory FileType
which takes the mode=, bufsize=, encoding= and errors= arguments of the open() function. 
'''

args = parser.parse_args()
print(args)
