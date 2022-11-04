# This program benefits from external files because it allows it to save and updated leaderboard that will continue to be used. If it didn't use external files, the
# leaderboard would reset each time you ran the code.

###################################################################
# Kelton Figurski
# Arrays Summative
# Simple Math Game With Leaderboard
###################################################################


import random
import time


# ----------------------------- Functions ----------------------------- #

# Function that replaces score on leaderboard with new time
def replaceline(list_num):
    with open ('Leaderboard.txt') as file:
        lines = file.readlines()
        
    lines[list_num] = f"{name}: {endtime}s\n"
    
    with open('Leaderboard.txt', 'w') as file:
        for line in lines:
            file.write(line)
            
# Function that moves leaderboard down so it adds new score instead of replacing old one
def movedown(list_num):
    with open ('Leaderboard.txt') as file:
        lines = file.readlines()
        
    lines[list_num] = f"\n{lines[list_num]}"
    
    with open('Leaderboard.txt', 'w') as file:
        for line in lines:
            file.write(line)
            
# Function that deletes extra line after moving down
def delete_extra_line():
    with open ('Leaderboard.txt') as file:
        lines = file.readlines()
        
    del lines[10]
    
    with open('Leaderboard.txt', 'w') as file:
        for line in lines:
            file.write(line)


# ----------------------------- Main Code ----------------------------- #

print("Math Game")

name = input("What is your name?") # Asks user for name
starttime = time.time() # Marks the starting time

x = 10

while x > 0:
    
    operation = random.randint(1, 4) # finds random number to create a random operation
    
    # Creates a addition problem
    if operation == 1:
         
        num1 = random.randint(1, 300)
        num2 = random.randint(1, 300)
        sum1 = num1 + num2
        
        while True:  
            
            addanswer = input(f"{num1} + {num2} = ")
            
            try:
                addanswer = int(addanswer)
                
            except:
                print("That is not a valid answer.")
                continue
            
            if int(addanswer) != sum1:
                print("Incorrect. Try Again.")
                
            else:
                break
        
    # Creates a subtraction problem    
    if operation == 2:
        
        num1 = random.randint(150, 300)
        num2 = random.randint(1, 149)
        difference = num1 - num2
        
        while True:
            
            subtractanswer = input(f"{num1} - {num2} = ")
            
            try:
                subtractanswer = int(subtractanswer)
                
            except:
                print("That is not a valid answer.")
                continue
            
            if int(subtractanswer) != difference:
                print("Incorrect. Try Again.")
                
            else:
                break

    # Creates a multiplication problem
    if operation == 3:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        product = num1 * num2
        
        while True:
        
            multiplyanswer = input(f"{num1} * {num2} = ")
            
            try:
                multiplyanswer = int(multiplyanswer)
                
            except:
                print("That is not a valid answer.")
                continue
            
            if int(multiplyanswer) != product:
                print("Incorrect. Try Again.")
                
            else:
                break

    # Creates a division problem
    if operation == 4:
        quotient = random.randint(1, 12)
        num2 = random.randint(1, 12)
        num1 = quotient * num2
        
        while True:
            
            divideanswer = input(f"{num1} / {num2} = ")
            
            try:
                divideanswer = int(divideanswer)
                
            except:
                print("That is not a valid answer.")
                continue
            
            if int(divideanswer) != quotient:
                print("Incorrect. Try Again.")
                
            else:
                break
        
    x = x - 1
    
endtime = time.time() - starttime # Marks the ending time
endtime = round(endtime) # Marks how long it took

print(f"\nYou got a time of {endtime}s") #prints time

# Splits the leaderboard into lines
file = open('Leaderboard.txt', 'r')
leaderboard = file.read().split('\n')
file.close()

# Each of these splits a line into name and time
leaderboard1 = leaderboard[0]
leaderboard1 = leaderboard1.split(':')

leaderboard2 = leaderboard[1]
leaderboard2 = leaderboard2.split(':')

leaderboard3 = leaderboard[2]
leaderboard3 = leaderboard3.split(':')

leaderboard4 = leaderboard[3]
leaderboard4 = leaderboard4.split(':')

leaderboard5 = leaderboard[4]
leaderboard5 = leaderboard5.split(':')

leaderboard6 = leaderboard[5]
leaderboard6 = leaderboard6.split(':')

leaderboard7 = leaderboard[6]
leaderboard7 = leaderboard7.split(':')

leaderboard8 = leaderboard[7]
leaderboard8 = leaderboard8.split(':')

leaderboard9 = leaderboard[8]
leaderboard9 = leaderboard9.split(':')

leaderboard10 = leaderboard[9]
leaderboard10 = leaderboard10.split(':')
    
# Each of these adds a time in correct spot
if endtime < int(leaderboard1[1]):
    movedown(0)
    delete_extra_line()
    replaceline(0)
    
elif endtime < int(leaderboard2[1]):
    movedown(1)
    delete_extra_line()
    replaceline(1)
    
elif endtime < int(leaderboard3[1]):
    movedown(2)
    delete_extra_line()
    replaceline(2)
    
elif endtime < int(leaderboard4[1]):
    movedown(3)
    delete_extra_line()
    replaceline(3)
    
elif endtime < int(leaderboard5[1]):
    movedown(4)
    delete_extra_line()
    replaceline(4)
    
elif endtime < int(leaderboard6[1]):
    movedown(5)
    delete_extra_line()
    replaceline(5)
    
elif endtime < int(leaderboard7[1]):
    movedown(6)
    delete_extra_line()
    replaceline(6)
    
elif endtime < int(leaderboard8[1]):
    movedown(7)
    delete_extra_line()
    replaceline(7)
    
elif endtime < int(leaderboard9[1]):
    movedown(8)
    delete_extra_line()
    replaceline(8)
    
elif endtime < int(leaderboard10[1]):
    movedown(9)
    delete_extra_line()
    replaceline(9)

# Saves updated leaderboard
file = open('Leaderboard.txt', 'r')
updated_leaderboard = file.read()

time.sleep(1)

print(f"\nLeaderboard: \n{updated_leaderboard}") # prints updated leaderboard