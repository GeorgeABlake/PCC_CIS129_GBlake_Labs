""" What county in the US should I move to?
By George Blake

I wrote this program to help me decide
what county to move to. It downloads
Economic Data from Gov Census API
and other databases then allows the user
to select what factors are important
then the program rates the counties
and displays them in order and by by map.
Started writing this coded Feb 22, 2023
"""
#***********This code suggested by chatGPt************
#
import requests
import sqlite3

# Replace 'YOUR_API_KEY' with your Census API key
api_key = '396cd46d5d73a1f44ccfdae7d4a5e010fde4ab39'

# Census API endpoint for 2019 ACS 5-Year Data - All variables
base_url = 'https://api.census.gov/data/2019/acs/acs5'

# Set up SQLite database
db_conn = sqlite3.connect('all_county_data.db')
cursor = db_conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS all_county_data (
        county_name TEXT,
        state_code TEXT
    )
''')
db_conn.commit()

# Function to fetch and store all economic variables for a given county
def fetch_and_store_all_data(county_fips, state_fips):
    url = f'{base_url}?get=*&for=county:{county_fips}&in=state:{state_fips}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print(f"Error fetching data for county {county_fips}: {data['error'][0]['message']}")
        return

    # Extract relevant data and their headers
    headers = data[0]
    county_data = data[1]

    # Insert data into the database dynamically
    cursor.execute('''
        INSERT INTO all_county_data ({})
        VALUES ({})
    '''.format(','.join(headers), ','.join(['?'] * len(headers))), tuple(county_data))
    db_conn.commit()

# Fetch and store all economic variables for all counties in the United States
for state_fips in range(1, 57):  # FIPS codes 1 to 56 represent states and territories
    for county_fips in range(1, 100):  # Assuming counties have FIPS codes 1 to 99
        fetch_and_store_all_data(str(county_fips).zfill(3), str(state_fips).zfill(2))

# Close database connection
db_conn.close()
