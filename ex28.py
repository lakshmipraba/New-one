from sys import exit
def gold_room():
 print"this room is full of gold.how much do u take?"
 next=raw_input(">")
 if"0" in next or "1" in next:
   how_much=int(next)
 else:
   dead("man learn to type a number")
 if how_much<50:
   print"nice,u win"
   exit(0)
 else: 
   dead("u r bad")
def bear_room():
 print"there is bear here"
 print"it has bunch of honey"
 print"it infront of another door"
 print"how u going to move the bear?"
 bear_moved= False
 while True:
  next=raw_input(">")
  if next=="take honey":
   dead("the bear looks at you then slaps your face off.")
  elif next=="taunt bear" and not bear_moved:
   print"it moved frm the door.u can go through it now."
   bear_moved=True
  elif next=="taunt bear" and bear_moved:
   dead("the bear gets pissed off and chews ur leg off.")
  elif next== "open door" and bear_moved:
   gold_room()
  else:
   print"no idea"
def cthulhu_room():
 print"here u see the evil cthulhu."
 print"he is whatever stares at u and u go insane"
 print"do u flee for ur life or eat ur head?"
 next=raw_input(">")
 if "flee"in next:
  start()
 elif"head" in next:
  dead("well that was tasty")
 else:
  cthulhu_room()
def dead(why):
 print why,"good job"
 exit(0)
def start():
 print"u r in a dark room."
 print" there is a door to ur right and left"
 print"which one do u take?"
 next=raw_input(">")
 if "left" in next:
  bear_room()
 elif"right" in next:
  cthulhu_room()
 else:
  dead("u dead")
start()  
  
