import pymongo
# below is url of server with userid and pw to connect with mongodb server
client = pymongo.MongoClient("mongodb+srv://aminravjani:Welcome1@cluster0.8pkesej.mongodb.net/?retryWrites=true&w=majority")
db = client.test # testing whether conenction is done
print(db)

# creating dictionary
d ={
    "name":"sudh",
    "email": "sudh@ineuron.ai",
    "surname": "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d) # unable to run this code.see lecture MongoDB 4 hr 11 min
https://github.com/aminravjani/testgitpush.git