from sys import argv
script,user_name=argv
prompt='*'
print"hi %s, i'm the %s script."%(user_name,script)
print"i would like to ask you a few questions."
print"do u lik me%s?"%user_name
likes=raw_input(prompt)
print"where do u live %s?"%user_name
lives=raw_input(prompt)
print"wat kind of computer u hav %s?"%user_name
computer=raw_input(prompt)
print"""%r%r%r"""%(likes,lives,computer)
