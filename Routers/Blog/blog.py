from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel
from Routers.Account.UserAuth import authenticate_token
from firebase_admin import firestore, auth

router = APIRouter()

store = firestore.client()


class Post(BaseModel):
    title: str
    content: str


# Create a blog post

@router.post("/posts")
async def create_post(post: Post, user: str = Depends(authenticate_token)):
    try:
        title = post.title
        content = post.content
        author = user.display_name
        uid = user.uid
        data = {"title": title, "content": content, "author": author}
        transaction = store.transaction()
        post_id = store.collection("Blogs").document(uid).collection("UserPosts").document().id
        user_post_ref = store.collection("Blogs").document(uid).collection("UserPosts").document(post_id)
        transaction.set(user_post_ref, data)
        all_blogs_ref = store.collection("All Blogs").document(post_id)
        transaction.set(all_blogs_ref, data)
        transaction.commit()
        return {"message": "Blog post created successfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}
# Get all blogs of the current user
@router.get("/get_user_blogs")
async def get_user_blogs(current_user: str = Depends(authenticate_token)):
    try:
        uid = current_user.uid
        blogs_ref = store.collection("Blogs").document(uid).collection("UserPosts")
        docs = blogs_ref.get()
        blogs_data = []
        for doc in docs:
            blogs_data.append({"id": doc.id, **doc.to_dict()})
        return {"blogs": blogs_data}
    except Exception as e:
        return {"message": f"Error: {e}"}
    
@router.get("/blogs")
async def get_all_blogs():
    try:
        blogs_data = []
        blogs_ref = store.collection("All Blogs")
        query_snapshot = blogs_ref.get()
        for doc in query_snapshot:
            blogs_data.append(doc.to_dict())

        return {"blogs": blogs_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

@router.delete(f"/delete_blogs/{id}")
async def delete_blogs(id:str,current_user: str = Depends(authenticate_token)):
    try:
        blogs_ref = store.collection("Blogs").document(current_user.uid).collection("UserPosts").document(id)
        blogs_ref.delete()
        return {"message": "deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

@router.patch(f"/update_blogs/{id}")
async def delete_blogs(post: Post,id:str,current_user: str = Depends(authenticate_token)):
    try:
        data = {
            "title": post.title,
            "content": post.content
        }
        blogs_ref = store.collection("Blogs").document(current_user.uid).collection("UserPosts").document(id)
        blogs_ref.update(data)
        return {"message": "updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
