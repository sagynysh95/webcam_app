from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure


def mongo_connect():
    uri = "mongodb+srv://user:qW12eRsag@cluster0.gvaf1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # uri = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.3"
    try:
        client = MongoClient(uri)
        print("Подключен к БД")
        db = client.face_data_db
        coll = db.face_data_coll
        return client, coll
    except ConnectionFailure:
        print("Не подключен к БД")


def mongo_insert(id, time, link):
    coll = mongo_connect()[1]
    print('Есть подключение к МОНГО')
    coll.insert_one({'_id': id, 'datetime': time, 'link': link})
    print("")
    print('Данные введены в БД')
    # res = coll.find()
    # for i in res:
    #     print(i)

    # res = coll.find()
    # for i in res:
    #     print(i)
    # # coll.insert_one({'_id': 3, 'name': 'Sagynysh'})


def mongo_get():
    coll = mongo_connect()[1]
    result = coll.find()
    return result
    # print('Не доступа к Монго')
    # return False

def mongo_get_image_by_id(id):
    coll = mongo_connect()[1]
    query = {"_id": id}
    result = coll.find_one(query, {"_id": 0, "link": 1})
    # print(result['link'])
    return result['link']




# mongo_get_image_by_id("e9be5678-a03d-4a4e-9528-bf8a6ea20791")

