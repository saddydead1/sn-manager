import customtkinter as ctk
import http_client as http
from user import User

log_in = False


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.snmtext = ctk.CTkLabel(self, text="Sonoma Manager v3")
        self.snmtext.pack(anchor="center")

        self.username = ctk.CTkEntry(self, placeholder_text="Username")
        self.username.pack(anchor="center")

        self.password = ctk.CTkEntry(self, placeholder_text="Password")
        self.password.configure(show="*")
        self.password.pack(anchor="center")

        self.log_button = ctk.CTkButton(self, text="Log in",
                                        command=lambda: http.login(User(self.username.get(), self.password.get())))
        self.log_button.pack(anchor="center")


def login():


    log_in = True


def logout():


    log_in = False