import requests

Token = requests.post("http://127.0.0.1:8000/account/api/token/",json={
    "username":"abinash",
    "password":"abinash"
})

token=Token.json()
# mytoken= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyOTEyOTI4LCJpYXQiOjE3MzI5MTI2MjgsImp0aSI6ImMzYmYxOTU4OGVkYjQxZmQ5NGRiYWYyYjJlYzlhMmI3IiwidXNlcl9pZCI6Mn0.UHX-AXPi4d2GndqPsm4LscGKuxHX2f12AegctMzY3G4'
# print(token)
mytoken=token['access']
myurl='http://127.0.0.1:8000/reservation/reservation_views/'
# headers = {'content-type': 'application/json'}
data1={
        "check_in": "2025-11-26",
        "check_out": "2025-11-26",
        "status": "pending",
        "guest_id": 1,
        "room_id": 1
}
response = requests.post(myurl,headers={ 'Authorization': f'Bearer {mytoken}' },json=data1)
print(response.status_code)
data =response.json()

print(data)
# 
# print('abi') 