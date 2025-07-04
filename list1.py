justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]

#number of members in justice league
print(len(justice_league))

#adding new member to justice league
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("updated list",justice_league)

#moving wonder women to beginning
justice_league.remove("WonderWoman")
justice_league.insert(0,"WonderWoman") #assigning 0 index to the wonder woman for adding at start
print("updated list",justice_league)

#adding superman in between aquaman and flash
justice_league.remove("Superman")
justice_league.insert(3,"Superman") 
print("updated list",justice_league)

#replacing the list
justice_league = ["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
print("new justice league is",justice_league)

#sorting the list alphabetically
justice_league.sort()
print("sorted justice league is",justice_league)

#predicting new leader
print("the new leader of justice league is",justice_league[0])



