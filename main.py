'''
HTTP Response Python
Nathan Tang
'''

import requests

while True:
    site = input("Website: ")
    
    try:
        try:
            response = requests.get(f'https://{site}', timeout=5)
        except:
            response = requests.get(f'http://{site}', timeout=5)

        ## Get status code
        print(f'Status Code: {response.status_code}')
        print(response.reason)

    except:
        print('Not a website')
    ## Get Headers
    # for i in response.headers:
    #     print("\n" + i + ":", response.headers.get(i))

  

    ## Get info
    # if response.status_code == 200:
    #     print('Status Code: 200')

    # Status Header
    # print(response.headers['Status'])

    again = input("Again? (y/n): ").lower()
    if again == 'y' or again == '':
        pass
    else:
        break