import fullproject
import datetime

time_posted = datetime.datetime.now()


class Post:
    def __init__(self, message, author, time):
        self.message = message
        self.author = author
        self.time = time

    def show_posts(self):
        print(f"{self.message} posted by {self.author}on {self.time}")


user_posts = Post("this is my second message on the app", fullproject.user3.name, time_posted)
user_posts.show_posts()


