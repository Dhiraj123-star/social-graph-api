from fastapi import APIRouter
from app.db import get_driver
from app.models import UserCreate, FriendRequest

router = APIRouter()
driver = get_driver()


@router.post("/users")
def create_user(user: UserCreate):
    with driver.session() as session:
        session.run("MERGE (u:User {name: $name})", name=user.name)
    return {"message": f"User '{user.name}' created"}


@router.post("/friends")
def add_friendship(request: FriendRequest):
    with driver.session() as session:
        session.run(
            """
            MATCH (a:User {name: $user1}), (b:User {name: $user2})
            MERGE (a)-[:FRIENDS_WITH]->(b)
            MERGE (b)-[:FRIENDS_WITH]->(a)
        """,
            user1=request.user1,
            user2=request.user2,
        )
    return {"message": f"{request.user1} and {request.user2} are now friends"}


@router.get("/friends/{username}")
def get_friends(username: str):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (:User {name: $username})-[:FRIENDS_WITH]->(f:User)
            RETURN f.name AS friend
        """,
            username=username,
        )
        return {"friends": [record["friend"] for record in result]}


@router.get("/mutual-friends")
def mutual_friends(user1: str, user2: str):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (a:User {name: $user1})-[:FRIENDS_WITH]->(f:User)<-[:FRIENDS_WITH]-(b:User {name: $user2})
            RETURN f.name AS mutual_friend
        """,
            user1=user1,
            user2=user2,
        )
        return {"mutual_friends": [record["mutual_friend"] for record in result]}
