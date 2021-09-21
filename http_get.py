import requests
import sys
import json
input=sys.stdin.readline
print("장소 검색:",end="")
place=str(input())
search='https://maps.googleapis.com/maps/api/geocode/json?key=api' \
'&sensor=false&language=ko&address={}'.format(place)

response=requests.get(search)

results=response.json()
lat=results['results'][0]['geometry']['location']['lat']
lng=results['results'][0]['geometry']['location']['lng']
adress=results['results'][0]['formatted_address']

print("위도:",lat)
print("경도:",lng)
print("주소:",adress)


