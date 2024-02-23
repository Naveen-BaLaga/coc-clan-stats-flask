from decouple import config
import pymongo
import sys

MONGODB_CONNECTION_STRING = config('MONGODB_CONNECTION_STRING')
DB_NAME = config('DB_NAME')
TABLES_COLLECTION_NAME = config('TABLES_COLLECTION_NAME')

try:
  client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received.")
  sys.exit(1)
  
def get_tables_data(table_name):
    try:
        db = client[DB_NAME]
        collection = db[TABLES_COLLECTION_NAME]

        # Find entry with key "Table Name" equal to the passed parameter table_name
        entry = collection.find_one({"Table Name": table_name})
        if entry:
            # Check if "Table Data" key exists in the entry
            if "Table Data" in entry:
                return {"status": "Success", "payload": entry["Table Data"]}
            else:
                return {"status": "Failure", "payload": "No 'Table Data' key in the entry."}
        else:
            return {"status": "Failure", "payload": "No entry with the specified 'Table Name' found."}

    except Exception as e:
        return {"status": "Failure", "payload": str(e)}