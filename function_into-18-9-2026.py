#def bmi(berat, tinggi):
#    b = berat/(tinggi*tinggi)
#    print(b)
#bmi(70,1.8)

hunger = 5
happiness = 5
energy = 5
hours_survived = 1

def eat():
    hunger +=2
    energy -= 1

def play():
    happiness +=3
    hunger -= 1
    energy -= 1

def sleep():
    energy+=2
    hunger -= 1
    happiness -= 1

def welcome():
    print("\n--- Hour:",hours_survived,"---")
    print(f"Hunger 😋 : {hunger} | Happiness 😊 : {happiness} | energy 🪫 : {energy}")

print("Welcome to Spocky, Every hour you need to take care of him, Raise him as long as possible") 
while hunger>0 and happiness>0  and energy>0:
    welcome()
    action = input("Which action do you want to do?\n1.Eat(+2 hunger, -1 energy)\n2.Play(+3 happiness, -1 hunger, -1, energy)\n3.Sleep(+2 energy, -1 hunger, -1 happiness)")
    if action == '1':
        eat()
    elif action =='2':
        play()
    elif action =='3':
        sleep()
    hours_survived +=1
print("Congrats, you survived:",hours_survived-1,"hours")

