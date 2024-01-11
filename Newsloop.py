import time
import random
import math
global Balance
Balance=int
int: Balance=0
input("Press Enter to start...")
time.sleep(3)
print("To complete the game you must become the leading news broadcaster:")
print("At random intervals you will need to select what event you want to report on good luck")
global viewers
viewers=random.randint(200,750)
global reports
reports=["Fire man saves cat stuck on tree","Supply issues cause prices to rise",]
reports[1]="Fire man saves cat stuck on tree"
reports[3]="Supply issues cause prices to rise"
while viewers<random.randint(1000000,6350000):
    time.sleep(random.randint(3,10))
    Choice1=random.choice(reports[1])
    Choice2=random.choice(reports[2])
    Choice3=random.choice(reports)
    Report=[Choice1, Choice2, Choice3]
    global answer
    answer=input(Report)
    if answer==1:
        answer=1
    if answer==2:
        answer=2
    if answer==3:
        answer=3 
    answer=int
    viewers=viewers+random.randint(10,30)*answer
    print("Your story was watched by ", viewers," people.")
    if Balance==-1:
        reports[2]="Robbery at Local Bank"
        reports[2]="Man Killed by Local Police"
        reports[2]="Woman Killed by Local Police"
    if Balance==1:
        reports[2]="Celebrity suprises, Local Kid with Cancer"
    if Balance==-2:
        reports[3]="Shelves empty due to supply chain issues"
        reports[3]="Unprecedented reports of hospitalizations due to the flu."
    if Balance==2:
        reports[3]="Donations to The Red Cross have drasticly increased"
        reports[3]="New road has been constructed"
    if Balance==-3:
        reports[4]="Crime rates have increased drasticly."
        reports[4]="New illegal drug has been discovered by local authorities"
        reports[4]="Shooter kills 5 people at Local High School"
        reports[4]="Reported sightings of aliens replacing humans"