import customtkinter as ui
from PIL import Image

class console:
    def __init__(self):
        self.app = ui.CTk()
        self.app.title("client")
        self.app.geometry("1024x700")

        # แสดงพิกัด
        self.xy_label = ui.CTkLabel(self.app, text="x:0 y:0")
        self.xy_label.place(x=10, y=10)

        # พื้นหลัง
        self.img = ui.CTkImage(Image.open("home.jpg"), size=((1024*0.7), (1024*0.7)))
        self.bg_label = ui.CTkLabel(self.app, text="", image=self.img)
        self.bg_label.place(x=320, y=0)

        self.img = ui.CTkImage(Image.open("walk_point.png"), size=(10, 10))
        self.walk_label = ui.CTkLabel(self.app, text="", image=self.img)
        self.walk_label.place(x=434, y=747)

        # จับ event เมาส์
        self.app.bind("<Motion>", self.show_xy)

        self.app.mainloop()
