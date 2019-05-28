


cnic = input("DO YOU HAVE VALID CNIC  -YES OR NO-  ?")

if cnic .lower() == 'yes' :
    gender = input('WHAT IS YOUR GENDER ?')
    if gender .lower() == 'male' :
        print('go to booth A')

    elif gender .lower() == 'female' :
        print('Go to booth B')

    else :
        print('Please write MALE or FEMALE only')

else :
    print('THANKS FOR COMING BUT PLEASE GO HOME')

