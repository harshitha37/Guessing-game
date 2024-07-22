import random
import math
m=int(input("enter lower bound:"))
n=int(input("enter upper bound:"))
rdm_num=random.randrange(m,n+1)
c=0
print("You've only",round(math.log(n-m+1,2)),"chances to get an integer!")
for i in range(round(math.log(n-m+1,2))):
    guess_num=int(input("guess a number:"))
    if rdm_num==guess_num:
        c+=1
        print("Congratulations you did it in",c ,"try")
        break
    elif rdm_num>guess_num:
        print('Try Again! You guessed too small')
        c+=1
    else:
        print('Try Again! You guessed too big')
        c+=1
if c>math.log(n-m+1,2):
    print("the number is",rdm_num)
    print("better luck next time!")