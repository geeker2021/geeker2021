##this is a number gussing game 


import random
ran=random.randint(0,10)
print("guss a number between 0 to 10 :)")
for i in range(10):
    g=int(input("guss a number : "))

    if ran==g:
            print("you win!!")
            if i==0 :
                print("you made it !! you got your full points !!")
            else:
                print("you take ",i ," extra chances !!")
            break
    else :
            strings = ['oh try again', 'its not', 'almost', 'try again', 'nope!!']
            random_string = random.choice(strings)
            print(random_string)
print("your score is ",10-i)