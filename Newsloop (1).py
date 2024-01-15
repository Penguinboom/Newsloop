import time
import random
import math
global Balance
Balance=0
input("Press Enter to start...")
time.sleep(2)
print("To complete the game you must become the leading news broadcaster:")
time.sleep(2)
global name 
print("But you can't do that without a company name so tell me, what is the name of your internationally local news network?")
name=input()
if name == "":
    name="Internationally Local News Network"
global competetor
competetor="NewsCorp"
time.sleep(2)
print("At random intervals you will need to select what event you want to report on good luck")
global viewers
viewers=random.randint(200,750)
class reports:
    instances = []
    def __init__(self, headline, body, effect,):
        self.headline = headline
        self.body = body
        self.effect = effect
        __class__.instances.append(self)
effect= float
a1= reports("Fire Fighters Save Cat", "Filler text", 1.4)
a2= reports("Bean production slows down", "Filler text", -1.45)
a3= reports("Man Charged with Crime Escapes", "Filler Text", -1.5)
a4= reports("Person Gives Money to People", "Filler Text", 1.5)
a5= reports("Sport Team, Wins Sport Game", "filler text", 1.7)
a6= reports("Person tripped due to bad side walk", "filler text", -1.75)
global preevent
preevent= a6
time.sleep(2)
while 1<2:
    viewers=viewers
    randIndex = random.randrange(len(reports.instances))
    randreport = reports.instances[randIndex]
    global event
    events =randreport    
    if not events==preevent:
        print("Boss, we found out that ", events.headline, "Do you like it? (y or n)")
        answer=input()
        proceed="y" or "Y" 
        if answer==proceed:
            viewers += round(random.randint(10,50)*abs(events.effect)) 
            Balance +=(events.effect) 
            print("Your story was watched by ", viewers," people.")
            print(Balance)
            if viewers >=1000:
                global Competition
                Competition=randreport
                print("Hey Boss ", competetor, "realesed an article about ", Competition.headline)
                viewers -= round(random.randint(10,30)*abs(Competition.effect))
        else:
            print("Sorry boss we'll try and find something else")
        preevent=events
    time.sleep(random.randint(2,5))
    if Balance <= -6:
        a7= reports("Bean Prices Rise", "Filler Text", -2)
        a8= reports("Crime Commited by cat", "filler text", -1.9)
        a9= reports("Man Charged with Crime helps Person", "Filler Text", 1.75)
    if Balance >= 6:
        a10= reports("Donations increase", "filler text", 1.9)
        a11= reports("Cat goes to Charity event","filler text", 2.3)
        a12= ("Local Sport Team Losses Sport Game", "filler text", -1.7)
    