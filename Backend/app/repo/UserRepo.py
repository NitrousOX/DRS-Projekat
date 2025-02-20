from flask import current_app
from bson import ObjectId
from app.models.User import User

def convert_id_to_str(item):
    if '_id' in item:
        item['_id'] = str(item['_id'])
    return item

class UserRepository:
    @staticmethod
    def get_all_data():
        collection = current_app.db['Users']
        data = collection.find()
        data_list = list(data)
        data_list = [convert_id_to_str(item) for item in data_list]
        return data_list

    @staticmethod
    def get_user_by_id(user_id):
        collection = current_app.db['Users']
        user = collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user = convert_id_to_str(user)  # Convert _id to string
        return user

    @staticmethod
    def get_user_by_email(email):
        collection = current_app.db['Users']
        user = collection.find_one({"email": email})
        if user:
            user = convert_id_to_str(user)  # Convert _id to string
        return user

    @staticmethod
    def create_user(user: User):
        collection = current_app.db['Users']
        user_dict = user.to_dict()
        result = collection.insert_one(user_dict)
        return result.inserted_id

    @staticmethod
    def update_user(user_id, updated_data):
        collection = current_app.db['Users']
        updated_data = {key: value for key, value in updated_data.items() if value is not None}
        result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_data})
        return result.modified_count > 0

    @staticmethod
    def delete_user(user_id):
        collection = current_app.db['Users']
        result = collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
