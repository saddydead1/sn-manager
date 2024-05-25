import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Sonoma Manager v3")




def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

