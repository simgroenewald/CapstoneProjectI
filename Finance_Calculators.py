# Compulsory Task

# Importing math functions.
import math

# User can either enter bond or investment here to do calculations.
selection = input ("Choose either 'investment' or 'bond' from the menu below to proceed:\
\n\
\ninvestment     - to calculate the amount of interest you'll earn on investment\
\nbond           - to calcualte the amount you'll have to pay on a home loan\
\nI would like to calculate:")

# Used so that capitalisation of letters does not matter.
selection = selection.lower()

# If statement for if the user chooses investment then this code will run.
if selection == "investment":
    invAmount = float(input ("How much would you like to invest:R"))
    intRate = float(input ("What is the interest rate you are investing at:"))
    invYear = float(input ("How many years would you like to invest for:"))
    interest = input ("Would you like simple or compound interest:")
    interest = interest.lower()
    # Nested if statements for if the user chooses either simple of compund interest.
    if interest == "simple":
        intSimple = invAmount*(1+((intRate/100)*invYear))
        intSimple = str(intSimple)
        print ("You will have a total of R" + intSimple)
    elif interest == "compound":
        intCompound = (invAmount*math.pow((1+(intRate/100)),invYear))
        intCompound = str(intCompound)
        print ("You will have a total of R" + intCompound)
    else: print ("You did not select compound or simple as an answer. Please try again.")


# Else if the user chooses bond then this code will run.
elif selection == "bond":
    houseVal = float(input ("Wha is the value of your huse:R"))
    intRate = float(input ("What is the interest rate:"))
    repayTime = float(input ("Over how many months do you plan to repay the bond:"))
    repay = ((intRate/100)*houseVal)/(1-math.pow((1+(intRate/100)),(-1*repayTime)))
    repay = str(repay)
    print ("Your monthly installments will be R" + repay)

# If the user does not enter bond or investment then this will print out.
else: print ("You did not enter bond or investment as an answer. Please try again.")

                    
                    
    
