

#Tic Tac Toe game in python by #Syntax.
#enter elements 0,2,4

first_row = [None,None,None]
second_row = [None,None,None]
third_row = [None,None,None]

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
    if(row == 0 and first_row[coloumn]== 1 or 0):
        print"You cannot Replace"
    else:
        first_row[coloumn] = valu
        return

    if row == 1 and second_row[coloumn]== 1 or 0:
        print"You cannot Replace"
    else:
        second_row[coloumn] = valu
        return

    if row == 2 and third_row[coloumn]== 1 or 0:
        print"You cannot replace"
    else:
        third_row[coloumn] = valu
        return

def didyouloose():
    #first 3 about horizontal equal,next 2 diogonal, next 3 vertical equals
    if(first_row[0] == first_row[1] == first_row[2] or \
    second_row[0] == second_row[1] == second_row[2] or \
    third_row[0] == third_row[0] == third_row[2] or \
    first_row[0] == second_row[1] == third_row[2] or \
    first_row[2] == second_row[1] == third_row[0] or \
    first_row[0] == second_row[0] == third_row[0] or \
    first_row[1] == second_row[1] == third_row[1] or \
    first_row[2] == second_row[2] == third_row[2]):
        return False
    else:
        return True


#********************************MAIN FUNCTION******************************
print "Welcome to the Tic Tac Toe Game!!\n"
print "Please Enter the values accroding to"
print "00,01,02|10,11,12|20,21,22"
for i in range(3):
    r_ow = raw_input("Enter the Row")
    c_ol = raw_input("Enter the Coloumn")
    i_nput = raw_input("Enter the input value")
    setting_inputs(int(r_ow),int(c_ol),int(i_nput))
    display_status()
    if(didyouloose()):
        print "you won!"

#check if you won?
