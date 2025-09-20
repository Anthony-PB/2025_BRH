from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import Dict, List, Optional
from django.db import connections

# --- Connection Setup (The Django Way) ---
# Django manages the database connection based on your settings.py.
# We get the 'default' database connection from Django's connection handler.
# This is the single source of truth for your database connection.
connection = connections['default']
db = connection.client[connection.settings_dict['NAME']]

users = db['users']
articles = db['articles']
sources = db['sources']

# Write functions here