# This is a sample Python script.
from datetime import datetime

import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
db = client["vocab"]
dbs = client.list_database_names()
vocab_col = db["vocab_list"]
vocab_dict = {'word': 'cryptic', 'definition': 'secret with hidden meaning'}
res = vocab_col.insert_one(vocab_dict)
print("inserted_id: ", res.inserted_id)
if "vocab" in dbs:
    print("Database exists")


def print_hi():
    fh = open("Vocabulary_set.csv", "r")
    wd_list = fh.readlines()
    wd_list.pop(0)
    vocab_list = []
    for rawstring in wd_list:
        word, definition = rawstring.split(',', 1)
        definition = definition.rstrip()
        vocab_list.append({'word': word, 'definition': definition})
    # print(vocab_list)
    # res = vocab_col.insert_many(vocab_list)
    # print(res.inserted_ids)
    # data = vocab_col.find_one()
    # print("data: ",data)
    # for data in vocab_col.find({},{"_id":0,"definition":0}):
    #    print(data)
    data = vocab_col.find_one({'word': 'boisterous'})
    print("data: ", data)
    upd = vocab_col.update_one({'word': 'boisterous'}, {'$set': {'definition': 'noisy and rowdy'}})
    print("updated: ", upd.modified_count)

    data = vocab_col.find_one({'word': 'boisterous'})
    print("data: ", data)

    upd = vocab_col.update_many({}, {"$set": {"last_updated UTC:": datetime.utcnow().strftime('%Y-%m-%d%H:%M'
                                                                                              ':%SZ')}})
    print("updated: ", upd.modified_count)


if __name__ == '__main__':
    print_hi()
