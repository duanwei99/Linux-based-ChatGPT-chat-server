import requests

url = "https://way.jd.com/jisuapi/get?appkey=3d1d782c98cd7034343556106217c01f&channel=头条&num=20&start=0&NO=742"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
