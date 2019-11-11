import arcade
import pathlib
import random
import pyglet

MAP=0
WIDTH =1400
HEIGHT =1200
SPRITE_SCALING = 0.5
WFO=1
MFO=1
FFO=1

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.gui = arcade.SpriteList()
        self.pointer = arcade.SpriteList()
        self.so=arcade.load_sound("Assets/Mysterious-piano.mp3")
        arcade.play_sound(self.so)
        self.cur = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "coursor.gif")
        self.cur.center_x = 700
        self.cur.center_y = 900
        self.cur.scale = 1 / 2
        self.pointer.append(self.cur)
        self.CASTLE= arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "castle.jpg")
        self.CASTLE.center_x = 600
        self.CASTLE.center_y = 800
        self.CASTLE.scale = 4
        self.gui.append(self.CASTLE)
        self.logo = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "glogo.png")
        self.logo.center_x = 800
        self.logo.center_y = 1100
        self.logo.scale = 10 / 12
        self.gui.append(self.logo)
        self.bt1 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "playmap1.png")
        self.bt1.center_x = 200
        self.bt1.center_y = 900
        self.bt1.scale = 7/12
        self.gui.append(self.bt1)
        self.bt2 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "playmap3.png")
        self.bt2.center_x = 200
        self.bt2.center_y = 700
        self.bt2.scale = 7/12
        self.gui.append(self.bt2)
        self.bt3 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "playmap2.png")
        self.bt3.center_x = 200
        self.bt3.center_y = 800
        self.bt3.scale = 7/12
        self.gui.append(self.bt3)
    def on_draw(self):
        arcade.start_render()
        self.gui.draw()
        self.pointer.draw()
    def on_mouse_motion(self, x, y, dx, dy):
        self.pointer[0].center_x = x
        self.pointer[0].center_y = y
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if(arcade.check_for_collision(self.pointer[0],self.bt1)==True):
            instructions_view = GameView()
            MAP = 1
            self.window.show_view(instructions_view)
        elif(arcade.check_for_collision(self.pointer[0],self.bt2)==True):
            instructions_view = GameView()
            MAP = 2
            self.window.show_view(instructions_view)
        elif(arcade.check_for_collision(self.pointer[0],self.bt3)==True):
            instructions_view = GameView()
            MAP=3
            self.window.show_view(instructions_view)
        else:
            pass

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Sprite lists
        self.allyStructs = arcade.SpriteList()
        self.allyUnits = arcade.SpriteList()
        self.enemyStructs = arcade.SpriteList()
        self.enemyUnits = arcade.SpriteList()
        self.map = arcade.SpriteList()
        self.pointer = arcade.SpriteList()
        self.cur = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "coursor.gif")
        self.cur.center_x = 700
        self.cur.center_y = 900
        self.cur.scale = 1 / 2
        self.pointer.append(self.cur)
        self.Wood=250
        self.Food=100
        self.Metal=25
        self.tc=0
        #if(MAP==1):
        print(MAP)
        self.map_location = pathlib.Path.cwd() / 'Assets' / 'WarFrontMap1.tmx'
        my_map = arcade.tilemap.read_tmx(self.map_location)
        self.map = arcade.tilemap.process_layer(my_map, 'Tile Layer 1', 1)
        self.map2 = arcade.tilemap.process_layer(my_map, 'Tile Layer 2', 1)
            #self.map = arcade.tilemap.process_layer(my_map, 'Tile Layer 3', 1)
        #else:
         #   pass
    def on_draw(self):
        arcade.start_render()
        self.map.draw()
        self.map2.draw()
        output_total_Wood = f"Wood: {self.Wood}"
        arcade.draw_text(output_total_Wood, 1230, 1180, arcade.color.WHITE, 14)
        output_total_Food = f" Food: {self.Food}"
        arcade.draw_text(output_total_Food, 1230, 1160, arcade.color.WHITE, 14)
        output_total_Metal= f"Metal: {self.Metal}"
        arcade.draw_text( output_total_Metal, 1230, 1140, arcade.color.WHITE, 14)
        self.pointer.draw()

    def on_update(self, delta_time):
        self.tc=self.tc+delta_time
        if(self.tc>1):
            self.tc=self.tc-1
            self.Wood=self.Wood+(1*WFO)
            self.Metal=self.Metal+(1*MFO)
            self.Food=self.Food+(1*FFO)
    def on_mouse_motion(self, x, y, dx, dy):
        self.pointer[0].center_x = x
        self.pointer[0].center_y = y

def main():
    window = arcade.Window(WIDTH, HEIGHT, "WarFront")
    menu_view = MenuView()
    window.set_mouse_visible(False)
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()