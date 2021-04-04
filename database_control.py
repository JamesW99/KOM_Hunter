import pymongo

client = pymongo.MongoClient("mongodb+srv://kom_hunter_root:kom_hunter_root@cluster0.knj2e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
edinburghDB = client.edinburgh
collection = edinburghDB['Segment_detail']
dblist = client.list_database_names()
# dblist = client.database_names()   #python3.6 or lower

def upload_segment_to_database(aSegmentDict):
    """
    Check if the stage already exists
    if aSegmentDict['id'] exists
    skip
    else
    """
    all_record = []
    all_record.append(aSegmentDict)
    collection.insert_many(all_record)


if __name__ == '__main__':
    if "edinburgh" in dblist:
        print("The database already exists！")
