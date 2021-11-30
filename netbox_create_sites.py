import requests
import json

requests.packages.urllib3.disable_warnings()

# session = requests.Session()
# session.verify = False


token = "a1d4293f44d220ff798c6768573b087bc4c45781"

data = [ {"name": "dc3", "slug": "dc3", "description": "Data Center in Toronto"}, {"name": "dc4", "slug": "dc4", "description": "Data Center in Ottawa"}]


url = 'http://127.0.0.1:8000/api/dcim/sites/'

headers = {'Authorization': "Token {}".format(token), 'content-type': "application/json"}

r = requests.post(url=url,  headers=headers, data=json.dumps(data))

print(r.status_code)

