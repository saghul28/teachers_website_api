from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel
from Routers.Account.UserAuth import authenticate_token
from firebase_admin import firestore, auth
router = APIRouter()
store = firestore.client()

class Comment(BaseModel):
    content: str

@router.post("/comments/{post_id}")
async def create_comment(post_id:str,comment: Comment, current_user: str = Depends(authenticate_token)):
    try:
        data = {
            "content": comment.content,
            "post_id": post_id,
            "user_uid": current_user.uid
        }
        comment_ref = store.collection("Comments").document()
        comment_ref.set(data)
        return {"message": "Comment created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

@router.get("/comments/{post_id}")
async def get_comments(post_id: str,current_user: str = Depends(authenticate_token)):
    try:
        comments_ref = store.collection("Comments").where("post_id", "==", post_id)
        docs = comments_ref.get()
        comments_data = []
        for doc in docs:
            comment_data = doc.to_dict()
            comments_data.append({"id": doc.id, "content": comment_data["content"]})
        return {"comments": comments_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

@router.delete("/delete_comments/{id}")
async def delete_comments(id: str,current_user: str = Depends(authenticate_token)):
    try:
        comment_ref = store.collection("Comments").document(id)
        comment_ref.delete()
        return {"message": "Comment deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

@router.patch("/update_comments/{id}")
async def update_comments(comment: Comment, id: str,current_user: str = Depends(authenticate_token)):
    try:
        data = {
            "content": comment.content,

            "user_uid": comment.user_uid
        }
        comment_ref = store.collection("Comments").document(id)
        comment_ref.update(data)
        return {"message": "Comment updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")