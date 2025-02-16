from flask import current_app
from pymongo.errors import PyMongoError

class UserRepository:
    @staticmethod
    def get_all_data():
        try:
            # Access the MongoDB collection
            collection = current_app.db['Users']
            
            # Fetch all documents
            data = collection.find()
            data_list = list(data)

            # Convert _id to string for JSON serialization
            for item in data_list:
                item['_id'] = str(item['_id'])

            return data_list
        except PyMongoError as e:
            # Handle any database errors
            current_app.logger.error(f"Error fetching data from MongoDB: {e}")
            return None
