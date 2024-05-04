from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from database import Database
import subprocess
import os

class testApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Login(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        self.db = Database(host='localhost', user='root', password='', database='todo')
        return testApp() 
    
    def validate_login(self):
        username = self.root.ids.UsernameLogin.text
        password = self.root.ids.PasswordLogin.text
        
        if not username or not password:
            self.root.ids.login_error_label.text = "Empty username or password"
            return
        
        if self.db.check_user(username, password):
            subprocess.Popen(["python", "main.py"])
            os._exit(0)
        else:
            self.root.ids.login_error_label.text = "Invalid credentials"

    def validate_signup(self):
        username = self.root.ids.Username.text
        password = self.root.ids.Password.text
        if not username or not password:
            self.root.ids.error_label.text = "Empty username or password"
            return
        signup_successful = self.db.signup(username, password)
        if signup_successful:
            self.root.ids.error_label.text = "Signup successful"
        else:
            self.root.ids.error_label.text = "Username already exists"
        

if __name__ == "__main__":
    Window.size = (778, 640)
    Builder.load_file("log.kv")
    Login().run()
