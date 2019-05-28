is_cnic_valid = input('DO YOU HAVE A VALID CNIC')
gender = str(input('SPECIFY YOUR GENDER'))


if is_cnic_valid .lower() == 'yes' and gender .lower() == 'malee' :
    print('PLEASE GO TO BOOTH A')


elif is_cnic_valid .lower() == "yes"  and gender .lower() == 'female' :
    print('PLEASE GO TO BOOTH B')

else :
    print('THANK YOU FOR COMING BUT SORRY GO HOME ! ')

