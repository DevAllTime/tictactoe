#Tic Tac Toe game in python by #Syntax.
#enter elements 0,2,4

first_row = [None,None,None]
second_row = [None,None,None]
third_row = [None,None,None]

#This function displays status
#this is the function  2
def display_status():
    for i in first_row:
        print "%s |"%(i),
    print ""
    for j in second_row:
        print "%s |"%(j),
    print ""
    for k in third_row:
        print "%s |"%(k),
    print "\n"

def setting_inputs(row,coloumn,valu):
    #input elements into the list & #Elements should not be replaced
    #defining setting input
    if row == 0:
        if first_row[coloumn]== 1 or 0:
            print"YOU CANNOT REPLACE!!!\n"
        else:
            first_row[coloumn] = valu
    if row == 1:
        if second_row[coloumn]== 1 or 0:
            print"YOU CANNOT REPLACE!!!\n"
        else:
            second_row[coloumn] = valu
    if row == 2:
        if third_row[coloumn]== 1 or 0:
            print"YOU CANNOT REPLACE!!!\n"
        else:
            third_row[coloumn] = valu

def didyouloose():
    #first 3 about horizontal equal,next 2 diogonal, next 3 vertical equals
    if first_row[0] == first_row[1] == first_row[2]:
        if first_row[0]!=None and first_row[1]!=None and first_row[2]!=None:
            return False
    if second_row[0] == second_row[1] == second_row[2]:
        if second_row[0]!=None and second_row[1]!=None and second_row[2]!=None:
            return False
    if third_row[0] == third_row[0] == third_row[2]:
        if third_row[0]!=None and third_row[0]!=None and third_row[2]!=None:
            return False
    if first_row[0] == second_row[1] == third_row[2]:
        if first_row[0]!=None and second_row[1]!=None and third_row[2]!=None:
            return False
    if first_row[2] == second_row[1] == third_row[0]:
        if first_row[2]!=None and second_row[1]!=None and third_row[0]!=None:
            return False
    if first_row[0] == second_row[0] == third_row[0]:
        if first_row[0]!=None and second_row[0]!=None and third_row[0]!=None:
            return False
    if first_row[1] == second_row[1] == third_row[1]:
        if first_row[1]!=None and second_row[1]!=None and third_row[1]!=None:
            return False
    if first_row[2] == second_row[2] == third_row[2]:
        if first_row[2]!=None and second_row[2]!=None and third_row[2]!=None:
            return False
    return True

#********************************MAIN FUNCTION******************************#
print "Welcome to the Tic Tac Toe Game!!\n"
print "Please Enter the values accroding to"
print "00,01,02|10,11,12|20,21,22"
result = True
while(result):
    Placment = raw_input("Enter the placment of element")
    #i_nput = raw_input("Enter input your mark 0 or 1"
    i_nput = 0
    while(int(i_nput) is not 0 or 1):
        i_nput = raw_input("Enter input your mark 0 or 1")
        if i_nput is "0" or "1":
            break
    setting_inputs(int(Placment[0]),int(Placment[1]),int(i_nput))
    display_status()
    result = didyouloose()
    if(not result):
        print "%s Won the Game"%(i_nput)
