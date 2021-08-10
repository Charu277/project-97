import random
print ("NUMBER GUESSING GAME")
number=random.randint(1,9)
chances=0



while chances<5:
    guessingNumber=input("Guess a number 1-9")
    guessingNumber=int(guessingNumber)

    if guessingNumber==number:
        print("congratulations!! you won") 
        break
    elif guessingNumber<number:
        print("your guess was too low")
    else:
        print("your guess was too high")


if not chances <5:
    print("you lose,the number is",number)       
        
 

    
