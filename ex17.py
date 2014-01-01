from sys import argv
from os.path import exists
script,from_file,to_file=argv
print"copying from %s to %s"%(from_file,to_file)
in_file=open(from_file)
indata=in_file.read()
print"the ip file is %d bytes long"%len(indata)
print"does the op file exists?%r"%exists(to_file)
print"ready,hit return to continue,ctrl+c to abort."
raw_input()
out_file=open(to_file,'w')
out_file.write(indata)
print"alright.done."
out_file.close()
in_file.close()
