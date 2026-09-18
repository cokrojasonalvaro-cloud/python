credit = 50
days_survived = 1
food = 10
oxygen = 10

print("Welcome to space commander, Survive 10 days to win")
while oxygen>0 and food> 0 and days_survived<=10:
    print("\n---Day:", days_survived,"---")
    print(f"💰 Credits: {credit} | 🌬️ Oxygen: {oxygen} | 🍎 Food: {food}")
    action = input("What action do you want to do?\n1.Buy oxygen(credit - 10,oxygen + 5)\n2.Buy Food(credit - 10,food + 5)\n3.Do nothing(credit +5)")
    if action =='1':
        credit -= 10
        oxygen +=5
    elif action =='2':
        credit -= 10
        food +=5
    elif action =='3':
        credit +=5
    days_survived +=1
    food -=2
    oxygen -=2
if oxygen<1 or food< 1:
    print("you failed, try again!")
elif days_survived > 10:
    print("Congrats you win!")
