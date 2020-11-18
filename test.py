import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/2", {"views":69, "likes":420})
print(response.json()) #.JSON returns us a method

#data = [{"likes": 78, "name": "Joe", "views": 10000}, {"likes": 1000, "name": "How to make REST API", "views": 8000}, {"likes": 35, "name": "uriel", "views": 2000}]
#
#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print(response.json()) #.JSON returns us a method
#
##input()
##response = requests.delete(BASE + "video/0")
##print(response)
#input()
#response = requests.get(BASE + "video/2", {"views":69})
#print(response.json()) #.JSON returns us a method