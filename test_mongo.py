from pymongo import MongoClient

MONGO_URI = "mongodb+srv://lakshmansanagapalli:KGD3m5bWxIr4MYed@linkedinclone.zyb3vfd.mongodb.net/?retryWrites=true&w=majority&appName=linkedinclone"

try:
    client = MongoClient(MONGO_URI)
    # Check connection by listing database names
    db_list = client.list_database_names()
    print("✅ Connected successfully! Available databases:", db_list)
except Exception as e:
    print("❌ Connection failed:", e)
finally:
    client.close()
