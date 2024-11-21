"""import requests
getdata = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', stream= True) #loading data in chunks (can also assign how much to load lik 1 kbby kb etc
print(getdata.status_code)
print(getdata.headers) #Headers: Contain metadata (like content type, server information, etc.), providing details about the response.
print(getdata.content) #Content: Contains the actual body of the response (the data you requested), which could be text, JSON, HTML, or binary data.
"""
"""
import requests
payload = {'code': 'USD'} #payload keywork name can be anything
getdata = requests.get('https://jsonplaceholder.typicode.com/users',
params = payload)
print(getdata.content)
#We are now getting the details of the 'code': 'USD' details in the response.
#We can get a response in 2 ways using (text) and (.content). Using response.text will give you the data back in text format
"""
#POST
import requests
myurl = 'https://jsonplaceholder.typicode.com/users'
myparams = {'id': 21, 'email':'xyz@gmail.com'}
postdata = requests.post(myurl, data=myparams)
print(postdata.text)