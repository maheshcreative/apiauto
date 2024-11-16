#API service layer that calls the apiclient for business logic and datatrans

from apiclient import APIClient
class APIService:

    def get_posts(self):
        # Fetches all posts from teh API
        response = APIClient.get("/posts")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch posts: {response.status_code}")
    def get_post(self, post_id)
        response = APIClient.get(f"/posts/{post_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch post: {response.status_code}")
    def create_post(self,title,body,user_id):
        #create a new post via API
        data = {
            "title":title,
            "body":body,
            "user_id":user_id
        }
        response = APIClient.post("/posts",data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create post: {response.status_code}")