# JSON = javascript object notation
# JSON is a format for storing and transporting data
# JSON is often used when data is sent from a server to a web page
import json
import requests
import sys
if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))
# to get the name of the song
n = response.json()
for result in n["results"]:
    print(result["trackName"])