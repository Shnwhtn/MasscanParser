import os
from xml.etree import ElementTree
import sys
outputfile = 'output.txt'
# this is an array for what to check so add filters here
checklist = ['apache','401 Unauthorised']
#parse tree


if sys.argv[1] is None:
    raise SystemExit("Need a file to convert")
if not os.path.exists(sys.argv[1]):
    raise SystemExit("File {} does not exist".format(sys.argv[1]))

inputfile = os.path.splitext(sys.argv[1])[0]


dom = ElementTree.parse(sys.argv[1])
scan = dom.findall('host')


#output list
def output(ip,port):
	outputstring = ip +":" +port+"\n"
	with open(outputfile, "a") as output:
		output.write(outputstring)
		

#find childen
def main():
	print("Running")
	for s in scan:
		addr = s.getchildren()[0].items()[0][1]
		port = s.getchildren()[1].getchildren()[0].items()[1][1]
		try:
			banner = s.getchildren()[1].getchildren()[0].getchildren()[1].items()[1][1]
			for elem in checklist:
				if elem in banner:
					output(addr,port)
					print("output")
					break;
		except:
			continue;
main()