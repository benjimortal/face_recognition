from classes.post import Post
class User:
    def __init__(self,user_email, name, password, current_job_title, skills):
        self.user_email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title
        self.skills = skills


    def change_password(self, new_password):
        self.password = new_password


    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title


    def skills(self, new_skill):
        self.skills = new_skill


    def get_user_info(self):
        print(f'User {self.name} currently works as a {self.current_job_title}. You can contact them at : {self.user_email} and its skills are {self.skills}!!')



app_user_one = User('jawidskim@outlook.com', 'Jawid', 'rjm96', 'developer', 'football')
app_user_one.change_job_title('programming'.upper())

app_user_two = User('reyhan@hotmail.com', 'Queen', 'jrm69', 'khayat', 'shena')
new_post = Post('on a secret mission', app_user_one.name)

