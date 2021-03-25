import argparse

parser = argparse.ArgumentParser(prog = 'program_one', description='Example Arguement Parser')
parser.add_argument('-p', '--port',  action = 'store', default = '8080', help = 'Port Number of the remote pc', type = str)
# action = 'store' simply stores the value for the optional arguement
parser.add_argument('IP', help = 'IP address of the remote pc',type=str)

args = parser.parse_args() #can be empty if we want to parse all arguements
print(args.IP)
print(args.port)
