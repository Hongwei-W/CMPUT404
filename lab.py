import requests as rq 

print(rq.__version__)

google = rq.get("http://www.google.com")
print(google)