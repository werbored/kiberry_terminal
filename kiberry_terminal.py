from datetime import datetime
from colorama import Fore, Back, init
from os import name, system, get_terminal_size, getlogin
from time import sleep

openexc = open("termconfig.kbr") # open config read
readopenexc = openexc.read() # execute config read

schp = "" # define primary
schs = "" # define secondary
scht = "" # define tertiary
 
exec(readopenexc) # execute python script ver

system("mode 67,30") # change cmd size

kiboverrides = ["restart", "exit"]

asca = schp+" ▄▀▀▄ █  ▄▀▀█▀▄    ▄▀▀█▄▄  "+schs+" ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄ "
ascb = schp+"█  █ ▄▀ █   █  █  ▐ ▄▀   █ "+schs+"▐  ▄▀   ▐ █   █   █ █   █   █ █   ▀▄ ▄▀ "
ascc = schp+"▐  █▀▄  ▐   █  ▐    █▄▄▄▀  "+schs+"  █▄▄▄▄▄  ▐  █▀▀█▀  ▐  █▀▀█▀  ▐     █   "
ascd = schp+"  █   █     █       █   █  "+schs+"  █    ▌   ▄▀    █   ▄▀    █        █   "
asce = schp+"▄▀   █   ▄▀▀▀▀▀▄   ▄▀▄▄▄▀  "+schs+" ▄▀▄▄▄▄   █     █   █     █       ▄▀    "
ascf = schp+"█    ▐  █       █ █    ▐   "+schs+" █    ▐   ▐     ▐   ▐     ▐       █     "
ascg = schp+"▐       ▐       ▐ ▐        "+schs+" ▐                                ▐     "

ascwtc = "\n"+asca+ascb+ascc+ascd+asce+ascf+ascg # join multilines

def clear(): # clear cmd
    if name == "nt":
        system("cls")
    else:
        system("clear")

init() # initialize colorama

def display(): # show ascii and clear cmd
    clear()
    print(ascwtc)
    timeeeee = datetime.now()
    timeformat = timeeeee.strftime(schp+"%H:"+schs+"%M:%S")
    print("\n"+scht+"Welcome, "+schs+str(getlogin())+schp+"@"+schs+"kiberry"+scht+",")
    print(scht+"The time is: "+schs+timeformat+scht+","+schp+"\n")

def action():
    actinp = input("-----> ")
    if str(actinp) == "cls":
        doall()
    else:
        system(str(actinp))

def doall():
    display()
    action()

display()

while True:
    action()