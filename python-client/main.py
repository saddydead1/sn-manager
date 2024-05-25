import customtkinter as ctk
import login_screen
import main_screen
from threading import Thread


class LoginThread(Thread):
    def __init__(self, name, func):
        Thread.__init__(self)
        self.name = name
        self.func = func

    def run(self):
        self.func()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Sonoma Manager v3")
        LoginThread.run("log in check", self.check_log_in())

    def check_log_in(self):
        if not login_screen.log_in:
            self.login_frame = login_screen.LoginFrame(master=self)
            self.login_frame.pack(anchor="center")
        else:
            self.test = ctk.CTkLabel(text='123')
            self.test.pack()
            self.login_frame.destroy()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

