from pymongo import MongoClient
uri = "mongodb+srv://playindrajitdas10_db_user:Indra12345@cluster0.ctsz3l7.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)