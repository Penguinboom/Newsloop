import time
import random
import math
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
plays=savedataplay.read()
savedataplay.close()
def game():
    panik=10
    plays=plays+1
    if 7<plays>5:
        print("The loop It's sickeni")
    input("Press Enter to start...")
    time.sleep(3)
    if plays>3 and Balance<-3:
        print("Everny time you comge he")
    print("To complete the game you must become the leading news broadcaster:")
    print("At random intervals you will need to select what event you want to report on good luck")
    if plays>10:
        print("Just leave we beeg of ryuo")
    viewers=random.randint(200,750)
    reports=["Fire man saves cat stuck on tree","Supply issues cause prices to rise"]
    reports[1]="Fire man saves cat stuck on tree"
    reports[-1]="Supply issues cause prices to rise"
    while viewers<random.randint(1000000,6350000)*plays:
        time.sleep(random.randint(6,20))
        Choice1=random.choice(reports)
        Choice2=random.choice(reports)
        Choice3=random.choice(reports)
        answer=int(input("1.",Choice1,"2.",Choice2,"3.",Choice3))
        if answer == 1:
            Balance=Balance+reports.index(Choice1)
            answer=Choice1
        elif answer == 2:
            Balance=Balance+reports.index(Choice2)
            answer=Choice2
        elif answer == 3:
            Balance=Balance+reports.index(Choice3)
            answer=Choice3
        if reports.index(answer)>0:
            panik=panik+reports.index(answer)*2
            viewers=viewers+random.randint(10*1+Balance,-10*1+Balance)
        if reports.index(answer)<=0:
            viewers=viewers+random.randint(10*1+-Balance,50*1+-Balance)
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