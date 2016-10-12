import urllib3
import json

destination_addresses = [ "San Francisco"," CA", "USA", "Victoria", "BC, Canada" ]

def get_details(distancematrix):
    http = urllib3.PoolManager()
    request = http.request('GET', '"https://maps.googleapis.com/maps/api/distancematrix/json?origins=Vancouver+BC|Seattle&destinations=San+Francisco|Victoria+BC&key=AIzaSyBuJVWRNQqE9ada3U5CWJURGm5k2qMcX0k')
    response = json.loads(request.data.decode('utf-8'))
    return [response['distance'][0]['duration'], response['text']['value']]
    print response
