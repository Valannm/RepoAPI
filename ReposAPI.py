import requests
import json

username = "Valannm"

request = requests.get('https://api.github.com/users/'+username+'/repos')
j = request.json()
for i in range(0,len(j)):
  print("Project Number:",i+1)
  print("Project Name:",j[i]['name'])
  print("Project URL:",j[i]['svn_url'],"\n")

