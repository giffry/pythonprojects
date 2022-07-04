from Django.blog.models import users,posts

# username="anu"
# password="Password@123"

# user=[user for user in users if user["username"]==username and user["password"]==password]

session={}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)

        else:
            print("u must login")

    return wrapper

def Authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user

# print(Authenticate(username="anu",password="Password@123"))

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=Authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("login success")
        else:
            print("invalid")

class PostsView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts

    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["user"]=userId
        posts.append(kwargs)
        print(posts)

class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        print(userId)
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts

class PostDetailsView:

    def get_object(self,id):
        post=[post for post in posts if post["postId"]==id]
        return post

    @signin_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_object(post_id)

        return post

    @signin_required
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=self.get_object(post_id)
        if data:
            post=data[0]
            posts.remove(post)
            print("post removed")
            print(len(posts))

    def put(self,*args,**kwargs):

        post_id=kwargs.get("post_id")

        instance=self.get_object(post_id)
        data=kwargs.get("data")
        if instance:
            post_obj=instance[0]
            post_obj.update(data)
            return post_obj

class LikeView:
    @signin_required
    def get(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post)




# log=SignInView()
# log.post(username="jhon",password="Password@123")
# print(session)

# pst=PostsView()
# print(pst.get())
# pst.post(postId=9,
#          title="hello there",
#          content="dfghjk",
#          liked_by=[])

# mypost=MyPostListView()
# print(mypost.get())
# post_detail=PostDetailsView()
# post_detail.delete(post_id=6)
# print(post_detail.get(post_id=4))

data={
    "title":"hello there"
}

post_detail=PostDetailsView()

print(post_detail.put(post_id=4,data=data))


lkv=LikeView()
lkv.get(postid=6)











