class User:
    def __init__(self, name, password, job_title, email):
        self.user_name = name
        self.password = password
        self.job_title = job_title
        self.email = email

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def show_info(self):
        print(f"i am {self.user_name} a {self.job_title}, you can contact me at {self.email}")