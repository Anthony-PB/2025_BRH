from pydantic import BaseModel, SecretStr, EmailStr, Field
from typing import Optional

# This UserSchema is needed by the 'users' app and potentially
# the 'articles' app (to show an author). So it belongs here.
class UserSchema(BaseModel):
    username: EmailStr
    display_name: str
    password: SecretStr

    # List of 'str' that is actually based on a MongoDB ObjectId type for Sources
    sources: list[str] = []

    # List of 'str' that is actually based on a MongoDB ObjectID type for Articles
    liked_posts: list[str] = []

    class Config:
        extra = "allow"

class SourceSchema(BaseModel):
    rssfeed: bool
    resource_uri: str

    # List of 'str' that is actually based on a MongoDB ObjectID type for Users
    users: list[str] = []

class ArticleSchema(BaseModel):
    # 'str' is actually MongoDB ObjectID type for Source
    source: str

    # A way to get to the specific post from the source
    post_url: str

    # List of 'str' that is actually based on a MongoDB ObjectID type for Users
    users: list[str] = []
