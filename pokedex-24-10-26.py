pokedex = {
    "charizard":{
        "Element":"Fire",
        "Hp":80,
        "Power":100
    },
    "pikachu":{
        "Element":"Electricity",
        "Hp":60,
        "Power":90
    },
    "mewtwo":{
        "Element":"Phychic",
        "Hp":100,
        "Power":100
    },
    "eevee":{
        "Element":"Normal",
        "Hp":50,
        "Power":50
    },
    "dragonite":{
        "Element":"Dragon",
        "Hp":90,
        "Power":100
    },
}
action=input("What pokemon would you like to search?(stop to quit)").lower()
while action != 'stop':
    if action in pokedex:
        print("---",action,"'s stats ---")
        print(pokedex[action])
    else:
        print("Sorry thats not in my dictionary, try something else!")
    action=input("What pokemon would you like to search?(stop to quit)").lower()