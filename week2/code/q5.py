# q5, pt1

import requests

def search_tianjin():
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': 'Tianjin, China',
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            osm_id = data[0]['osm_id']
            osm_type = data[0]['osm_type']
            return osm_type, osm_id
    return None, None

osm_type, osm_id = search_tianjin()
if osm_id:
    print(f"OSM Type: {osm_type}")
    print(f"OSM ID: {osm_id}")
else:
    print("Failed to retrieve OSM ID for Tianjin.")


def get_bounding_box(osm_type, osm_id):
    url = f"https://nominatim.openstreetmap.org/lookup?osm_ids={osm_type[0].upper()}{osm_id}&format=json"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        if data:
            bounding_box = data[0]['boundingbox']
            max_latitude = bounding_box[1]
            return max_latitude
    return None

# Retrieve OSM Type and OSM ID for Tianjin
osm_type, osm_id = search_tianjin()

if osm_id:
    max_latitude = get_bounding_box(osm_type, osm_id)
    if max_latitude:
        print(f"The maximum latitude of the bounding box for Tianjin, China (OSM ID {osm_id}) is {max_latitude}.")
    else:
        print("Failed to retrieve the bounding box information.")
else:
    print("Failed to retrieve OSM ID for Tianjin.")
