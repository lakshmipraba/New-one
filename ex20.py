from sys import argv
script,ipf=argv
def print_all(f):
 print f.read()
def rewind(f):
 f.seek(0)
def pal(lc,f):
 print lc,f.readline()
cf=open(ipf)
print "1'st let's print the whole file:\n"
print_all(cf)
print "1'st let's rewind of like a tabe."
rewind(cf)
print"let's print 3 lnes"
cl=1
pal(cl,cf)
cl=2
pal(cl,cf)
cl=3
pal(cl,cf)
