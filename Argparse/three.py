import argparse

parser = argparse.ArgumentParser(prog = 'program_3', description = 'Basic Math', argument_default=argparse.SUPPRESS)
''' Notice the argument "argument_default = argparse.SUPPRESS", what it does is,  if an argument does not appear in the argv, it does not appear in the Namespace '''
''' Remove that argument, and you will see that the namespace will contain the arguments with default values, if not specified. '''

parser.add_argument('--add',nargs = '*',type = float, help = 'Provide numbers to perform addition')
#nargs = '*' denotes that there may be any number of arguments to it
parser.add_argument('--p', '-proxy_addresses',nargs = '*', type = str , help = 'Provide Proxy-chain IPs')
args = parser.parse_args(['--add', '1', '2', '3', '45'])
print(args)
