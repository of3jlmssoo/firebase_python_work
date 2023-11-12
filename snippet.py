# https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#get
# https://googleapis.dev/nodejs/firestore/latest/CollectionReference.html#listDocuments


# Project name Firebase-Flutter-Codelab
# Project ID fir-flutter-codelab-aec96
import firebase_admin
from firebase_admin import auth

from firebase_admin import credentials
from firebase_admin import firestore
import os
import uuid
os.environ["FIRESTORE_EMULATOR_HOST"]="localhost:8080"
os.environ["GCLOUD_PROJECT"]="fir-flutter-codelab-aec96"

def queryReports(user):
    reports = []
    doc_ref = db.collection('users').document(user).collection("reports")
    for doc in doc_ref.list_documents():
        print('doc:',doc.id)
        reports.append(doc.id)
    return reports
    print("--------")

def queryExpences(user,report):
    reports = []
    doc_ref = db.collection('users').document(user).collection("reports").document(report).collection("expences")
    for doc in doc_ref.list_documents():
        print('doc:',doc.id)
        reports.append(doc.id)
    return reports
    print("--------")

def addData():
    dref = db.collection("users").document(user1).collection("reports").document(report1).collection("expences")
    dref.add({"date": "2023/11/01", "type":"公共交通機関"})
    dref = db.collection("users").document(user1).collection("reports").document(report1).collection("expences")
    dref.add({"date": "2023/11/02", "type":"公共交通機関"})
    dref = db.collection("users").document(user1).collection("reports").document(report1).collection("expences")
    dref.add({"date": "2023/11/03", "type":"公共交通機関"})

    dref = db.collection("users").document(user1).collection("reports").document(report2).collection("expences")
    dref.add({"date": "2023/11/01", "type":"公共交通機関"})
    dref = db.collection("users").document(user1).collection("reports").document(report2).collection("expences")
    dref.add({"date": "2023/11/02", "type":"公共交通機関"})
    dref = db.collection("users").document(user1).collection("reports").document(report2).collection("expences")
    dref.add({"date": "2023/11/03", "type":"公共交通機関"})


    dref = db.collection("users").document(user2).collection("reports").document(report1).collection("expences")
    dref.add({"date": "2023/11/01", "type":"公共交通機関"})
    dref = db.collection("users").document(user2).collection("reports").document(report1).collection("expences")
    dref.add({"date": "2023/11/02", "type":"公共交通機関"})
    dref = db.collection("users").document(user2).collection("reports").document(report1).collection("expences")
    dref.add({"date": "2023/11/03", "type":"公共交通機関"})

    dref = db.collection("users").document(user2).collection("reports").document(report2).collection("expences")
    dref.add({"date": "2023/11/01", "type":"公共交通機関"})
    dref = db.collection("users").document(user2).collection("reports").document(report2).collection("expences")
    dref.add({"date": "2023/11/02", "type":"公共交通機関"})
    dref = db.collection("users").document(user2).collection("reports").document(report2).collection("expences")
    dref.add({"date": "2023/11/03", "type":"公共交通機関"})
        

print("uuid5:",uuid.uuid4())

cred = credentials.Certificate("./fir-flutter-codelab-aec96-firebase-adminsdk-5t2nn-0b706966b4.json")
app = firebase_admin.initialize_app(cred)
print("cred:",cred)

# user = credentials.Certificate.get_access_token[app['idToken']]
# print(user['uid'])

print("uid:",auth.UserInfo.uid.getter)

# /users/{userid}/exchange/{exchangeid}/transactions/{transaction}
# /users/{user}/reports/{report}/expences/{expense}
user1 = "user1"
user2 = "user2"
report1 = "report1"
expence11 = "exp11"
expence12 = "exp12"
expence13 = "exp13"
report2 = "report2"
expence21 = "exp21"
expence22 = "exp22"
expence23 = "exp23"


db = firestore.client()
print("db:",db)

# addData()


# doc_ref = db.collection("users").document("reports")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
#
# room_a_ref = db.collection("rooms").document("roomA")
# message_ref = room_a_ref.collection("messages").document("message1")



# dref = db.collection("users").document(user).collection("reports").document(report).collection("expences").document(expence1)
# dref.set({"date": "2023/11/01", "type":"公共交通機関"})
# dref = db.collection("users").document(user).collection("reports").document(report).collection("expences").document(expence2)
# dref.set({"date": "2023/11/02", "type":"公共交通機関"})
# dref = db.collection("users").document(user).collection("reports").document(report).collection("expences").document(expence3)
# dref.set({"date": "2023/11/03", "type":"公共交通機関"})


# qrefUsers = db.collections("users")
# print(qrefUsers)
# for user in qrefUsers:
#     print("user:",user)

print("--------")
# docs = db.collection("users").stream()
# print("docs",docs)


doc_ref = db.collection("users").document("abcdefghijkl").collection("reports").document("mnopqrstu").collection("expences").document("LuGG0HSQ3J3tO0QmkvDl")

doc = doc_ref.get()
if doc.exists:
    print(f"Document data: {doc.to_dict()}")
else:
    print("No such document!")    
print("--------")
# doc_ref = db.collection('users').document(user1).collection("reports")
# for doc in doc_ref.list_documents():
#     print('doc:',doc.id)
# print("--------")

# doc_ref = db.collection('users').document(user2).collection("reports")
# for doc in doc_ref.list_documents():
#     print('doc:',doc.id)
print(queryReports(user1))
print(queryReports(user2))
userReports = queryReports(user1)
print(userReports)
print("--------")

for report in userReports:
    print(queryExpences(user1,report))
