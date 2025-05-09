import requests # type: ignore #module 

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
output =response.json()
for i in range(len(output)):
    print (output[i]["user"]["login"])
