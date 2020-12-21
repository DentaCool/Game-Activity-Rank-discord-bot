import pymongo
from UserModel import *

mongo_url = ""
mongo_client = pymongo.MongoClient(mongo_url)

db = mongo_client['data']
users_col = db['users']


def add_profile(user):
    users_col.insert_one(user)


def get_all_users():
    users = list(users_col.find({}))
    return users


def get_user(username, discord_id):
    user = users_col.find_one({"discord_id": discord_id})
    if user is not None:
        return dict(user)
    user = UserData(discord_id, username)
    add_profile(user)
    return dict(users_col.find_one({"discord_id": discord_id}))


def update(user: UserData):
    users_col.find_one_and_replace(filter={"username": user.username}, replacement=user)
