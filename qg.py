#!/usr/bin/python
import requests



# define header
headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

#define data
data = {'foo': 'bar'}

r = requests.get('https://www.jd.com', data=data, headers=headers)

print(r.text)


