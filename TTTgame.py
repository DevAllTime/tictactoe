

#Tic Tac Toe game in python by #Syntax.
#enter elements 0,2,4

first_row = [None,None,None]
second_row = [None,None,None]
third_row = [None,None,None]

#This function displays status
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
    # debugging print "%d %d %d"%(row,coloumn,valu)
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
    if(first_row[0] == first_row[1] == first_row[2] and first_row[0]!= None and first_row[1]!= None and first_row[2]!= None or \
    second_row[0] == second_row[1] == second_row[2] and second_row[0]!= None and second_row[1]!= None and second_row[2]!= None or \
    third_row[0] == third_row[0] == third_row[2] and third_row[0]!=None and third_row[0]!=None and third_row[2]!= None  or \
    first_row[0] == second_row[1] == third_row[2] and first_row[0]!=None and second_row[1]!=None and third_row[2]!=None or \
    first_row[2] == second_row[1] == third_row[0] and first_row[2]!=None and second_row[1]!=None and third_row[0]!=None or \
    first_row[0] == second_row[0] == third_row[0] and first_row[0]!=None and second_row[0]!=None and third_row[0]!=None or \
    first_row[1] == second_row[1] == third_row[1] and first_row[1]!=None and second_row[1]!=None and third_row[1]!=None or \
    first_row[2] == second_row[2] == third_row[2] and first_row[2]!=None and second_row[2]!=None and third_row[2]!=None ):
        return False
    else:
        return True

    if first_row[0] == first_row[1] == first_row[2]:
        if first_row[0]!=None and first_row[1]!=None and first_row[2]!=None:
            return False
    if second_row[0] == second_row[1] == second_row[2]:
        if second_row[0]!=None and second_row[1]!=None and second_row[2]!




#********************************MAIN FUNCTION******************************
print "Welcome to the Tic Tac Toe Game!!\n"
print "Please Enter the values accroding to"
print "00,01,02|10,11,12|20,21,22"
result = True
#while(result):
for i in range(3):
    r_ow = raw_input("Enter the Row")
    c_ol = raw_input("Enter the Coloumn")
    i_nput = raw_input("Enter the input value")
    setting_inputs(int(r_ow),int(c_ol),int(i_nput))
    display_status()
    #result = didyouloose()
    if(not didyouloose()):
        print "WON"



#check if you won?
