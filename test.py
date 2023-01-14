import requests
BASE ='http://127.0.0.1:5000/'

# response = requests.put(BASE +'video/2',data={'name':'fuck like','likes':12,'views':122})
response = requests.get(BASE +'api/stats/total')

print(response.json())