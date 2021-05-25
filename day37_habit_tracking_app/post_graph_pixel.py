import requests
import datetime

TOKEN = ""
BASE_URL = "https://pixe.la"
USERNAME = "frankv125"
GRAPH_ID = "graph1"
POST_GRAPH_PIXEL_ENDPOINT = f"{BASE_URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()
DATE = today.strftime("%Y%m%d")
GRAPH_PARAMS = {
    "date": DATE,
    "quantity": "9"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=POST_GRAPH_PIXEL_ENDPOINT, json=GRAPH_PARAMS, headers=headers)
# print(response)
print(DATE)

# https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915",
# "quantity":"5","optionalData":"{\"key\":\"value\"}"}' {"message":"Success.","isSuccess":true}