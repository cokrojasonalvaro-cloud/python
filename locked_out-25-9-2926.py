items = []
print("You are trapped in a locked room\n find the 'Golden key' to escape")
def find():
    items.append(input("What did you find?"))
escaped  = False
while escaped == False:
    print("items =",items)
    do= input("What do you wan to do ?\n1.Find items in the room\n2.remove all items\n3.Give up")
    if do =='1':
        items.append(input("What item did you find?"))
    elif do == '2':
        items.clear()
    elif do =='3':
        print("You gave up")
        break
    
    if "Golden key"in items:
        print("congats you escaped")
        escaped = True
    

