import random
when = ["last year", "last month", "last week", "yesterday"]
who = ["a pilot", "a clown", "a panda", "a chicken"]
name = ["Jaden", "Caden", "Clayton", "Messi"]
what = ["fell asleep", "Cooked dimsum", "Studied physics", "Played fortnite"]
where = ["japan", "Shangahai", "Dufan", "Starbucks", "New york"]
rsg = random.choice(when)+', '+random.choice(who)+" named "+random.choice(name)+' '+random.choice(what)+" in "+random.choice(where)+'.'
print(rsg)