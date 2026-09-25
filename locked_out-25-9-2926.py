items = []
print("You are trapped in a locked room\n find the 'Golden Key' to escape")
def find():
    items.append(input("What did you find?"))
while escaped == False:
    print("items ="+items)
    do= input("\n1.Find items in the room\n2.remove all items\n3.Give up")
