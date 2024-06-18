import requests

def search_quanzhou():
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': 'Quanzhou, China',
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

def get_bounding_box(osm_type, osm_id):
    url = f"https://nominatim.openstreetmap.org/lookup?osm_ids={osm_type[0].upper()}{osm_id}&format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            bounding_box = data[0]['boundingbox']
            max_latitude = bounding_box[1]
            return max_latitude
    return None

# Step 1: Retrieve OSM Type and OSM ID for Quanzhou
osm_type, osm_id = search_quanzhou()

osm_id=244081721
# Step 2: Get the bounding box information using the OSM Type and OSM ID
if osm_id and str(osm_id).endswith("1721"):
    max_latitude = get_bounding_box(osm_type, osm_id)
    if max_latitude:
        print(f"The maximum latitude of the bounding box for Quanzhou, China (OSM ID {osm_id}) is {max_latitude}.")
    else:
        print("Failed to retrieve the bounding box information.")
else:
    print("Failed to retrieve OSM ID for Quanzhou or OSM ID does not end with 1721.")
