#import math moudle
import math
#import random moudle..
import random
#def function to calculte hypotenuse take two argu..
def hypotenuse(a,b):
##    print('a**2::  ',a**2)
##    print('b**2::  ',b**2)
    c = math.sqrt(a**2 +b**2)
    return(c)
    

print('return hypotenuse(3,4)::  ',hypotenuse(3,4))
print('return hypotenuse(30,40)::  ',hypotenuse(30,40))
print('return hypotenuse(6,8)::  ',hypotenuse(6,8))

## section of guess function  
print('guess function >>>')
lst=[]
for x in range(21):
    lst.append(random.randint(1,150))
lst= sorted(lst,reverse=False) 
##guess = (sum(lst)/ len(lst)) +10
##guess=int(guess)
##print('guess number::  ',guess)
print('You can enter any number between 1:150, integer number only...')

user_guess =int(input('Enter your valid number:: '))
def guess(user_guess):
    num_guess = (sum(lst)/ len(lst)) +10
    num_guess=int(num_guess)
    print('guess number::  ',num_guess)
    if(num_guess < user_guess):
        return('The guess number samller than your guessing')
    elif(num_guess > user_guess):
        return('The guess number greater than your guessing')
    elif(num_guess == user_guess):
        return('Congratulation... your guessing is correct.')
        
print(guess(user_guess))

