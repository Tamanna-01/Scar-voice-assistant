import requests

key = "eeb9f39236b64129805fcbc3fd4fadf2"
api_address = "https://newsapi.org/v2/everything?q=keyword&apiKey="+ key
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append(f"Number {str(i+1)} {json_data['articles'][i]['title']}.")
        # ar.append("Number " + str(i+1) + json_data["articles"][i]["title"]+".")
    return ar


# arr = news()
# print(ar)