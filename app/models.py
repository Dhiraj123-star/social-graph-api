from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str


class FriendRequest(BaseModel):
    user1: str
    user2: str
