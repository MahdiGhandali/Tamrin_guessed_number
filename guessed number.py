import random
number=(random.randint(1,10000))
playername=input("Hello what is your name?")
print("okay!", playername, "im gussing a number between 1 and 10000")
s=0
while True:
    a=int(input("your number:"))
    if a<number:
        print("sorry baby!!my guess is bigger than your number")
        s+=1
        continue
    elif a>number:
        print("sorry baby!!my guess is smuller than your number")
        s+=1
        continue
    else:
         print("bravo!!!you guessed right")
         s+=1
         print("your number of attempts:" ,s)
         break
