

Sheet_no = str(input(" Enter marksheet no : "))

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

p = float (((physics+phys)/200)*100)

m = float((maths/200)*100)

over_all_percentage = float(((urdu+english+islamiyat+pakistan_studies+chemistry+chem+phys+physics
                             +maths)/1100)*100)






print('\n\n\n\n\n\n\n\n\n\n         BOARD OF INTERMEDIATE EDUCATION KARACHI\n\n\n')
print("\n\n\n           Statement of Marks\n")
print('\n\n SHEET NUMBER : ' + str(Sheet_no) )
print( '\n GROUP :'+ str(Group) )
print('\n ENROLMENT NUMBER :' + str(Enrolment_no))
print( '\n ROLL NUMBER : ' + str(Roll_no))
print( '\n NAME :' + str(Name) )
print( '\n FATHER NAME :' + str(Fatehr_name))
print('\n COLLEGE : '+ str(College))

print('\n\n\nINDIVIDUAL PERCENTAGES\n\n')

print('\n\n URDU : ' + str(u) + ' %')

print('\n ENGLISH : ' + str(e) + ' %')

print('\n ISLAMIYAT : ' + str(i) + ' %\n')

print('PAKISTAN STUDIES : ' + str(p) + ' %\n')

print('CHEMISTRY : ' + str(c) + ' %\n')

print('PHYSICS : ' + str(p) + ' %\n')

print('MATHS : ' + str(m) + ' %\n')

print("OVER ALL PERCENTAGE : " + str(over_all_percentage) + ' %')


if over_all_percentage < 35 :
    print("\n\n         FAIL !")

elif   35 < over_all_percentage <= 60 :
      print("\n\n       C GRADE")

elif 60< over_all_percentage<= 69.9 :
    print('\n\n         B GRADE')

elif 70< over_all_percentage <=80 :
    print("\n\n          A GRADE")

elif 80 < over_all_percentage <= 100 :
    print('\n\n          A+ GRADE ')

else :
    print ("INVALID CALCULATION")
