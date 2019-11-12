import arcade
import pathlib
import random
import pyglet

WIDTH = 1400
HEIGHT = 1200
SPRITE_SCALING = 0.5


class MAP():
    def __init__(self):
        super().__init__()
        self.MapN = 0

    def GET(Name):
        return self.MapN

    def SET(MAP):
        MapN = MAP


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.gui = arcade.SpriteList()
        self.pointer = arcade.SpriteList()
        self.so = arcade.load_sound("Assets/Mysterious-piano.mp3")
        arcade.play_sound(self.so)
        self.cur = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "coursor.gif")
        self.cur.center_x = 700
        self.cur.center_y = 900
        self.cur.scale = 1 / 2
        self.pointer.append(self.cur)
        self.CASTLE = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "castle.jpg")
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
        self.bt1.scale = 7 / 12
        self.gui.append(self.bt1)
        self.bt2 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "playmap3.png")
        self.bt2.center_x = 200
        self.bt2.center_y = 700
        self.bt2.scale = 7 / 12
        self.gui.append(self.bt2)
        self.bt3 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "playmap2.png")
        self.bt3.center_x = 200
        self.bt3.center_y = 800
        self.bt3.scale = 7 / 12
        self.gui.append(self.bt3)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()
        self.pointer.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.pointer[0].center_x = x
        self.pointer[0].center_y = y

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        Name = MAP
        if (arcade.check_for_collision(self.pointer[0], self.bt1) == True):
            Name.SET(1)
            instructions_view = GameView()
            self.window.show_view(instructions_view)
        elif (arcade.check_for_collision(self.pointer[0], self.bt2) == True):
            Name.SET(2)
            instructions_view = GameView()
            self.window.show_view(instructions_view)
        elif (arcade.check_for_collision(self.pointer[0], self.bt3) == True):
            Name.SET(3)
            instructions_view = GameView()
            self.window.show_view(instructions_view)
        else:
            pass


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Sprite lists
        self.structure = None
        self.Unit = None
        self.curUnit = None
        self.WFO = 1
        self.MFO = 1
        self.FFO = 1
        self.offset = 400
        self.allyStructs = arcade.SpriteList()
        self.allyUnits = arcade.SpriteList()
        self.enemyStructs = arcade.SpriteList()
        self.enemyUnits = arcade.SpriteList()
        self.Menu1 = arcade.SpriteList()
        self.Menu2 = arcade.SpriteList()
        self.map = arcade.SpriteList()
        self.pointer = arcade.SpriteList()
        self.cur = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "coursor.gif")
        self.cur.center_x = 700
        self.cur.center_y = 900
        self.cur.scale = 1 / 2
        self.pointer.append(self.cur)
        self.HQ = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "castle.png")
        self.HQ.center_x = 120
        self.HQ.center_y = 1000
        self.HQ.scale = 1 / 8
        self.allyStructs.append(self.HQ)
        self.EHQ = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "enemy captured castle.png")
        self.EHQ.center_x = 1080
        self.EHQ.center_y = 200
        self.EHQ.scale = 1 / 8
        self.allyStructs.append(self.EHQ)
        # MENU 1 DEFAULT MENU COORDS
        self.MB1 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Menuback1.png")
        self.MB1.center_x = 1300
        self.MB1.center_y = 500
        self.MB1.scale = 1
        self.Menu1.append(self.MB1)
        self.MBT1 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Barracks_Button.png")
        self.MBT1.center_x = 1300
        self.MBT1.center_y = 870
        self.MBT1.scale = 1 / 8
        self.Menu1.append(self.MBT1)
        self.MBT2 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Farm_Button.png")
        self.MBT2.center_x = 1300
        self.MBT2.center_y = 685
        self.MBT2.scale = 1 / 8
        self.Menu1.append(self.MBT2)
        self.MBT3 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Metal_Mine.png")
        self.MBT3.center_x = 1300
        self.MBT3.center_y = 500
        self.MBT3.scale = 1 / 8
        self.Menu1.append(self.MBT3)
        self.MBT4 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Wood_Button.png")
        self.MBT4.center_x = 1300
        self.MBT4.center_y = 320
        self.MBT4.scale = 1 / 8
        self.Menu1.append(self.MBT4)
        # MENU 2 OFFEST MENU COORDS
        self.MB2 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "menu2b.png")
        self.MB2.center_x = 1300 + self.offset
        self.MB2.center_y = 500
        self.MB2.scale = 1
        self.Menu2.append(self.MB2)
        self.Wood = 250
        self.Food = 100
        self.Metal = 25
        # woodc cost
        self.WCM = " "
        self.WCF = " "
        # Mine cost
        self.MCW = " "
        self.MCF = " "
        # farm Cost
        self.FCM = " "
        self.FCW = " "
        # Barracks cost
        self.BCM = " "
        self.BCF = " "
        # DECLARE SPRITES
        self.FARM = arcade.Sprite()
        self.MINE = arcade.Sprite()
        self.Barracks = arcade.Sprite()
        self.WoodM = arcade.Sprite()
        self.BarracksL = 0
        self.tc = 0
        self.menu = 1
        # Map Setup
        self.map_location = pathlib.Path.cwd() / 'Assets' / 'WarFrontMap1.tmx'
        my_map = arcade.tilemap.read_tmx(self.map_location)
        self.map = arcade.tilemap.process_layer(my_map, 'Tile Layer 1', 1)
        self.map2 = arcade.tilemap.process_layer(my_map, 'Tile Layer 2', 1)
        # self.map = arcade.tilemap.process_layer(my_map, 'Tile Layer 3', 1)

    def on_draw(self):
        arcade.start_render()
        self.map.draw()
        self.map2.draw()
        self.allyStructs.draw()
        self.enemyStructs.draw()
        self.Menu1.draw()
        self.Menu2.draw()
        # resource totals
        output_total_Wood = f"Wood: {self.Wood}"
        arcade.draw_text(output_total_Wood, 1220, 1090, arcade.color.WHITE, 24)
        output_total_Food = f" Food: {self.Food}"
        arcade.draw_text(output_total_Food, 1220, 1050, arcade.color.WHITE, 24)
        output_total_Metal = f"Metal: {self.Metal}"
        arcade.draw_text(output_total_Metal, 1220, 1010, arcade.color.WHITE, 24)
        # wood building cost
        arcade.draw_text(self.WCM, 1300, 350, arcade.color.WHITE, 18)
        arcade.draw_text(self.WCF, 1300, 370, arcade.color.WHITE, 18)
        # Mine building cost
        arcade.draw_text(self.MCW, 1300, 530, arcade.color.WHITE, 18)
        arcade.draw_text(self.MCF, 1300, 550, arcade.color.WHITE, 18)
        # Farm building cost
        arcade.draw_text(self.FCM, 1300, 715, arcade.color.WHITE, 18)
        arcade.draw_text(self.FCW, 1300, 735, arcade.color.WHITE, 18)
        # Bafrracks building cost
        arcade.draw_text(self.BCM, 1300, 900, arcade.color.WHITE, 18)
        arcade.draw_text(self.BCF, 1300, 920, arcade.color.WHITE, 18)
        self.pointer.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if arcade.check_for_collision(self.pointer[0], self.Menu1[1]):
            self.structure = "BARRACKS"
        elif arcade.check_for_collision(self.pointer[0], self.Menu1[2]):
            self.structure = "FARM"
        elif arcade.check_for_collision(self.pointer[0], self.Menu1[3]):
            self.structure = "METALMINE"
        elif arcade.check_for_collision(self.pointer[0], self.Menu1[4]):
            self.structure = "WOODCUTTER"
        if (self.structure == "FARM") & \
                (arcade.check_for_collision_with_list(self.pointer[0], self.allyStructs).__sizeof__() < 21) & \
                (self.Wood > 50) & (self.Metal > 20) & (self.cur.center_x < 1200) & (self.cur.center_x > 100) \
                & (self.cur.center_y < 1200) & (self.cur.center_y > 100):
            self.Metal = self.Metal - 20
            self.Wood = self.Wood - 50
            self.FARM = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "farm.png")
            self.FARM.center_x = self.cur.center_x
            self.FARM.center_y = self.cur.center_y
            self.FARM.scale = 1 / 12
            self.allyStructs.append(self.FARM)
            self.FFO = self.FFO + 1
            self.structure = None
        if (self.structure == "METALMINE") & \
                (arcade.check_for_collision_with_list(self.pointer[0], self.allyStructs).__sizeof__() < 21) & \
                (self.Wood > 50) & (self.Food > 200) & (self.cur.center_x < 1200) & (self.cur.center_x > 100) \
                & (self.cur.center_y < 1200) & (self.cur.center_y > 100):
            self.Food = self.Food - 200
            self.Wood = self.Wood - 50
            self.MINE = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "MetalMine.png")
            self.MINE.center_x = self.cur.center_x
            self.MINE.center_y = self.cur.center_y
            self.MINE.scale = 1 / 12
            self.allyStructs.append(self.MINE)
            self.MFO = self.MFO + 1
            self.structure = None
        if (self.structure == "WOODCUTTER") & \
                (arcade.check_for_collision_with_list(self.pointer[0], self.allyStructs).__sizeof__() < 21) & \
                (self.Metal > 30) & (self.Food > 200) & (self.cur.center_x < 1200) & (self.cur.center_x > 100) \
                & (self.cur.center_y < 1200) & (self.cur.center_y > 100):
            self.Food = self.Food - 200
            self.Metal = self.Metal - 30
            self.WoodM = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "woodcutters_hut.png")
            self.WoodM.center_x = self.cur.center_x
            self.WoodM.center_y = self.cur.center_y
            self.WoodM.scale = 1 / 12
            self.allyStructs.append(self.WoodM)
            self.WFO = self.WFO + 1
            self.structure = None
        if (self.structure == "BARRACKS") & \
                (arcade.check_for_collision_with_list(self.pointer[0], self.allyStructs).__sizeof__() < 21) & \
                (self.Wood > 100) & (self.Metal > 40) & (self.cur.center_x < 1200) & (self.cur.center_x > 100) \
                & (self.cur.center_y < 1200) & (self.cur.center_y > 100) & (self.BarracksL == 0):
            self.Metal = self.Metal - 40
            self.BarracksL = 1
            self.Wood = self.Wood - 100
            self.Barracks = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "barracks.png")
            self.Barracks.center_x = self.cur.center_x
            self.Barracks.center_y = self.cur.center_y
            self.Barracks.scale = 1 / 12
            self.allyStructs.append(self.Barracks)
            self.structure = None
        else:
            pass
        if arcade.check_for_collision(self.pointer[0], self.Barracks)&(self.MB2.center_x==1700):
            print("Change to menu 2")
            #offset buttons menu 1
            self.MBT1.center_x=self.MBT1.center_x+self.offset
            self.MBT2.center_x=self.MBT2.center_x+self.offset
            self.MBT3.center_x=self.MBT3.center_x+self.offset
            self.MBT4.center_x=self.MBT4.center_x+self.offset
            #set menu2
            self.MB2.center_x = self.MB2.center_x - self.offset
        elif arcade.check_for_collision(self.pointer[0], self.allyStructs[0])&(self.MB2.center_x==1300):
            #offset menu 2
            self.MB2.center_x = self.MB2.center_x + self.offset
            #reset menu 1 buttons
            self.MBT1.center_x=self.MBT1.center_x-self.offset
            self.MBT2.center_x=self.MBT2.center_x-self.offset
            self.MBT3.center_x=self.MBT3.center_x-self.offset
            self.MBT4.center_x=self.MBT4.center_x-self.offset
            print("Change to menu 1")
        print(self.MB2.center_x)

    def on_update(self, delta_time):
        self.tc = self.tc + delta_time
        self.allyStructs.update()
        if arcade.check_for_collision(self.pointer[0], self.Menu1[1]):
            self.MBT1.scale = 1 / 7
            self.BCM = "Metal: 40"
            self.BCF = "Food: 100 "
        else:
            self.MBT1.scale = 1 / 8
            self.BCM = " "
            self.BCF = " "

        if arcade.check_for_collision(self.pointer[0], self.Menu1[2]):
            self.MBT2.scale = 1 / 7
            self.FCM = "Metal: 20"
            self.FCW = "Wood: 50"

        else:
            self.MBT2.scale = 1 / 8
            self.FCM = " "
            self.FCW = " "

        if arcade.check_for_collision(self.pointer[0], self.Menu1[3]):
            self.MBT3.scale = 1 / 7
            self.MCF = "Food: 200"
            self.MCW = "Wood: 50"
        else:
            self.MBT3.scale = 1 / 8
            self.MCF = " "
            self.MCW = " "

        if arcade.check_for_collision(self.pointer[0], self.Menu1[4]):
            self.MBT4.scale = 1 / 7
            self.WCM = "Metal: 30"
            self.WCF = "Food: 200"
        else:
            self.WCM = " "
            self.WCF = " "
            self.MBT4.scale = 1 / 8
        if self.menu == 1:
            self.Menu1.update()
        if self.menu == 2:
            self.Menu2.update()
        if (self.tc > 1):
            self.tc = self.tc - 1
            self.Wood = self.Wood + (2 * self.WFO)
            self.Metal = self.Metal + (2 * self.MFO)
            self.Food = self.Food + (2 * self.FFO)

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
