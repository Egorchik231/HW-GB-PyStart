def pers_info(name, sername, date_birth, city, e_mail, phone):
    print(f'{name} {sername}, {date_birth}, {city}, {e_mail}, {phone}')

name = input('Enter name: ')
sername = input('Enter sername: ')
date_birth = input('Year: ')
city = input('Enter city: ')
e_mail = input('Enter e-mail: ')
phone = input('Enter phone: ')

pers_info(name, sername, date_birth, city, e_mail, phone)