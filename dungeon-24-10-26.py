dict = {
    "north":{"Location":"Dragon's den",
             "Description":"There's a sleeping dragon",
             "suggestion":"Go south!"},
    "south":{"Location":"hallway",
             "Description":"Its a dark and spooky hallway!",
             "suggestion":"Go north!"},
    "east":{"Location":"treasure room",
             "Description":"The room is filled with valuables and gold coins!",
             "suggestion":"Go west!"},
    "west":{"Location":"monster room",
             "Description":"Zombies are all over the room!",
             "suggestion":"Go east!"},
    "middle room":{"Location":"nothing here",
                    "Description":"There's nothing here",
                    "suggestion":"Go north, south, east or west!"}
    }
n=0
e=0
explored = []
while True:
    direction = input("Welcome to the Dungeon, go any direction\n1.north\n2.south\n3.east\n4.west")
    if direction =='1':
        if n<1 and e==0:
            n+=1
            if n==0:
                print(dict["middle room"])
            elif n==1:
                print(dict["north"])
                explored.append("north")
                
        else:
            print("sorry, you cant go to that direction, try another direction")
    elif direction =='2':
        if n>-1 and e ==0:
            n-=1
            if n==0:
                print(dict["middle room"])
            elif n==-1:
                print(dict["south"])
                explored.append("south")
        else:
            print("sorry, you cant go to that direction, try another direction")
    elif direction =='3':
        if e<1 and n==0:
            e+=1
            if e==0:
                print(dict["middle room"])
            elif e==1:
                print(dict["east"])
                explored.append("east")
        else:
            print("sorry, you cant go to that direction, try another direction")
    elif direction =='4':
        if e>-1 and n==0:
            e-=1
            if e==0:
                print(dict["middle room"])
            elif e==-1:
                print(dict["west"])
                explored.append("west")
        else:
            print("sorry, you cant go to that direction, try another direction")
    if "west" in explored and "east" in explored and "north" in explored and "south" in explored:
        print("congrats you explored all the rooms")
        break
    elif direction == "stop":
        break
    else:
        print("We couldnt recognised that direction, try again")

