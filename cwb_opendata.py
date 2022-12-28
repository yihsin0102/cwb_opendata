import requests as rq
import json
import os

cwbkey = os.getenv('cwbkey')
r = rq.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization='+cwbkey).json()
a= r['records']['earthquake']
for i in a:
    t = i['reportContent']
    print(t)
