import sys
import requests

# Token test : qZQOOVYH3ojuLg5tPgyFvZT7i
# Token santé : XmNpKdWgpy3WPlf52bz0eQFF8


def sizeToHuman(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1000:
            return "%3.3f %s" % (size, x)
        size /= float(1000)

    return size


url = "https://admin.test.kiwi-backup.com/api/contrats.json"

payload = ""
headers = {
    'Content-Type': "application/json",
    'X-AUTH-TOKEN': "qZQOOVYH3ojuLg5tPgyFvZT7i",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "f6719567-f68d-4c47-aaa7-4b8c90a2a18f,46b251d0-3b9b-41ce-b449-c2046029d94f",
    'Accept-Encoding': "gzip, deflate",
    'Referer': "http://admin.test.kiwi-backup.com/api/contrats.json",
    'Cookie': "PHPSESSID=15de9e2eb01dfaf74fd393a4c94f0fae",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)
if response.status_code != 200:
    sys.exit(0)

data = response.json()
volume_total = 0
for element in data['response']['results']:
    try:
        volume_total += element['volume_total']
        print(element['libelle'] + ' - ' + sizeToHuman(element['volume_total']))
    except TypeError:
        print(element['libelle'] + " - no data")
        pass
print(sizeToHuman(volume_total))
