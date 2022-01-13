import requests as rq 

print(rq.__version__)

google = rq.get("http://www.google.com")
print(google)

source_code = rq.get("https://raw.githubusercontent.com/Hongwei-W/CMPUT404/master/lab.py")
print(source_code.content)