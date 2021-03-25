import argparse

parser = argparse.ArgumentParser(prog = 'program_2', description = 'Example 2')
#we include an option like verbosity, where we require the count of the occurrence of a particular arguement
parser.add_argument('-v','-verbose' , action = 'count',  help = 'Increase verbosity for each usage')
parser.add_argument('-p', '--port',  action = 'store', default = '8080', help = 'Port Number of the remote pc', type = str)
parser.add_argument('IP', help = 'IP address of the remote pc',type=str)

args = parser.parse_args()
print(args)
