import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import random
from PyProbs import Probability as pr

###############################################################################
########################DEFINITION OF NEEDED VARIABLES#########################
###############################################################################

#Lambdas for the poission distribution
lamT_c12 = 4
lamL_c1  = 2
lamL_c2  = 4

#Mean exponential distribution tenants and c1 and c2
mT   = 1/lamT_c12
mLc1 = 1/lamL_c1

#mean waiting time
mWaiting = 10

#Maximum time of simulation (iterations)
expLength = 1500

#Matching probabilities in c2 there is no probability for c1 since it is a fcfs system
pc2 = 15

###############################################################################
##############################START OF MAIN SYMULATION#########################
###############################################################################

leftAgents = {}

C1houses        = []
C2houses        = []
allAgents       = []
stayedC1        = []
stayedC2        = []
leftMarket      = []
searchingAgents = [] 

dLeftArrivedT   = []
dSearching      = []
dc2TookArrivedT = []
dc1TookArrivedT = []

waitingTimeC2F  = []
waitingTimeC2L  = []
waitingTimeC2A  = []

waitingTimeC1F  = []
waitingTimeC1L  = []
waitingTimeC1A  = []

waitingTimeTF   = []
waitingTimeTL   = []
waitingTimeTA   = []

C1houses.append(0)
C2houses.append(0)
stayedC1.append(0)
stayedC2.append(0)
allAgents.append(0)
searchingAgents.append(0)
leftMarket.append(0)

dc1TookArrivedT.append(0)
dc2TookArrivedT.append(0)
dLeftArrivedT.append(0)
dSearching.append(0)

waitingTimeC1A.append(0)
waitingTimeC1F.append(0)
waitingTimeC1L.append(0)

waitingTimeC2A.append(0)
waitingTimeC2F.append(0)
waitingTimeC2L.append(0)

waitingTimeTF.append(0)
waitingTimeTL.append(0)
waitingTimeTA.append(0)

