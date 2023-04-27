import random
import math
lower=int(input("Enter lower bound:  "))
upper=int(input("Enter upper bound:  "))
x=random.randint(lower,upper)
print("\n\tYou've only ",
         round(math.log(upper-lower+1,2)),
      "chance to guess the integer!\n")
count=0
while count < math.log(upper-lower+1,2):
    count +=1
    guess=int(input("Guess a number: "))
    if x==guess:
        print("that's right",count,"try")
        break
    elif x>guess:
        print("you guessed too small")
    elif x<guess:
        print("you guessed too big")
    print("\tbetter try next time!")
