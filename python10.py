import requests

response=requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_project = response.json()

for project in my_project:
    print(f"Project name :{project['name']}\nProject Url :{project['web_url']}\n")
