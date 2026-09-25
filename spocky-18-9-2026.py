hunger = 5
happiness = 5
energy = 5
hours_survived = 1

print("Welcome to Spocky, Every hour you need to take care of him, Raise him as long as possible") 
while hunger>0 and happiness>0  and energy>0:
    print("\n--- Hour:",hours_survived,"---")
    print(f"Hunger 😋 : {hunger} | Happiness 😊 : {happiness} | energy 🪫 : {energy}")
    action = input("Which action do you want to do?\n1.Eat(+2 hunger, -1 energy)\n2.Play(+3 happiness, -1 hunger, -1, energy)\n3.Sleep(+2 energy, -1 hunger, -1 happiness)")
    if action == '1':
        hunger +=2
        energy -= 1
    elif action =='2':
        happiness +=3
        hunger -= 1
        energy -= 1
    elif action =='3':
        energy+=2
        hunger -= 1
        happiness -= 1
    hours_survived +=1
print("Congrats, you survived:",hours_survived-1,"hours")

