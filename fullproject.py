class Users:
    def __init__(self, name, job, email, password):
        self.name = name
        self.job = job
        self.email = email
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

    def change_job(self, new_job):
        self.job = new_job

    def show_personal_info(self):
        print(f"{self.name} is an {self.job}. contact him at {self.email}")


user3 = Users("ogbologbo", "akpayan", "oghologhoapayan@gmail.com", "1234")
user3.show_personal_info()