lT = []
lT.append(0)
i = 1
while i <= (lamL_c2 + 0.1):
    ####################
    ###Def. Variables###
    ####################
    #First come first serve queue for category 1
    FCFS_C1 = []

    #Houses in c2 and c1 available
    residences_c1 = []
    residences_c2 = []

    #Dictionary with the tenannts
    tenants = {}

    #Dictionary with the tenannts
    landlordsc1 = {}
    landlordsc2 = {}

    ####################
    ####Inicializing####
    ####################
    #Tennants arrival times
    arrivalTimesTenants = []
    timePassed = 0
    while timePassed < expLength:
        x = random.exponential(scale=mT)
        timePassed += x
        arrivalTimesTenants.append(int(timePassed))

    #Landlords C1 arrival times
    arrivalTimesLandlordsC1 = []
    timePassed = 0
    while timePassed < expLength:
        x = random.exponential(scale=mLc1)
        timePassed += x
        arrivalTimesLandlordsC1.append(int(timePassed))


    #Landlords C2 arrival times
    arrivalTimesLandlordsC2 = []
    timePassed = 0
    mLc2 = 1/i
    while timePassed < expLength:
        x = random.exponential(scale=mLc2)
        timePassed += x
        arrivalTimesLandlordsC2.append(int(timePassed))

    #Time Variable and tenant landlord cq and landlord c2 special identificator
    t     = 0
    tID   = 0
    lc1ID = 0
    lc2ID = 0

    arrivedTotal    = 0
    dLeftTheMarket  = 0
    dFoundC2        = 0
    dFoundC1        = 0

    #Starting of the iterations
    while t <= expLength:
        arrived = 0
        #adding the new tenants to the market according to exponential distribution and its poission distribution
        for x in arrivalTimesTenants:
            if x == t:
                agent = {
                    "arrival"   : t,
                    "found"     : False,
                    "category"  : "empty",
                    "waitingT"  : 0,
                    "maxWait"   : random.exponential(scale=mWaiting),
                    "offers"    : {},
                    "left"      : False
                }
                tenants.update({tID : agent})
                arrived += 1
                arrivedTotal += 1

                #mathing with all houses in c2
                for x in residences_c2:
                    if pr.Prob(pc2/100) and not agent["found"] and not agent["left"]:
                        agent["offers"].update({x : "C2"})

                #checks if he is the first in fcfs and if there is a house gives it to the agent
                if len (FCFS_C1) == 0 and len(residences_c1) > 0:
                    tenants[tID]["found"]    = True
                    tenants[tID]["category"] = "C1"
                    landlordID = residences_c1[0]
                    landlordsc1[landlordID]["found"] = True
                    del residences_c1[0]
                    dFoundC1 += 1
                else:
                    FCFS_C1.append(tID)

                tID  += 1
            else:
                continue     

        #adding new houese to market from c1 according to its corresponding poission process
        for x in arrivalTimesLandlordsC1:
            if x == t:
                agent = {
                    "arrival"   : t,
                    "found"     : False,
                    "waitingT"  : 0,
                    "left"      : False
                }
                landlordsc1.update({lc1ID : agent})
                residences_c1.append(lc1ID)

                #match the new house to first tenants in fcfs
                #if someone in queue takes it off and gives the house
                #checks if the agent already took other option
                # and if he dies it take of list
                takeOf = []
                for x in FCFS_C1:
                    if not tenants[x]["found"] and not tenants[x]["left"]:
                        tenants[x]["found"]    = True
                        tenants[x]["category"] = "C1"
                        landlordID = residences_c1[0]
                        landlordsc1[landlordID]["found"] = True
                        del residences_c1[0]
                        takeOf.append(x)
                        dFoundC1 += 1
                        break
                    else: #already has accomodation, take of fcfs
                        takeOf.append(x)

                for x in takeOf:
                    FCFS_C1.remove(x)

                lc1ID += 1
            else:
                continue

        #adding new houese to market from c2 according to poission process
        for x in arrivalTimesLandlordsC2:
            if x == t:
                agent = {
                    "arrival"   : t,
                    "found"     : False,
                    "waitingT"  : 0,
                    "left"      : False
                }
                landlordsc2.update({lc2ID : agent})
                residences_c2.append(lc2ID)

                #match the new house to all tenants searching
                for key, agnt in tenants.items():
                    #agent gets matched, is searching for accomodation and hasnt perished
                    if pr.Prob(pc2/100) and not agnt["found"] and not agnt["left"]:
                        agnt["offers"].update({lc2ID : "C2"})

                lc2ID += 1
            else:
                continue

        #increments time variable of agents and if greater than maxWait the agent leaves 
        #the market or tries to take a house from its list that isnt taken yet
        for ID, agnt in tenants.items():
            if agnt["waitingT"] >= agnt["maxWait"] and not agnt["left"] and not agnt["found"]: #last chance

                #one last time matching if agent cant find anything leaves market
                found = False
                for ID, category in agnt["offers"].items():
                    if category == "C2" and len(residences_c2) > 0 and ID in residences_c2 and not landlordsc2[ID]["found"]:
                        residences_c2.remove(ID)
                        landlordsc2[ID]["found"] = True
                        agnt["found"] = True
                        found = True
                        dFoundC2 += 1
                        break
                    elif category == "C3": #implement in the furure
                        continue
                
                if not found:
                    leftAgents.update({ID : agnt})
                    agnt["left"] = True
                    dLeftTheMarket += 1

            elif not agnt["found"] and not agnt["left"]: #still searching just increment time
                agnt["waitingT"] += 1

            else: #already found accomodation
                continue
        
        for ID, agnt in landlordsc1.items():
           if not agnt["found"]:
               agnt["waitingT"] += 1

        for ID, agnt in landlordsc2.items():
            if not agnt["found"]:
               agnt["waitingT"] += 1

        t += 1

    sumWaitC1L   = 0
    sumWaitC1F   = 0
    agntsFoundC1 = 0
    agntsLeftC1  = 0
    for ID, agnt in landlordsc1.items():
        if agnt["found"]:
            sumWaitC1F   += agnt["waitingT"]
            agntsFoundC1 += 1
        else:
            sumWaitC1L   += agnt["waitingT"]
            agntsLeftC1  += 1

    stayedC1.append(agntsFoundC1)

    sumWaitC2L   = 0
    sumWaitC2F   = 0
    agntsFoundC2 = 0
    agntsLeftC2  = 0
    for ID, agnt in landlordsc2.items():
        if agnt["found"]:
            sumWaitC2F   += agnt["waitingT"]
            agntsFoundC2 += 1
        else:
            sumWaitC2L   += agnt["waitingT"]
            agntsLeftC2  += 1
    
    stayedC2.append(agntsFoundC2)

    sumWaitTL   = 0
    sumWaitTF   = 0
    agntsFoundT = 0
    agntsLeftT  = 0
    for ID, agnt in tenants.items():
        if agnt["found"]:
            sumWaitTF   += agnt["waitingT"]
            agntsFoundT += 1
        else:
            sumWaitTL   += agnt["waitingT"]
            agntsLeftT  += 1

    print(i)
    lT.append(i)

    leftMarket.append(dLeftTheMarket)
    dc1TookArrivedT.append(dFoundC1/(arrivedTotal/1.0))
    dc2TookArrivedT.append(dFoundC2/(arrivedTotal/1.0))
    dLeftArrivedT.append(dLeftTheMarket/(arrivedTotal/1.0))
    dSearching.append((arrivedTotal-dFoundC1-dFoundC2-dLeftTheMarket)/(arrivedTotal/1.0))
    searchingAgents.append(arrivedTotal-dFoundC1-dFoundC2-dLeftTheMarket)
    allAgents.append(arrivedTotal)
    C1houses.append(len(landlordsc1))
    C2houses.append(len(landlordsc2))

    if sumWaitC1F == 0 and sumWaitC1L == 0:
        waitingTimeC1A.append(0)
        waitingTimeC1F.append(0)
        waitingTimeC1L.append(0)
    elif sumWaitC1F > 0 and sumWaitC1L == 0:
        waitingTimeC1A.append(sumWaitC1F/(agntsFoundC1/1.0))
        waitingTimeC1F.append(sumWaitC1F/(agntsFoundC1/1.0))
        waitingTimeC1L.append(0)
    elif sumWaitC1F == 0 and sumWaitC2L > 0:
        waitingTimeC1A.append(sumWaitC1L/(agntsLeftC1/1.0))
        waitingTimeC1F.append(0)
        waitingTimeC1L.append(sumWaitC1L/(agntsLeftC1/1.0))
    else:
        waitingTimeC1A.append((sumWaitC1F+sumWaitC1L)/((agntsFoundC1+agntsLeftC1)/1.0))
        waitingTimeC1F.append(sumWaitC1F/(agntsFoundC1/1.0))
        waitingTimeC1L.append(sumWaitC1L/(agntsLeftC1/1.0))

    if sumWaitC2F == 0 and sumWaitC2L == 0:
        waitingTimeC2A.append(0)
        waitingTimeC2F.append(0)
        waitingTimeC2L.append(0)
    elif sumWaitC2F > 0 and sumWaitC2L == 0:
        waitingTimeC2A.append(sumWaitC2F/(agntsFoundC2/1.0))
        waitingTimeC2F.append(sumWaitC2F/(agntsFoundC2/1.0))
        waitingTimeC2L.append(0)
    elif sumWaitC2F == 0 and sumWaitC2L > 0:
        waitingTimeC2A.append(sumWaitC2L/(agntsLeftC2/1.0))
        waitingTimeC2F.append(0)
        waitingTimeC2L.append(sumWaitC2L/(agntsLeftC2/1.0))
    else:
        waitingTimeC2A.append((sumWaitC2F+sumWaitC2L)/((agntsFoundC2+agntsLeftC2)/1.0))
        waitingTimeC2F.append(sumWaitC2F/(agntsFoundC2/1.0))
        waitingTimeC2L.append(sumWaitC2L/(agntsLeftC2/1.0))

    if sumWaitTF == 0 and sumWaitTL == 0:
        waitingTimeTA.append(0)
        waitingTimeTF.append(0)
        waitingTimeTL.append(0)
    elif sumWaitTF > 0 and sumWaitTL == 0:
        waitingTimeTA.append(sumWaitTF/(agntsFoundT/1.0))
        waitingTimeTF.append(sumWaitTF/(agntsFoundT/1.0))
        waitingTimeTL.append(0)
    elif sumWaitTF == 0 and sumWaitTL > 0:
        waitingTimeTA.append(sumWaitTL/(agntsLeftT/1.0))
        waitingTimeTF.append(0)
        waitingTimeTL.append(sumWaitTL/(agntsLeftT/1.0))
    else:
        waitingTimeTA.append((sumWaitTF+sumWaitTL)/((agntsLeftT+agntsFoundT)/1.0))
        waitingTimeTF.append(sumWaitTF/(agntsFoundT/1.0))
        waitingTimeTL.append(sumWaitTL/(agntsLeftT/1.0))

    i += 1    

