import requests

response = requests.get(url="https://kitsu.io/api/edge/anime?filter[text]=cowboy%20bebop")
response.raise_for_status()
assert response.status_code == 200
data = response.json()
# print(type(data))
# print(response.headers)
assert response.headers['Content-Type'] == 'application/vnd.api+json'

for expectedanimedata in data["data"]:
    if expectedanimedata['id'] == '1':
        print(expectedanimedata["attributes"]["slug"])

expectedmatchdata = data["data"][0]["attributes"]["slug"]
print(expectedmatchdata)
actualanimedata = "cowboy-bebop"
assert expectedmatchdata == actualanimedata
