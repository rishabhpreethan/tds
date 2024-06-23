import json
from collections import defaultdict
from rapidfuzz import fuzz
from rapidfuzz import process

# Read the JSON file
with open('tds\\week3\\city-product-sales.json') as f:
    sales_data = json.load(f)

# Group cities by similarity using phonetic clustering
def cluster_cities(sales_data, threshold=80):
    city_clusters = {}
    all_cities = list(set(entry['city'] for entry in sales_data))
    
    for city in all_cities:
        matched_cities = process.extract(city, all_cities, scorer=fuzz.ratio, score_cutoff=threshold)
        cluster_key = min(matched_cities, key=lambda x: x[1])[0]
        if cluster_key not in city_clusters:
            city_clusters[cluster_key] = set()
        city_clusters[cluster_key].add(city)
    
    return city_clusters

# Step 2: Filter entries for product "Flour" with sales at least 53
def filter_entries(sales_data, city_clusters):
    filtered_entries = []
    for entry in sales_data:
        if entry['product'] == 'Flour' and entry['sales'] >= 53:
            for cluster_key, cities in city_clusters.items():
                if entry['city'] in cities:
                    filtered_entries.append((cluster_key, entry['sales']))
                    break
    return filtered_entries

# Step 3: Group filtered entries by clustered city
def group_by_city(filtered_entries):
    city_sales = defaultdict(int)
    for cluster_key, sales in filtered_entries:
        city_sales[cluster_key] += sales
    return city_sales

# Step 4: Find the city with the highest sales
def find_top_city(city_sales):
    top_city = max(city_sales, key=city_sales.get)
    return top_city, city_sales[top_city]

# Run the steps
city_clusters = cluster_cities(sales_data)
filtered_entries = filter_entries(sales_data, city_clusters)
city_sales = group_by_city(filtered_entries)
top_city, top_city_sales = find_top_city(city_sales)

# Output the result
print(f"The city with the highest sales is: {top_city}, with total sales of: {top_city_sales} units.")

# For the given options, the expected answer should be one of: 641, 642, 643, 644
print(top_city_sales)
