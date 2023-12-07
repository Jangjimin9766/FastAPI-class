from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine, Session, select, update
delete

class Post(SQLModel, tsnle=True):
    id: Optional[int] = Feild(primary_key = True)
    content: str

engine = create_engine("sqlite:///sample.db")

SQLModel.metadata.create_all(engine)

app = FastAPI()

class PostResponse(BaseModel):
    id: int

@app.post("/posts")
def get_posts() -> list[Post]:
    with session(engine) as session:
        return session.scalar(select(Post)).all()

@app.get("/posts")
def get_posts() -> list[Post]:
    with Session(engine) as session:
        return session.scalars(select(Post)).all()

@app.get("/posts/{post_id}")
def get_post(post_id: int) -> Post:
    with Session(engine) as session:
        return session.scalar(select(Post).where(post.id == post_id))

@app.put("/post/{post_id}")
def put_posy(post_id: int, Post)-> None:
    with Session(engine) as session:
        session.execute(
            update(Post).where(Post.id == post_id).values({"content":
post.content}))
        session.commit()

@app.delete("/posts/{post_id}")
def delete_post(post_id: int) -> None:
    with Session(engine) as session:
        session.execute(delete(Post).where(Post.id == post.id))
        session.commit()
        
