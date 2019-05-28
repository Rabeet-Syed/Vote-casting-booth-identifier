Sheet_no = str(input(" \n\n\n\nEnter marksheet no : "))

Group = str(input("Enter Group  :"))

Roll_no = int(input('Enter roll no :'))

Enrolment_no = str(input("Enter Enrolment no :"))

Name = str(input('Enter name :'))

Fatehr_name = str(input('Enter father name :'))

College = str(input('Enter college name :'))


print('!!!  THEORY MARKS  !!!')



urdu = int(input('Enter obtained marks in URDU :'))

english = int(input('Enter obtained marks in ENGLISH :'))

islamiyat = int(input('Enter obtained marks in ISLAMIYAT :'))

pakistan_studies = int(input('Enter obtained marks in PAKISTAN STUDIES :'))

chemistry = int(input('Enter obtained marks in CHEMISTRY :'))

physics = int(input('Enter obtained marks in PHYSICS :'))

maths = int(input('Enter obtained marks in MATHS :'))




print("  !!! PRACTICAL MARKS !!!  ")

chem = int(input('Enter obtained marks in CHEMISTRY PRACTICAL :'))

phys = int(input('Enter obtained marks in PHYSICS PRACTICAL :'))



u = float((urdu / 200) *100)

e = float((english / 200)*100)

i = float ((islamiyat / 50)*100)

p = float ((pakistan_studies / 50)*100)

c = float (((chemistry+chem)/200)*100)

P = float (((physics+phys)/200)*100)

m = float((maths/200)*100)

over_all_percentage = float(((urdu+english+islamiyat+pakistan_studies+chemistry+chem+phys+physics
                             +maths)/1100)*100)



print("\n\n\n                    ****************************")


print('\n\n\n\n\n\n\n\n            BOARD OF INTERMEDIATE EDUCATION KARACHI')
print('                   --------------------------\n\n\n')
print("\n\n\n                 Statement of Marks")
print('                 ------------------\n')
print('\n\n SHEET NUMBER : ' + str(Sheet_no) )
print( '\n GROUP :'+ str(Group) )
print('\n ENROLMENT NUMBER :' + str(Enrolment_no))
print( '\n ROLL NUMBER : ' + str(Roll_no))
print( '\n NAME :' + str(Name) )
print( '\n FATHER NAME :' + str(Fatehr_name))
print('\n COLLEGE : '+ str(College))

print('\n\n\n            INDIVIDUAL PERCENTAGES')
print('              -------------------\n\n')

if 0<= urdu <= 200 :
    print('\n\n URDU : ' + str(u) + ' %')
else :
    print('ENTER COREECT MARKS FOR URDU')


if 0<= english <= 200 :
    print('\n ENGLISH : ' + str(e) + ' %')
else :
    print('ENTER COREECT MARKS FOR ENGLISH')


if 0<= islamiyat <= 50 :
    print('\n ISLAMIYAT : ' + str(i) + ' %\n')
else :
    print('ENTER COREECT MARKS FOR ISLAMIYAT')



if 0<= pakistan_studies <= 50 :
    print('PAKISTAN STUDIES : ' + str(p) + ' %\n')
else :
    print('ENTER COREECT MARKS FOR PAKISTAN STUDIES')


if 0<= chemistry <= 200 :
    print('CHEMISTRY : ' + str(c) + ' %\n')
else :
    print('ENTER COREECT MARKS FOR CHEMISTRY')

if 0<= physics <= 200 :
    print('PHYSICS : ' + str(P) + ' %\n')
else :
    print('ENTER COREECT MARKS FOR PHYSICS')

if 0<= maths and maths <= 200 :
    print('MATHS : ' + str(m) + ' %\n')
else :
    print('ENTER COREECT MARKS FOR MATHS')



if 0<= u >= 100and 0<=e>=100and 0<= i >= 100 and 0<= p >= 100 and 0<= c >= 100 and 0<= P >= 100 and 0<= m >= 100 :
    print("\n\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-\n\n\n")
    print("OVER ALL PERCENTAGE : " + str(over_all_percentage) + ' %')


    if over_all_percentage < 35 :
        print("\n\n            FAIL !")

    elif   35 < over_all_percentage <= 60 :
      print("\n\n          C GRADE")

    elif 60< over_all_percentage<= 69.9 :
        print('\n\n            B GRADE')

    elif 70< over_all_percentage <=80 :
         print("\n\n             A GRADE")

    elif 80 < over_all_percentage <= 100 :
        print('\n\n             A+ GRADE ')

    else :
        print ("\n\n       INVALID CALCULATION")

else:
    print('PLEASE GIVE CORRECT DATA')
