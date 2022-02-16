from pymongo import MongoClient

client = MongoClient('localhost', 27017)

local_database = client['local']
collection_names = local_database.list_collection_names()

sample_database = client['collection-2--8667220554415667166']

print(local_database)

print(collection_names)


print(sample_database.list_collection_names())

sessions = local_database.sessions.posts
print(sessions)

print(sessions.find_one())
