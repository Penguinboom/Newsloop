import keyboard
import time
import random
import math
a=1
Balance=0
SavedataB = open("Scale_Var.txt","r")
Balance=SavedataB.read()
SavedataB.close()
savedatapeace = open("Zen_Var.txt","r")
peace=savedatapeace.read()
savedatapeace.close()
savedatachaos = open("Khorne_Var.txt","r")
Chaos=savedatachaos.read()
savedataplay = open("Times_Played.txt","r")
plays=savedataplay
savedataplay.close()
asphalt=open("Answer", "r")
asphalt.close()
viewers=random.randint(200,750)
def game():
    panik=10
    input("Press Enter to start...")
    time.sleep(3)
    print("To complete the game you must become the leading news broadcaster:")
    print("At random intervals you will need to select what event you want to report on good luck")
    reports=["Fire man saves cat stuck on tree","Supply issues cause prices to rise","Gas prices rise"]
    reports[1]="Fire man saves cat stuck on tree"
    reports[-1]="Supply issues cause prices to rise"
    reports[-1]="Gas prices rise"
    while viewers<random.randint(1000000,6350000):
        time.sleep(random.randint(6,20))
        Choice1=random.choice(reports)
        Choice2=random.choice(reports)
        Choice3=random.choice(reports)
        print("1.",Choice1,"2.",Choice2,"3.",Choice3)
        answer=input()
        if answer == 1:
            Balance=Balance+reports.index(Choice1)
            answer=Choice1
            asphalt=open("Answer", "w")
            asphalt.write(answer)
            asphalt.close()
        elif answer == 2:
            answer=Choice2
            asphalt=open("Answer", "w")
            asphalt.write(answer)
            asphalt.close()
        elif answer == 3:
            answer=Choice3
            asphalt=open("Answer", "w")
            asphalt.write(answer)
            asphalt.close() 
        Balance=Balance+asphalt.read()        
        viewers=viewers+random.randint(20,86)
        print("Your story was watched by ", viewers," people.")
        if Balance ==-2:
            reports[-2]="Robbery at Local Bank"
            reports[-2]="Man Killed by Local Police"
            reports[-2]="Woman Killed by Local Police"
        if Balance ==2:
            reports[2]="Celebrity suprises, Local Kid with Cancer"
        if Balance ==-3:
            reports[3]="Peacful protests arise in response to the violence caused by police"
            reports[-3]="Shelves empty due to supply chain issues"
            reports[-3]="Unprecedented reports of hospitalizations due to the flu."
        if Balance ==3:
            reports[3]="Donations to The Red Cross have drasticly increased"
            reports[3]="New road has been constructed"
        if Balance ==-4:
            reports[-4]="Crime rates have increased drasticly."
            reports[-4]="New illegal drug has been discovered by local authorities"
            reports[-4]="Shooter kills 5 people at Local High School"
            reports[-4]="Reported sightings of aliens replacing humans"
        if answer == "Peacful protests arise in response to the violence caused by police":
            reports[-4]="Police fire into a peacful protest killing 20 people."
        if panik >= 100 and answer == "Riots have spread acroos the intire country":
            print("Who knew you were such a cruel person would you do this if you knew this wasn't a game?")
        SavedataB = open("News_Game.txt","w")
        SavedataB.write(Balance)
        SavedataB.close()
        savedatachaos = open("Khorne_Var.txt","w")
        savedatachaos.write(Chaos)
        savedatachaos.close
        savedatapeace = open("Zen_Var.txt","w")
        savedatapeace.write(peace)
        savedatapeace.close
        savedataplay = open("Times_Played.txt","w")
        savedataplay.write(plays)
        savedataplay.close
    if Balance >10 and Chaos == 0:
        "You proved that you are dedicated to us you are forever in are grace"
        peace=peace+1
    if Balance >10 and Chaos >0:
        print("have you came to reedem your self or give us a false hope?")
        peace=peace+1
    if Balance <0 and peace == 0:
        print("The world has gone to chaos but at least you got the views")
        Chaos=Chaos+1
    if Balance < 0 and peace > 0:
        print("Did you get board or did this became something of the likes of undertale and you wanted all the options?")
        Chaos=Chaos+1
game()