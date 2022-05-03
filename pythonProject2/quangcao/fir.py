import pyrebase
config = {
    "apiKey": "AIzaSyATfhIehc5XZThp6Z3Mc4xeeZzfgy33Iks",
    "authDomain": "doantn-e31d0-default-rtdb.firebaseio.com",
    "databaseURL": "https://doantn-e31d0-default-rtdb.firebaseio.com",
    "storageBucket": "doantn-e31d0",
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()
print("##############################")
people=db.child("diekien").get()
print(people.val())
db.update({"Next":True})
# import requests
# import json
# firebaseurl="https://doantn-e31d0-default-rtdb.firebaseio.com/.json"
# #requests.patch(url=firebaseurl,json=json.loads(json_data)
# PARAMS = {'dieukien':True}
# r=requests.get(url=firebaseurl)
# data = r.json()
# print(data)