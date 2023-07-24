import random


def rolldice():
    return random.randint(1,6)
print("welcome to the game of rolling dice..")
flag=1

while(flag==1):
    input("press enter to roll the Dice")
    output=rolldice()
    print(f"the rolled dice number is  {output}!")
    flag=int(input("do u want to play again ------ if yes then press 1 if not press 0:  "))
    if flag==0:
        print("thanks for playing this game -- goodbye!!")
        break
