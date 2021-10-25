from time import sleep
from pyfiglet import Figlet
import os

os.system('color 1f')

f = Figlet(font='ascii___')

print(f.renderText("CEHPOINT"))

def start():
    print("1. Learn Pentesting")
    print("2. Learn Bug Bounty")
    print("3. Learn Cyber Security")
    print("4. Learn Web Development")
    print("5. How To Make Money")
    c = int(input("What do you want to learn ? (reply in 1-5)  0 to exit  "))
    _ReadFunc(c)

msg = ''
def _ReadFunc(c):
    if(c==0) :
        os.system('exit')
    elif (c == 1):
        os.system('color 0a')
        msg = "pentesting"
        _TermSelect(c, msg)
    elif (c == 2):
        os.system('color 27')
        msg = "bug bounty"
        _TermSelect(c, msg)
    elif (c == 3):
        os.system('color af')
        msg = "cyber security"
        _TermSelect(c, msg)
    elif (c == 4):
        os.system('color 0f')
        msg ="Web Development"
        _TermSelect(c, msg)
    elif (c == 5):
        os.system('color 74')
        msg= "How To Make Money"
        _TermSelect(c, msg)
    else:
        print("Sorry your selection is invalid")
        sleep(2)
        start()


def _TermSelect(n, msg):
    print("\nYou have been selected "+msg)
    print("\nHow you want to learn ? ")
    print("1. Short Term")
    print("2. Long Term")
    tm = int(input("Enter your choise (1-2) "))
    if(tm==1):
        _shortTerm(n, msg)

def _ReadShort(n, day):
    if n== 1 and day==1:
        print("Day 1 \n https://learn.devsecit.com/book/pentest?day=1")
    elif n==1 and day==2:
        print("Day 2 \n https://learn.devsecit.com/book/pentest?day=2")
    elif n==1 and day==3:
        print("Day 3 \n https://learn.devsecit.com/book/pentest?day=3")
    elif n==1 and day==4:
        print("Day 4 \n https://learn.devsecit.com/book/pentest?day=4")
    elif n==1 and day==5:
        print("Day 5 \n https://learn.devsecit.com/book/pentest?day=5")
        # enter for 2nd option
    if n== 2 and day==1:
        print("Day 1 \n https://learn.devsecit.com/book/bounty?day=1")
    elif n==2 and day==2:
        print("Day 2 \n https://learn.devsecit.com/book/bounty?day=2")
    elif n==2 and day==3:
        print("Day 3 \n https://learn.devsecit.com/book/bounty?day=3")
    elif n==2 and day==4:
        print("Day 4 \n https://learn.devsecit.com/book/bounty?day=4")
    elif n==2 and day==5:
        print("Day 5 \n https://learn.devsecit.com/book/bounty?day=5")
        # enter for 3rd option
    if n== 3 and day==1:
        print("Day 1 \n https://learn.devsecit.com/book/security?day=1")
    elif n==3 and day==2:
        print("Day 2 \n https://learn.devsecit.com/book/security?day=2")
    elif n==3 and day==3:
        print("Day 3 \n https://learn.devsecit.com/book/security?day=3")
    elif n==3 and day==4:
        print("Day 4 \n https://learn.devsecit.com/book/security?day=4")
    elif n==3 and day==5:
        print("Day 5 \n https://learn.devsecit.com/book/security?day=5")
        # enter for 4th option
    if n== 4 and day==1:
        print("Day 1 \n https://learn.devsecit.com/book/development?day=1")
    elif n==4 and day==2:
        print("Day 2 \n https://learn.devsecit.com/book/development?day=2")
    elif n==4 and day==3:
        print("Day 3 \n https://learn.devsecit.com/book/development?day=3")
    elif n==4 and day==4:
        print("Day 4 \n https://learn.devsecit.com/book/development?day=4")
    elif n==4 and day==5:
        print("Day 5 \n https://learn.devsecit.com/book/development?day=5")
        # enter for 5th option
    if n== 5 and day==1:
        print("Day 1 \n https://learn.devsecit.com/book/money?day=1")
    elif n==5 and day==2:
        print("Day 2 \n https://learn.devsecit.com/book/money?day=2")
    elif n==5 and day==3:
        print("Day 3 \n https://learn.devsecit.com/book/money?day=3")
    elif n==5 and day==4:
        print("Day 4 \n https://learn.devsecit.com/book/money?day=4")
    elif n==5 and day==5:
        print("Day 5 \n https://learn.devsecit.com/book/money?day=5")

    conf= input("\nDo you want to read next ? (y/n)")
    if conf=='y' :
        if day<5:
            _ReadShort(n, day+1)
        else:
            print("You have read all pages.Thanks ")
    else:
        print("Thank you for use our E-Learning bot. Visit again")
        print(f.renderText("CEHPOINT"))


def _shortTerm(n,msg):
    print("\n\n")
    print(f.renderText(msg))
    print("\nChoose class day")
    print("1. Day 1 ")
    print("2. Day 2 ")
    print("3. Day 3 ")
    print("4. Day 4 ")
    print("5. Day 5 ")

    day = int(input("Select in 1-5 "))
    _ReadShort(n, day)

start()