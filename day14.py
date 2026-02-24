import day14gamedata
import random
import day14logo

indexa = random.randint(0,50)
indexb = random.randint(0,50)
score = 0
while indexb == indexa:
    indexb = random.randint(0, 50)

while True:
    print("Compare A: "+day14gamedata.data[indexa]["name"]+ ", " + day14gamedata.data[indexa]["description"] +", " + day14gamedata.data[indexa]["country"])
    print(day14logo.vs)
    print("Against B: "+day14gamedata.data[indexb]["name"]+ ", " + day14gamedata.data[indexb]["description"] +", " + day14gamedata.data[indexb]["country"])

    followerA = day14gamedata.data[indexa]["follower_count"]
    followerB = day14gamedata.data[indexb]["follower_count"]
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if (choice == 'A' and followerA > followerB) or (choice == 'B' and followerB > followerA):
        score += 1
        print(f"You are right! Current score: {score}")
        indexa = indexb
        indexb = random.randint(0, 50)
    else:
        print(f"You lose. Final score: {score}")
        break