import pwinput
import random
list = []

lowercase = 'abcdefghijklmnopqrstuv'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols   = '@#$%*-_;'


password = lowercase + uppercase + symbols 
FinalPassword = ''.join(random.sample(password,8))

print("your generated password is ",FinalPassword)

a = pwinput.pwinput(prompt = 'confirm your password : ')

while(a!=FinalPassword):
    print("Incorrect password entered.Try again")
    a = pwinput.pwinput(prompt = 'confirm your password : ')
    list.append(a)
    if len(list)>5:
        print("You have incorrectly entered password for more than 5 times.You are denied access to visiting this page")
        break



if a==FinalPassword:
    print("Password verified successfully !")
    print("Stay safe, stay secure ! :) ")


print("done")



