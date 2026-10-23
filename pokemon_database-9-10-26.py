pokemon_collect = ['Pikachu','Charizard','Mew','Charmander','Snorlax']
print("Welcome to your pokemon database\nYour pokemons = ",pokemon_collect)
do = input("What would you like to do?\n1 to add\n2 to remove\n3 to replace \n4 to stop")
while do != '4':
    if do == '1':
        pokemon_collect.append(input("What pokemon would you like to add?"))
    elif do == '2':
        pokemon_collect.remove(input("What pokemon would you like to remove?"))
    elif do == '3':
        pokemon_collect.remove(input("Which pokemon would you like to remove?"))
        pokemon_collect.append(input("Which pokemon would be the replacement?"))
    elif do =='4':
        break
    print("Your pokemons = ",pokemon_collect)
    do = input("What would you like to do?\n1 to add\n2 to remove\n3 to replace \n4 to stop\n")
