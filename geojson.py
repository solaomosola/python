from urllib import request, parse,error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Enter location")
    if len(address)<1:
        break
    url = serviceurl + parse.urlencode({"address":address})

    print('Retrieving ',url)
    uh = request.urlopen(url)

    data = uh.read().decode()
    print('Retrieved ', len(data), 'characters')

    print(data)
    try:
        js = json.loads(data)
    except expression as identifier:
        js = None

    if not js or 'status' not in js or js['stautus']!='OK':
        print('---Failed to retired ---')
        print(data)
        continue
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print('lat', lat, 'lng',lng)

    location = js['results'][0]['formatted_address']
    print(location)