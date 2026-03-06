import customtkinter as ui
from PIL import Image


class console:
    def __init__(self):

        self.app = ui.CTk()
        self.app.title("client")
        self.app.geometry("1024x700")

        # ======================
        # FRAME MAP
        # ======================
        self.frame_R = ui.CTkFrame(self.app, width=716, height=700, corner_radius=10)
        self.frame_R.place(x=300, y=0)

        # ======================
        # LABEL SHOW XY
        # ======================
        self.xy_label = ui.CTkLabel(self.app, text="Player x:0 y:0")
        self.xy_label.place(x=10, y=10)

        # ======================
        # BACKGROUND
        # ======================
        self.bg_img = ui.CTkImage(Image.open("home.jpg"), size=(716, 700))
        self.bg_label = ui.CTkLabel(self.frame_R, text="", image=self.bg_img)
        self.bg_label.place(x=0, y=0)

        # wall
        self.collision = Image.open("collision_map.png").convert("L")

        # ======================
        # PLAYER
        # ======================
        self.player_img = ui.CTkImage(Image.open("walk_point.png"), size=(40, 40))

        self.player = ui.CTkLabel(self.frame_R, text="", image=self.player_img)

        self.player_x = 200
        self.player_y = 200

        self.player.place(x=self.player_x, y=self.player_y)

        # ======================
        # KEY STATE
        # ======================
        self.keys = set()

        self.app.bind("<KeyPress>", self.key_press)
        self.app.bind("<KeyRelease>", self.key_release)

        self.app.focus_set()

        # game loop
        self.update()

        self.app.mainloop()

    # ======================
    # KEY PRESS
    # ======================
    def key_press(self, event):
        self.keys.add(event.keysym.lower())

    def key_release(self, event):
        if event.keysym.lower() in self.keys:
            self.keys.remove(event.keysym.lower())

    def can_move(self, x, y):

        if x < 0 or y < 0 or x >= 716 or y >= 716:
            return False

        pixel = self.collision.getpixel((int(x), int(y)))

        return pixel > 200

    # ======================
    # GAME LOOP
    # ======================
    def update(self):

        speed = 5

        new_x = self.player_x
        new_y = self.player_y

        if "w" in self.keys:
            new_y -= speed

        if "s" in self.keys:
            new_y += speed

        if "a" in self.keys:
            new_x -= speed

        if "d" in self.keys:
            new_x += speed

        # ======================
        # LIMIT MAP
        # ======================
        if new_x < 0:
            new_x = 0

        if new_y < 0:
            new_y = 0

        if new_x > 676:
            new_x = 676

        if new_y > 660:
            new_y = 660

        if self.can_move(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y
            self.player.place(x=self.player_x, y=self.player_y)
        # move player
        # self.player.place(x=self.player_x, y=self.player_y)
        # update label
        self.xy_label.configure(text=f"Player x:{self.player_x} y:{self.player_y}")
        # loop
        self.app.after(16, self.update)
console()
