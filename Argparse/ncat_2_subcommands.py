import argparse

''' this version includes functionality of sub arguments, such as ncat listen, or ncat connect '''

''' ArgumentParser supports the creation of such sub-commands with the add_subparsers() method.
The add_subparsers() method is normally called with no arguments and returns a special action object.
This object has a single method, add_parser(), which takes a command name and any ArgumentParser
constructor arguments, and returns an ArgumentParser object that can be modified as usual. '''

parser = argparse.ArgumentParser(prog = 'Ncat Dummy', description = 'Ncat like tool')
subparsers = parser.add_subparsers(title = 'Subcommands available',description='Valid Subcommands', help = 'Subcommands help')

''' add subcommand "listen" '''
parser_listen = subparsers.add_parser('listen', help = 'listen help',aliases = ['l'])
parser_listen.add_argument('-p','--port', dest = 'lport' ,nargs = '?', metavar = 'PORT', default = '8080', help = 'Use the given local Port')

''' add subcommand "connect" '''
parser_connect = subparsers.add_parser('connect', help = 'connect help',aliases = ['c'])
parser_connect.add_argument('-p','--port', dest = 'lport' ,nargs = '?', metavar = 'PORT', default = '8080', help = 'Use the given local Port')
parser_connect.add_argument('Destination Address',  action = 'store', help = 'Address of the destination')
parser_connect.add_argument('Destination Port',action = 'store', help = 'Port number of the destination')

args = parser.parse_args()
print(args)
