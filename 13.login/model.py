import pymongo
myclient = pymongo.MongoClient("mongodb+srv://saravanamuthusha:Register@cluster0.azsub.mongodb.net/")
db=myclient["vels"]


user =  db['student'].find_one ({
    "username":"venom",
    "password":"1"
    })
print(user)



# for x in db['student'].find():
#     print(x["_id"])