import customtkinter as ui
from PIL import Image

class console:
    def __init__(self):
        self.app = ui.CTk()
        self.app.title("client")
        self.app.geometry("1024x700")
        self.map_w = 716
        self.map_h = 700
        self.keys = {"w": False, "a": False, "s": False, "d": False}

        self.my_x = 200
        self.my_y = 650
        self.speed = 2

        # Frame
        self.frame_R = ui.CTkFrame(self.app, width=self.map_w, height=self.map_h, corner_radius=10)
        self.frame_R.place(x=300, y=0)

        # แสดงพิกัด
        self.xy_label = ui.CTkLabel(self.app, text="x:0 y:0")
        self.xy_label.place(x=10, y=10)

        # พื้นหลัง
        self.bg_img = ui.CTkImage(Image.open("home.jpg"), size=(716, 716))
        self.bg_label = ui.CTkLabel(self.frame_R, text="", image=self.bg_img)
        self.bg_label.place(x=0, y=0)

        # จุดเดิน
        self.walk_img = ui.CTkImage(Image.open("walk_point.png"), size=(25, 25))
        self.walk_label = ui.CTkLabel(self.frame_R, text="", image=self.walk_img)
        self.walk_label.place(x=200, y=650)

        # player
        self.player_img = ui.CTkImage(Image.open("player.png"), size=(30, 30))
        self.player_label = ui.CTkLabel(self.frame_R, text="", image=self.player_img)
        self.player_label.place(x=self.my_x, y=self.my_y)

        #wall
        self.collision = Image.open("collision_map.png").convert("L")

        # keyboard control
        #self.app.bind("<Key>", self.move_player)
        self.update_player()
        self.app.bind("<KeyPress>", self.key_press)
        self.app.bind("<KeyRelease>", self.key_release)

        # เมาส์
        self.app.bind("<Motion>", self.show_xy)

        self.app.mainloop()

    def key_press(self, event):
        if event.char in self.keys:
            self.keys[event.char] = True

    def key_release(self, event):
        if event.char in self.keys:
            self.keys[event.char] = False

    def update_player(self):

        new_x = self.my_x
        new_y = self.my_y

        if self.keys["w"]:
            new_y -= self.speed
        if self.keys["s"]:
            new_y += self.speed
        if self.keys["a"]:
            new_x -= self.speed
        if self.keys["d"]:
            new_x += self.speed

        if self.can_move(new_x, new_y):
            self.my_x = new_x
            self.my_y = new_y
            self.player_label.place(x=self.my_x, y=self.my_y)

        self.app.after(16, self.update_player)  # ~60 FPS

    def can_move(self, x, y):

        if x < 0 or y < 0 or x >= 716 or y >= 716:
            return False

        pixel = self.collision.getpixel((int(x), int(y)))

        return pixel > 200

    def move_player(self, event):

        new_x = self.my_x
        new_y = self.my_y

        if event.char == "w":
            new_y -= self.speed
        elif event.char == "s":
            new_y += self.speed
        elif event.char == "a":
            new_x -= self.speed
        elif event.char == "d":
            new_x += self.speed

        if self.can_move(new_x, new_y):
            self.my_x = new_x
            self.my_y = new_y
            self.player_label.place(x=self.my_x, y=self.my_y)


    def show_xy(self, event):
        x = event.x
        y = event.y
        self.xy_label.configure(text=f"x:{x} y:{y}")

console()
