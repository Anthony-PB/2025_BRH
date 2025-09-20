from pydantic import *
from typing import Optional

# This UserSchema is needed by the 'users' app and potentially
# the 'articles' app (to show an author). So it belongs here.
class UserDBSchema(BaseModel):
    email: EmailStr
    display_name: Optional[str]
    password_hash: SecretStr

    # List of 'str' that is actually based on a MongoDB ObjectId type for Sources
    sources: list[str] = []

    # List of 'str' that is actually based on a MongoDB ObjectID type for Articles
    liked_posts: list[str] = []

    class Config:
        extra = "allow"

class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    confirm_password: SecretStr

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'UserRegisterSchema':
        pw1 = self.password.get_secret_value()
        pw2 = self.confirm_password.get_secret_value()
        if pw1 is not None and pw1 != pw2:
            raise ValueError('Passwords do not match')
        return self

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
