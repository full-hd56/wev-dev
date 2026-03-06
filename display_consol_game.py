import customtkinter as ui
from PIL import Image

class console:
    def __init__(self):
        self.app = ui.CTk()
        self.app.title("client")
        self.app.geometry("1024x700")

        # Frame
        self.frame_R = ui.CTkFrame(self.app, width=716, height=700, corner_radius=10)
        self.frame_R.place(x=300, y=0)

        # แสดงพิกัด
        self.xy_label = ui.CTkLabel(self.app, text="x:0 y:0")
        self.xy_label.place(x=10, y=10)

        # พื้นหลัง (อยู่ใน frame)
        self.bg_img = ui.CTkImage(Image.open("home.jpg"), size=(716, 716))
        self.bg_label = ui.CTkLabel(self.frame_R, text="", image=self.bg_img)
        self.bg_label.place(x=0, y=0)

        # จุดเดิน
        self.walk_img = ui.CTkImage(Image.open("walk_point.png"), size=(30, 30))
        self.walk_label = ui.CTkLabel(self.frame_R, text="", image=self.walk_img)
        self.walk_label.place(x=20, y=20)

        # จับ event เมาส์
        #self.frame_R.bind("<Motion>", self.show_xy)
        self.app.bind("<Motion>", self.show_xy)

        self.app.mainloop()

    def show_xy(self, event):
        x = event.x
        y = event.y
        self.xy_label.configure(text=f"x:{x} y:{y}")

console()
