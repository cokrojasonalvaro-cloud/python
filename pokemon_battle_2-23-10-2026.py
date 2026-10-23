pokemon = [
    "Bulbalsaur", "Charmander", "Squirtle",
    "Ivysaur","Charmeleon", "Wartortle", 
    "Venusaur", "Charizard", "Blastoise"
]
latias_health =60
latios_health =60
weapon = input("Which pokemon would you like to pick?\n1-Basic\n2-Advance\n3-Master")
if weapon =='1':
    print("You got basic pokemon=",pokemon[0:3])
    piu = pokemon[0:3]

if weapon =='2':
    print("You got advance pokemon=",pokemon[3:6])
    print("You got basic pokemon=",pokemon[0:3])
    piu = pokemon[3:6]
    
if weapon =='3':
    print("You got master pokemon=",pokemon[6:])
    piu = pokemon[6:9]

while latias_health>0 or latios_health>0:
    print("---Latias health:",latias_health,"---latios health:",latios_health,"---")
    which = input("Which one would you like to attack?\n1-latias\n2-Latios")
    print("Which pokemon would you like to attack with?")
    for i in range (0,3):
            print(i+1,'.',piu[i])
    att = input()
    if which=='1' and att=='1':
        latias_health-=15
    elif which=='1' and att=='2':
        latias_health-=25
    elif which=='1' and att=='3':
        latias_health-=35
    elif which=='2' and att=='1':
        latios_health-=15
    elif which=='2' and att=='2':
        latios_health-=25
    elif which=='2' and att=='3':
        latios_health-=35
print("Congrats you won")
            
         
        