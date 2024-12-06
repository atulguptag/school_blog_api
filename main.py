import models
from typing import List
from bson import ObjectId
from fastapi import FastAPI, HTTPException
from pymongo.collection import ReturnDocument
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.school_blog
collection = db.posts


@app.post("/posts/", response_model=models.BlogPostInDB)
async def create_post(post: models.BlogPost):
    post_data = post.model_dump()
    result = await collection.insert_one(post_data)
    new_post = await collection.find_one({"_id": result.inserted_id})
    return {**new_post, "id": str(new_post["_id"])}


@app.get("/posts/{post_id}", response_model=models.BlogPostInDB)
async def read_post(post_id: str):
    post = await collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {**post, "id": str(post["_id"])}


@app.get("/posts/", response_model=List[models.BlogPostInDB])
async def read_posts():
    cursor = collection.find({})
    posts = await cursor.to_list(length=100)
    return [{**post, "id": str(post["_id"])} for post in posts]


@app.put("/posts/{post_id}", response_model=models.BlogPostInDB)
async def update_post(post_id: str, post: models.BlogPost):
    post_data = post.model_dump()
    updated_post = await collection.find_one_and_update(
        {"_id": ObjectId(post_id)},
        {"$set": post_data},
        return_document=ReturnDocument.AFTER
    )
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {**updated_post, "id": str(updated_post["_id"])}


@app.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    result = await collection.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
