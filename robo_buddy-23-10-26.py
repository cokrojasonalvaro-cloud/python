dict = {
    "joke":"How does the ocean say hi? It waves!",
    "pun":"I don't trust stairs because they're always up to something.",
    "fact":"A cloud weighs around a million tonnes."
}
while True:
    print("Hi, im robo buddy, would you like a pun,a joke or fact")
    action = input()
    if action in dict:
        print(dict[action])
    elif action =='bye':
        print("bye!")
        break
    else:
        print("That's mot in my dictionary, try something else")