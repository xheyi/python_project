from blueprint import User
from post import Post
import datetime

post_date = datetime.datetime.now()
user_information = User("Awojobi Suleiman", "0902", "devops engineer", "awojobisuleiman1@gmail.com")
user_information.show_info()

user_information.change_job_title("cloud_engineer")
user_information.show_info()

user2 = User("awojobi tobi", "housd12", "web designer", "awotobi@gmail.com")
user2.show_info()

first_post = Post("this is my first message on this app", user_information.user_name, post_date)
first_post.show_posts()

