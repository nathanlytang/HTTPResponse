'''
HTTP Response Python
Nathan Tang
'''

import requests

while True:
    site = input("\nWebsite: ")
    
    try:
        try:
            response = requests.get(f'https://{site}', timeout=5)
        except:
            response = requests.get(f'http://{site}', timeout=5)

        # Get status code
        print(f'Status Code: {response.status_code}')
        print(response.reason)

    except:
        print('Not a website')

    again = input("\nAgain? (y/n): ").lower()
    if again == 'y' or again == '':
        pass
    else:
        break