import random
'''
snake=1
water=-1
gun=0
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict = { 1: "Snake",-1 :"Water", 0:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict [computer]}")


if(computer == you):
    print("Its a draw")
else:
    if(computer== -1 and you == 1):
        print("You win")

    elif(computer== -1 and you == 0):
        print("you lose")  

    elif(computer== 1 and you == -1):    
          print("you lose")  

    elif(computer== 1 and you == 0):    
          print("you win") 

    elif(computer== 0 and you == 1):    
          print("you lose")  
          
    elif(computer== 0 and you == -1):    
          print("you win")  
    else:
         print("Something went wrong")      
