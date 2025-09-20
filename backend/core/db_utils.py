from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import Dict, List, Optional
from django.db import connections
from .schemas import *

# --- Connection Setup (The Django Way) ---
# Django manages the database connection based on your settings.py.
# We get the 'default' database connection from Django's connection handler.
# This is the single source of truth for your database connection.
connection = connections['default']
db = connection.client[connection.settings_dict['NAME']]

users = db['users']
articles = db['articles']
sources = db['sources']

# --- Helper Function (Internal Use Only) ---
def _serialize_document(doc: Dict) -> Dict:
    """
    Converts a document's '_id' from ObjectId to a JSON-friendly string.
    """
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc


# Write functions here

def create_user(user_data: Dict) -> str:
    """
    Inserts a new user document into the database.

    Args:
        user_data: A dictionary of user data, already validated and processed
                   by the UserRegistrationSerializer. It is expected to contain
                   the 'password_hash', NOT the plain-text password.

    Returns:
        The json representation of the new user.
    """
    result = users.insert_one(user_data)
    # 2. Immediately fetch the document we just created using its new ID.
    #    We can reuse our existing get_user_by_id function for this!
    new_user_id = str(result.inserted_id)
    created_user_document = get_user_by_id(new_user_id)
    
    return created_user_document

def get_all_users() -> List[Dict]:
    """
    Fetches all users from the database.
    """
    cursor = users.find({})
    return [_serialize_document(doc) for doc in cursor]


def update_user(user_id: str, update_data: Dict) -> bool:
    """
    Updates a user document.
    """
    result = users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )
    return result.modified_count > 0


def delete_user(user_id: str) -> bool:
    """
    Deletes a user document.
    """
    result = users.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0

def get_user_by_id(user_id: str) -> Optional[Dict]:
    """
    Fetches a single user by their ID string and validates its shape.
    """
    try:
        user_doc = users.find_one({"_id": ObjectId(user_id)})
        if not user_doc:
            return None
        validated_user = UserDBSchema.model_validate(user_doc)
        # Serialize the validated model back to a dict for the API
        serialized_user = _serialize_document(validated_user.model_dump())
        return serialized_user
    except ValidationError as e:
        # TODO: Log error
        print(f"ERROR: Data for user {user_id} is invalid: {e}")
        return None
    except Exception:
        return None