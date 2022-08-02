import urllib3

http = urllib3.PoolManager()

company = "YOUR_TEAMWORK_SITE_NAME"
key = "YOUR_API_KEY"
action = "projects.json"

url = "https://{0}.teamwork.com/{1}".format(company, action)
headers = urllib3.util.make_headers(basic_auth=f"{key}:xxx")
request = http.request('GET', url, headers=headers)

response = request.status
data = request.data

print(data)