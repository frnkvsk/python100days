import requests

TOKEN = "dakf78$202rslchmhfd93217ddye476"
BASE_URL = "https://pixe.la"
USERNAME = "frankv125"
CREATE_GRAPH_ENDPOINT = f"{BASE_URL}/v1/users/{USERNAME}/graphs"
GRAPH_CONFIG_PARAMS = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "steps",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=CREATE_GRAPH_ENDPOINT, json=GRAPH_CONFIG_PARAMS, headers=headers)
print(response)

# https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
# {"message":"Success.","isSuccess":true}