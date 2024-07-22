import random

def getNumber():
    return random.randrange(1,10)

def getResult(usernum,secretNumber):
    if usernum > secretNumber:
        return "high"
    elif usernum == secretNumber:
        return "correct"
    else:
        return "low"
def runGuess():
    secretNumber = getNumber()
    while True:
        usernum = int(input())
        result = getResult(usernum,secretNumber)
        if result=="high":
            print("your Number is much greater")
        elif result == "correct":
            print("YOu are Genius!!")
            break
        
        else:
            print("Go more higher")
        

        
            

            
if __name__ == '__main__':
    runGuess()