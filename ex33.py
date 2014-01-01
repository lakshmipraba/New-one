from sys import argv
script,filename=argv
print"we r going to erase  %r:"%filename
print "if u dn't want that,hit ctrl+c (c^)."
print"if u want do that,hit RETURN."
raw_input("?")
print"opening the file.."
target=open(filename,'w+')
print"now i'm gping to ask u for 3 lines."
l1=raw_input("l1:")
l2=raw_input("l2")
l3=raw_input("l3")
print"i'm going to write these to the file."
target.write(l1)
target.write("\n")
target.write(l2)
target.write("\n")
target.write(l3)
target.write("\n")
print"finally read it"
print target.read()

