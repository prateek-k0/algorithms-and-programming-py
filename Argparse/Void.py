''' In greed we lust, the rest relinquished '''

import argparse
import ipaddress

''' function to check validity of the port number provided '''
def check_port(port):
    if int(port) in range(1,65536):
        return int(port)
    else:
        raise ValueError('Invalid Port number. Please enter correct Port number.')


''' Creating the top-level Parser '''
parser = argparse.ArgumentParser(prog = 'Void', description = 'Dont really know what it does!')

''' Creating Subparser for various commands '''
sub_parser = parser.add_subparsers(title = 'Subcommands available', dest = 'subcommand', description = 'Valid Subcommads', help = 'Subcommands help')

''' Creating Parent parsers for common set of arguments between each subcommand '''
common_parser = argparse.ArgumentParser(add_help = False, prefix_chars = '-')
common_parser.add_argument('-p', '--port', dest = 'lport', nargs = '?', metavar = 'PORT', default = '8080', type =check_port, help = 'Use the given local Port, default : 8080')
common_parser.add_argument('-e', '--exec', dest = 'command', nargs = '?', metavar = 'COMMAND', help = 'Execute the given command on successful connection')


''' Creating parsers for subcommands '''

''' Creating parser for subcommand "listen" '''
parser_listen = sub_parser.add_parser('listen', parents = [common_parser], help = 'listen help', aliases = ['l'])

''' Creating parser for subcommand "connect" '''
parser_connect = sub_parser.add_parser('connect', parents = [common_parser], help = 'connect help', aliases = ['c'])
parser_connect.add_argument('address', action = 'store', metavar = 'Destination_Address', nargs = 1, type = ipaddress.ip_address, help = 'Address of the destination')
parser_connect.add_argument('port', action = 'store', metavar = 'Destination_Port', nargs = 1, type = check_port, help = 'Port of the destination')
parser_connect.add_argument('--proxy', dest = 'proxy_conf', metavar = 'Proxy_Config_file', nargs = 1, type = argparse.FileType('wb', bufsize=0), help = 'Provide filw with Proxychain configuration')

if __name__ == '__main__' :
#    parser_listen.print_help()
    args = parser.parse_args()
    print(args)
