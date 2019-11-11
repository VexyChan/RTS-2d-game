import arcade
import pathlib
import random

class StructOBJ(arcade.Sprite):
    def __init__(self, texture_path: str, speed: int, game_window):
        super().__init__(texture_path)
        self.speed = speed
        self.game = game_window
        self.type="not defined"
        self.dmg=-1
        self.hp=-1
class GameConstructors(arcade.Window):

    def __init__(self, screen_w: int = 1024, screen_h: int = 1024):
        super().__init__(screen_w, screen_h)
        self.allyStructs=arcade.SpriteList()
        self.allyUnits=arcade.SpriteList()
        self.enemyStructs=arcade.SpriteList()
        self.enemyUnits=arcade.SpriteList()
        self.maplist = arcade.SpriteList()
        self.gui = arcade.SpriteList()
        self.pointer=arcade.SpriteList()
        #self.set_mouse_visible(False)

    def setup(self):
        self.cur = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "coursor.gif")
        self.cur.center_x = 700
        self.cur.center_y = 900
        self.cur.scale = 1 / 2
        self.pointer.append(self.cur)
        self.logo=arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "glogo.png")
        self.logo.center_x=700
        self.logo.center_y=900
        self.logo.scale=1/2
        self.gui.append(self.logo)


    def on_mouse_motion(self, x, y, dx, dy):
        self.pointer[0]. = x
        self.pointer[0].position_y = y
        if(arcade.check_for_collision(self.pointer[0],self.logo)==1):
            self.logo.scale=1
        else:
            self.logo.scale=1/2
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_update(self, delta_time: float):
        self.logo.scale=1/2
        #fireball.scale = 1 / 10

    def on_draw(self):
        arcade.start_render()
        self.maplist.draw()
        self.gui.draw()
        self.pointer.draw()

class selectC:
     def __init__(self, position_x, position_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

def main():
    window = GameConstructors()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()