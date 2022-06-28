import requests
import json 

url = 'https://api-dev-platform.usbim.com/BimPlatformRest/api/1.0/login'

body = {
    'username': 'syncposte@acca.it',
    'password': '3jJ8XiXshkbYRfM'
    }

header ={
    'X-USBIM-PLATFORM-SERVICE-KEY' : 'q3msTz701V1yrRHMoxH0WKoCCj6kSbszCpzQTiYySqQqiOOrSiWW5gvEeu15gCmz'
}


# def getToken(url, body):
#     myRequest = requests.post(url, json = body, headers = {'X-USBIM-PLATFORM-SERVICE-KEY' : 'q3msTz701V1yrRHMoxH0WKoCCj6kSbszCpzQTiYySqQqiOOrSiWW5gvEeu15gCmz'})
#     response = json.loads(myRequest.content)
#     token = response['token']
#     return token

def getToken(url, body, header):
    myRequest = requests.post(url, json = body, headers = header)
    response = json.loads(myRequest.content)
    token = response['token']
    return token

def main():
    token = getToken(url, body, header)
    print(token)

if __name__ == "__main__":
    main()
