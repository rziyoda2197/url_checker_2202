import requests

url = input("URL: ")

try:
    r = requests.get(url)
    print("Status:", r.status_code)
except:
    print("Xato URL")
