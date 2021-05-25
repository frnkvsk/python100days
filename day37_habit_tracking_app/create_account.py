import requests


BASE_URL = "https://pixe.la"
CREATE_ACCOUNT_ENDPOINT = f"{BASE_URL}/v1/users"
USER_PARAMS = {
    "token":"",
    "username":"frankv125",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=CREATE_ACCOUNT_ENDPOINT, json=USER_PARAMS)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@frankv125 , it is your profile page!","isSuccess":true}