###############################################################################
############################PLOTTING OF THE SIMULATION#########################
###############################################################################

val1 = ["{:X}".format(i) for i in range(lamL_c2+1)] 
val2 = ["Stayed C1", "Stayed C2", "Left Market", "Searching", "All Agents", "Houses C1", "Houses C2", "Ratio left", "Ratio C1", "Ratio C2", "W. Time T. All", "W. Time T. Left", "W. Time T. Found", "W. Time C1 All", "W. Time C1 Left", "W. Time C1 Found", "W. Time C2 All", "W. Time C2 Left", "W. Time C2 Found"] 
val3 = [stayedC1, stayedC2, leftMarket, searchingAgents, allAgents, C1houses, C2houses, dLeftArrivedT, dc1TookArrivedT, dc2TookArrivedT, waitingTimeTA, waitingTimeTL, waitingTimeTF, waitingTimeC1A, waitingTimeC1L, waitingTimeC1F, waitingTimeC2A, waitingTimeC2L, waitingTimeC2F ] 
   
fig, ax = plt.subplots() 
ax.set_axis_off() 
table = ax.table( 
    cellText = val3,  
    rowLabels = val2,  
    colLabels = val1, 
    rowColours =["skyblue"] * 19,  
    colColours =["skyblue"] * 19, 
    cellLoc ='center',  
    loc ='upper left')         
   
table.auto_set_font_size(False)
table.set_fontsize(12)
ax.set_title("Data after 2000 iterations over λC2 \n λTenants = " + str(lamT_c12) + " λC1 = " + str(lamL_c1) + " P = " + str(pc2) , fontweight ="bold") 

plt.show()