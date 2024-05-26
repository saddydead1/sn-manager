import customtkinter as ctk
import login_screen
import main_screen


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Sonoma Manager v3")

        self.login_frame = login_screen.LoginFrame(master=self)
        self.login_frame.pack(anchor="center")


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.title("Sonoma Manager v3")


def main():
    if not login_screen.log_in:
        log = LoginWindow()
        log.mainloop()

        print(1)
    else:
        main = MainWindow()
        main.mainloop()


if __name__ == "__main__":
    main()

