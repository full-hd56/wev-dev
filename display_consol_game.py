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
        self.frame_R = ui.CTkFrame(self.app, width=716, height=700)
        self.frame_R.place(x=300, y=0)

        # ======================
        # LABEL XY
        # ======================
        self.xy_label = ui.CTkLabel(self.app, text="Player x:0 y:0")
        self.xy_label.place(x=10, y=10)

        # ======================
        # BACKGROUND
        # ======================
        self.bg_img = ui.CTkImage(Image.open("home.jpg"), size=(716, 700))
        self.bg_label = ui.CTkLabel(self.frame_R, text="", image=self.bg_img)
        self.bg_label.place(x=0, y=0)

        # ======================
        # WALL POSITION
        # ======================
        # (x1,y1,x2,y2)
        self.walls = [

            (45,550,305,550),
            (385, 555, 660, 555)

        ]

        # ======================
        # PLAYER
        # ======================
        self.player_img = ui.CTkImage(Image.open("walk_point.png"), size=(30, 30))
        self.player = ui.CTkLabel(self.frame_R, text="", image=self.player_img)

        self.player_x = 300
        self.player_y = 300

        self.player.place(x=self.player_x, y=self.player_y)

        # ======================
        # KEY STATE
        # ======================
        self.keys = set()

        self.app.bind("<KeyPress>", self.key_press)
        self.app.bind("<KeyRelease>", self.key_release)

        self.app.focus_set()

        self.update()
        self.app.mainloop()

    # ======================
    # KEY
    # ======================
    def key_press(self, event):
        self.keys.add(event.keysym.lower())

    def key_release(self, event):
        self.keys.discard(event.keysym.lower())

    # ======================
    # CHECK WALL
    # ======================
    def can_move(self, x, y):

        for wall in self.walls:

            x1,y1,x2,y2 = wall

            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                return False

        return True

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

        if self.can_move(new_x,new_y):
            self.player_x = new_x
            self.player_y = new_y
            self.player.place(x=self.player_x,y=self.player_y)

        self.xy_label.configure(text=f"x:{self.player_x} y:{self.player_y}")

        self.app.after(16,self.update)


console()
