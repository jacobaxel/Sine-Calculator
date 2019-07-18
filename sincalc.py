#sin x = x - x^3/3! + x^5/5! etc etc 

def mcLaurinSign (termNumber):
    if termNumber % 2 == 0:
        return -1
    else:
        return 1
    
def factorial(n):
    finalAnswer = 1
    for x in range(1,n+1):
        finalAnswer *= x #finalAnswer = finalAnswer * x
    return finalAnswer

pi = 3.1415926575
 
def sinCalculator(angle, degreesOrRadians):
    if degreesOrRadians == "degrees":
        angle = angle * pi / 180
    finalAnswer = 0
    for x in range (1,100,2):
        if (x%4 == 1):
            finalAnswer = finalAnswer + (angle**x/factorial(x))
        else:
            finalAnswer = finalAnswer - (angle**x/factorial(x))
        
    return round(finalAnswer,8)
    
    
def sin2Calc(angle, degreesOrRadians):
    if degreesOrRadians == "degrees":
        angle = angle * pi / 180
    finalAnswer = 0
    for x in range(0,40):
        finalAnswer = finalAnswer + (((-1)**x)*(angle**((2*x)+1))/(factorial((2*x)+1)))
    return round(finalAnswer,8)
    
def simplifyRadian(radian):
    while (radian>2*pi):
        radian = radian - (2*pi)
    return radian

def version3():
    angle=input("What angle would you like to calculate the sine of? : ")
    try: 
        angle = float(angle)
        degreesOrRadians=input("Are you inputting your angle in degrees? : ")
        if degreesOrRadians.upper() != "YES" and degreesOrRadians.upper() != "NO":
            print("Answer yes or no please!")
        elif degreesOrRadians.upper() == "YES":
            angle = angle % 360
            angle = angle * pi / 180
            finalAnswer = 0
            for x in range(0,40):
                finalAnswer = finalAnswer + (((-1)**x)*(angle**((2*x)+1))/(factorial((2*x)+1)))
            print (round(finalAnswer,8))
        else:
            angle = simplifyRadian(angle)
            finalAnswer = 0
            for x in range(0,40):
                finalAnswer = finalAnswer + (((-1)**x)*(angle**((2*x)+1))/(factorial((2*x)+1)))
            print (round(finalAnswer,8))
        
    except:
        if angle.upper() == "DEREK":
            print("GO HOME MR. STAMPONE!!!!!!!!")
            
            
        elif angle.upper() == "ASH":
            print("Hello Mr. Das. This is the IRS. Please enter your social security number. But seriously, please enter a numerical angle.")
            angle=input("What angle would you like to calculate the sine of? : ")
            try: 
                angle = float(angle)
                degreesOrRadians=input("Are you inputting your angle in degrees? : ")
                if degreesOrRadians.upper() != "YES" and degreesOrRadians.upper != "NO":
                    print("Answer yes or no please!")
                elif degreesOrRadians.upper() == "YES":
                    angle = angle * pi / 180
                    finalAnswer = 0
                    for x in range(0,40):
                        finalAnswer = finalAnswer + (((-1)**x)*(angle**((2*x)+1))/(factorial((2*x)+1)))
                print (round(finalAnswer,8))
            except: 
                print("WHY ARE'NT YOU ENTERING A NUMBER")
                
        elif angle.upper() == "COURTNEY":
            print("Hello Ms. Morgan, your hair is awesome. But seriously, please enter a numerical angle.")
            angle=input("What angle would you like to calculate the sine of? : ")
            try: 
                angle = float(angle)
                degreesOrRadians=input("Are you inputting your angle in degrees? : ")
                if degreesOrRadians.upper() != "YES" and degreesOrRadians.upper != "NO":
                    print("Answer yes or no please!")
                elif degreesOrRadians.upper() == "YES":
                    angle = angle * pi / 180
                    finalAnswer = 0
                    for x in range(0,40):
                        finalAnswer = finalAnswer + (((-1)**x)*(angle**((2*x)+1))/(factorial((2*x)+1)))
                print (round(finalAnswer,8))
            except: 
                print("WHY ARE'NT YOU ENTERING A NUMBER")
            
        else:
            print("please enter a numerical angle!!")


version3()
    
    
    
#print(sinCalculator(pi,""))
#print(sin2Calc(pi,""))

#print(sin2Calc(400,""))

        