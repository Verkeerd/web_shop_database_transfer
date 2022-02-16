import pymongo

client = pymongo.MongoClient("mongodb+srv://verkeerd:uhsxqz%25%23BD078@projectrecomendationeng.ogvrf.mongodb.net/"
                             "projectRecomendationEngine?retryWrites=true&w=majority")

project_db = client.projectRecomendationEngine

collection_sessions = project_db.sessions

print(collection_sessions.find_one())