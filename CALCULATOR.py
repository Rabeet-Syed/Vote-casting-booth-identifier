print(" \n\n\n\n\n\n\n\n\n\n\n\n               !! BASIC CALCULATOR !! ")
print('                   -------------\n\n\n')

num_1 = float(input("            Enter First Value : \n \n---->    "))

num_2 = float(input(" \n \n            Enter second value : \n \n---->    "))

op = str(input(" \n \n            Enter Operand : \n \n ----{+ - / * %}---->    "))
print('\n\n\n           **********************************************************\n\n\n')
if op == '+' :
    print("               RESULT OF ADDING  " + str(num_1) + " & " + str(num_2) + " = " + str(num_1 + num_2 )+ "\n\n.")

elif op == "-" :
    print("               RESULT OF SUBTRACTING  " + str(num_2) + " From " + str(num_1) + " = " + str(num_1 - num_2 )+ '\n\n')

elif op== '*' :
    print("              RESULT OF MULTIPLICATING " + str(num_1) + " & " + str(num_2) + " = " + str(num_1 * num_2 )+ '\n\n')

elif op == '/' :
    print("              RESULT OF DIVIDING " + str(num_2) + " FROM " + str(num_1) + " = " + str(num_1 / num_2 )+ '\n\n')

elif op == '%' :
     print("             REMAINDER OF DIVIDING " + str(num_2) + " FROM " + str(num_1) + " = " + str(num_1 % num_2 )+ '\n\n')

else :
    print("!!            INVALID OPERATION REQUESTED !!")
