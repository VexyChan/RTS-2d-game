import time

import arcade
import pathlib

from arcade import Sprite

WIDTH = 1400
HEIGHT = 1200
SPRITE_SCALING = 0.5
FRAME_WIDTH = 63
FRAME_HEIGHT = 79

class Node():
    def __init__(self):
        self.n=None
        self.s=None
        self.e=None
        self.w=None
        self.x=None
        self.y=None
    def setn(self,val):
        self.n=val
    def sets(self,val):
        self.s=val
    def sete(self,val):
        self.e=val
    def setw(self,val):
        self.w=val
    def setx(self,val):
        self.x=val
    def sety(self,val):
        self.y=val
    def getn(self):
        return self.n
    def gets(self):
        return self.s
    def sete(self):
        return self.e
    def setw(self):
        return self.w
    def setx(self):
        return self.x
    def sety(self):
        return self.y
# noinspection PyTypeChecker
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.gui = arcade.SpriteList()
        self.pointer = arcade.SpriteList()
        self.intro = arcade.play_sound(arcade.load_sound("Assets/Mysterious-piano.mp3"))
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

    def on_update(self, delta_time: float):
        if arcade.check_for_collision(self.pointer[0], self.bt1):
            self.bt1.scale = 8 / 12
        else:
            self.bt1.scale = 7 / 12
        if arcade.check_for_collision(self.pointer[0], self.bt2):
            self.bt2.scale = 8 / 12
        else:
            self.bt2.scale = 7 / 12
        if arcade.check_for_collision(self.pointer[0], self.bt3):
            self.bt3.scale = 8 / 12
        else:
            self.bt3.scale = 7 / 12

    def on_mouse_motion(self, x, y, dx, dy):
        self.pointer[0].center_x = x
        self.pointer[0].center_y = y

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if arcade.check_for_collision(self.pointer[0], self.bt1):
            instructions_view = GameView()
            self.window.show_view(instructions_view)
        elif arcade.check_for_collision(self.pointer[0], self.bt2):
            instructions_view = GameView()
            self.window.show_view(instructions_view)
        elif arcade.check_for_collision(self.pointer[0], self.bt3):
            instructions_view = GameView()
            self.window.show_view(instructions_view)
        else:
            pass


# noinspection PyTypeChecker
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Sprite lists
        # check to see current selected menu building / unit
        self.structure = None
        self.Unit = None
        # Pointer to current selected unit
        self.curUnit = None
        # // current multipliers of resource gathers
        self.WFO = 1
        self.MFO = 0
        self.FFO = 1
        self.graph= None
        # menu swap offset
        self.offset = 400
        # sprite lists
        self.allyStructs = arcade.SpriteList()
        self.allyUnits = arcade.SpriteList()
        self.enemyStructs = arcade.SpriteList()
        self.enemyUnits = arcade.SpriteList()
        self.Menu1 = arcade.SpriteList()
        self.Menu2 = arcade.SpriteList()
        self.map = arcade.SpriteList()
        self.pointer = arcade.SpriteList()
        # pointer sprite
        self.cur = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "coursor.gif")
        self.cur.center_x = 700
        self.cur.center_y = 900
        self.cur.scale = 1 / 2
        self.pointer.append(self.cur)
        # ally HQ
        self.HQ = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "castle.png")
        self.HQ.center_x = 120
        self.HQ.center_y = 1000
        self.HQ.scale = 1 / 8
        self.HQ.HP = 5000
        self.allyStructs.append(self.HQ)
        # enemy HQ
        self.EHQ = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "enemy captured castle.png")
        self.EHQ.center_x = 1080
        self.EHQ.center_y = 200
        self.EHQ.scale = 1 / 8
        self.EHQ.HP = 5000
        self.enemyStructs.append(self.EHQ)
        self.EHQ = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Enemy_Mine.png")
        self.EHQ.center_x = 1080
        self.EHQ.center_y = 700
        self.EHQ.scale = 1 / 8
        self.EHQ.HP = 1000
        self.enemyStructs.append(self.EHQ)
        self.EHQ = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Enemy_Mine.png")
        self.EHQ.center_x = 980
        self.EHQ.center_y = 400
        self.EHQ.scale = 1 / 8
        self.EHQ.HP = 1000
        self.enemyStructs.append(self.EHQ)
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
        self.uMBT1 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Unit1.png")
        self.uMBT1.center_x = 1300 + self.offset
        self.uMBT1.center_y = 870
        self.uMBT1.scale = 1 / 8
        self.Menu2.append(self.uMBT1)
        self.uMBT2 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Unit2.png")
        self.uMBT2.center_x = 1300 + self.offset
        self.uMBT2.center_y = 685
        self.uMBT2.scale = 1 / 8
        self.Menu2.append(self.uMBT2)
        self.uMBT3 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Unit3.png")
        self.uMBT3.center_x = 1300 + self.offset
        self.uMBT3.center_y = 500
        self.uMBT3.scale = 1 / 8
        self.Menu2.append(self.uMBT3)
        self.uMBT4 = arcade.Sprite(pathlib.Path.cwd() / 'Assets' / "Unit4.png")
        self.uMBT4.center_x = 1300 + self.offset
        self.uMBT4.center_y = 320
        self.uMBT4.scale = 1 / 8
        self.Menu2.append(self.uMBT4)
        #setup for enemy+ allys
        path = pathlib.Path.cwd() / 'Assets' / 'orcs' / 'ruler'
        self.eunit = \
            arcade.AnimatedTimeSprite(0.5, center_x=1050, center_y=320)
        all_files = path.glob('*.png')
        # location moving to
        self.eunit.move_x = self.eunit.center_x
        self.eunit.move_y = self.eunit.center_y
        # size of unit
        self.eunit.scale = 1 / 2
        # hp of unit
        self.eunit.HP = 100
        self.eunit.DMG = 25
        textures = []
        for file_path in all_files:
            frame = arcade.load_texture(str(file_path))
            textures.append(frame)
        self.eunit.textures = textures
        self.enemyUnits.append(self.eunit)
        #new enemy
        path = pathlib.Path.cwd() / 'Assets' / 'orcs' / 'assassini'
        self.bunit = \
            arcade.AnimatedTimeSprite(0.5, center_x=1000, center_y=300)
        all_files = path.glob('*.png')
        # location moving to
        self.bunit.move_x = self.bunit.center_x
        self.bunit.move_y = self.bunit.center_y
        # size of unit
        self.bunit.scale = 1 / 2
        # hp of unit
        self.bunit.HP = 100
        self.bunit.DMG = 25
        textures = []
        for file_path in all_files:
            frame = arcade.load_texture(str(file_path))
            textures.append(frame)
        self.bunit.textures = textures
        self.enemyUnits.append(self.bunit)
        # new enemy
        path = pathlib.Path.cwd() / 'Assets' / 'ogres' / 'yidle'
        self.dunit = \
            arcade.AnimatedTimeSprite(0.5, center_x=980, center_y=340)
        all_files = path.glob('*.png')
        # location moving to
        self.dunit.move_x = self.dunit.center_x
        self.dunit.move_y = self.dunit.center_y
        # size of unit
        self.dunit.scale = 1 / 2
        # hp of unit
        self.dunit.DMG = 25
        self.dunit.HP = 100
        textures = []
        for file_path in all_files:
            frame = arcade.load_texture(str(file_path))
            textures.append(frame)
        self.dunit.textures = textures
        self.enemyUnits.append(self.dunit)
        path = pathlib.Path.cwd() / 'Assets' / 'orcs' / 'archer idle'
        self.cunit = \
            arcade.AnimatedTimeSprite(0.5, center_x=940, center_y=340)
        all_files = path.glob('*.png')
        # location moving to
        self.cunit.move_x = self.dunit.center_x
        self.cunit.move_y = self.dunit.center_y
        # size of unit
        self.cunit.scale = 1 / 2
        # hp of unit
        self.cunit.DMG = 25
        self.cunit.HP = 100
        textures = []
        for file_path in all_files:
            frame = arcade.load_texture(str(file_path))
            textures.append(frame)
        self.cunit.textures = textures
        self.enemyUnits.append(self.cunit)
        path = pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'run'
        self.junit = \
            arcade.AnimatedTimeSprite(0.5, center_x=200, center_y=1000)
        all_files = path.glob('*.png')
        # location moving to
        self.junit.move_x = self.junit.center_x
        self.junit.move_y = self.junit.center_y
        # size of unit
        self.junit.scale = 1 / 2
        # hp of unit
        self.junit.DMG = 25
        self.junit.HP = 100
        textures = []
        for file_path in all_files:
            frame = arcade.load_texture(str(file_path))
            textures.append(frame)
        self.junit.textures = textures
        self.allyUnits.append(self.junit)
        # owned Resources
        self.Wood = 250
        self.Food = 100
        self.Metal = 50
        # wood cost
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
        # unit 1 cost
        self.uWCM = " "
        self.uWCF = " "
        # unit 2 cost
        self.uMCW = " "
        self.uMCF = " "
        # unit 3 cost
        self.uFCM = " "
        self.uFCW = " "
        # unit 4 cost
        self.uBCM = " "
        self.uBCF = " "
        #spawn decleration
        self.spawn_Point_x = self.HQ.center_x + 45
        self.spawn_Point_y = self.HQ.center_y - 45
        # DECLARE SPRITES
        self.FARM = arcade.Sprite()
        self.MINE = arcade.Sprite()
        self.Barracks = arcade.Sprite()
        self.WoodM = arcade.Sprite()
        # building limit on barrack
        self.BarracksL = 0
        # time check
        self.tc = 0
        self.frame_time = 0
        # Place holder till building is hovered
        self.Current_HP = 0
        # Map Setup
        self.map_location = pathlib.Path.cwd() / 'Assets' / 'WarFrontMap1.tmx'
        my_map = arcade.tilemap.read_tmx(self.map_location)
        self.map = arcade.tilemap.process_layer(my_map, 'Tile Layer 1', 1)
        self.map2 = arcade.tilemap.process_layer(my_map, 'Tile Layer 2', 1)
        self.map3 = arcade.tilemap.process_layer(my_map, 'Tile Layer 3', 1)
        self.map4 = arcade.tilemap.process_layer(my_map, 'Tile Layer 4', 1)
        self.graph = []
        
        #if this did work which for some reason it doesnt i would have an arcade collision check on building each building to make it
        #tile specific to build these buildings

        self.aunit=arcade.Sprite()

    def on_draw(self):
        arcade.start_render()
        # draw sprites
        self.map.draw()
        self.map2.draw()
        self.map3.draw()
        self.map4.draw()
        self.allyStructs.draw()
        self.enemyStructs.draw()
        self.enemyUnits.draw()
        self.allyUnits.draw()
        self.Menu1.draw()
        self.Menu2.draw()
        # resource totals & GUI info
        HP = f"Current HP:{self.Current_HP}"
        arcade.draw_text(HP, 950, 1160, arcade.color.WHITE, 24)
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
        # Barracks building cost
        arcade.draw_text(self.BCM, 1300, 900, arcade.color.WHITE, 18)
        arcade.draw_text(self.BCF, 1300, 920, arcade.color.WHITE, 18)
        # unit costs
        # wood building cost
        arcade.draw_text(self.uWCM, 1300, 350, arcade.color.WHITE, 18)
        arcade.draw_text(self.uWCF, 1300, 370, arcade.color.WHITE, 18)
        # Mine building cost
        arcade.draw_text(self.uMCW, 1300, 530, arcade.color.WHITE, 18)
        arcade.draw_text(self.uMCF, 1300, 550, arcade.color.WHITE, 18)
        # Farm building cost
        arcade.draw_text(self.uFCM, 1300, 715, arcade.color.WHITE, 18)
        arcade.draw_text(self.uFCW, 1300, 735, arcade.color.WHITE, 18)
        # Bafrracks building cost
        arcade.draw_text(self.uBCM, 1300, 900, arcade.color.WHITE, 18)
        arcade.draw_text(self.uBCF, 1300, 920, arcade.color.WHITE, 18)
        # mouse in game
        self.pointer.draw()

    def on_mouse_release(self, x: float, y: float, button: int,modifiers: int):
        self.curUnit.move_x = self.cur.center_x
        self.curUnit.move_y = self.cur.center_y
        self.curUnit=None

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # looks to see if you clicked on a structure from the build menu
        if arcade.check_for_collision(self.pointer[0], self.Menu1[1]):
            self.structure = "BARRACKS"
        elif arcade.check_for_collision(self.pointer[0], self.Menu1[2]):
            self.structure = "FARM"
        elif arcade.check_for_collision(self.pointer[0], self.Menu1[3]):
            self.structure = "METALMINE"
        elif arcade.check_for_collision(self.pointer[0], self.Menu1[4]):
            self.structure = "WOODCUTTER"
        # checks to see if you clicked on a unit from the unit menu
        if arcade.check_for_collision(self.pointer[0], self.Menu2[1]):
            self.Unit = "Unit1"
        elif arcade.check_for_collision(self.pointer[0], self.Menu2[2]):
            self.Unit = "Unit2"
        elif arcade.check_for_collision(self.pointer[0], self.Menu2[3]):
            self.Unit = "Unit3"
        elif arcade.check_for_collision(self.pointer[0], self.Menu2[4]):
            self.Unit = "Unit4"
        #collision check for unit selection
        print(self.Unit)
        self.curUnit = None
        if(arcade.check_for_collision_with_list(self.cur,self.allyUnits).__len__()>0):
            self.curUnit = arcade.check_for_collision_with_list(self.cur,self.allyUnits)[0]
            if (self.curUnit != None):
                self.curUnit.change_x = 0
                self.curUnit.change_y = 0
                self.curUnit.move_x = self.curUnit.center_x
                self.curUnit.move_y = self.curUnit.center_y

        # serices of If statments that check if the structure was clicked on the menu
        # if the structure is no ontop of another owned structure
        # if the place you wish to place it is within the map
        # if you have enough resources
        # if there is a building limit you dont go over it
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
            self.FARM.HP = 1000
            self.allyStructs.append(self.FARM)
            self.FFO = self.FFO + 1
            arcade.play_sound(arcade.load_sound("Assets/H3.wav"))
            arcade.play_sound(arcade.load_sound("Assets/H2.wav"))
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
            self.MINE.HP = 1000
            self.allyStructs.append(self.MINE)
            self.MFO = self.MFO + 1
            arcade.play_sound(arcade.load_sound("Assets/H3.wav"))
            arcade.play_sound(arcade.load_sound("Assets/H2.wav"))
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
            self.WoodM.HP = 1000
            self.allyStructs.append(self.WoodM)
            self.WFO = self.WFO + 1
            arcade.play_sound(arcade.load_sound("Assets/H3.wav"))
            arcade.play_sound(arcade.load_sound("Assets/H2.wav"))
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
            self.Barracks.HP = 2000
            self.allyStructs.append(self.Barracks)
            self.structure = None
            arcade.play_sound(arcade.load_sound("Assets/H3.wav"))
            arcade.play_sound(arcade.load_sound("Assets/H2.wav"))
        if arcade.check_for_collision(self.pointer[0], self.Barracks) & (self.MB2.center_x == 1700):
            # set menu2
            self.MB2.center_x = self.MB2.center_x - self.offset
            self.uMBT1.center_x = 1700 - self.offset
            self.uMBT2.center_x = 1700 - self.offset
            self.uMBT3.center_x = 1700 - self.offset
            self.uMBT4.center_x = 1700 - self.offset
            # offset buttons menu 1
            self.MBT1.center_x = self.MBT1.center_x + self.offset
            self.MBT2.center_x = self.MBT2.center_x + self.offset
            self.MBT3.center_x = self.MBT3.center_x + self.offset
            self.MBT4.center_x = self.MBT4.center_x + self.offset
        elif arcade.check_for_collision(self.pointer[0], self.allyStructs[0]) & (self.MB2.center_x == 1300):
            # offset menu 2
            self.MB2.center_x = self.MB2.center_x + self.offset
            self.uMBT1.center_x = 1300 + self.offset
            self.uMBT2.center_x = 1300 + self.offset
            self.uMBT3.center_x = 1300 + self.offset
            self.uMBT4.center_x = 1300 + self.offset
            # reset menu 1 buttons
            self.MBT1.center_x = self.MBT1.center_x - self.offset
            self.MBT2.center_x = self.MBT2.center_x - self.offset
            self.MBT3.center_x = self.MBT3.center_x - self.offset
            self.MBT4.center_x = self.MBT4.center_x - self.offset
    def on_update(self, delta_time):
        if (self.Unit == "Unit1") & (self.Food > 100) & (self.Wood > 40):
            # cost of unit
            self.Food = self.Food - 100
            self.Wood = self.Wood - 40
            #replace with animated sprite when done
            #self.aunit = arcade.Sprite()
            path = pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'idle'
            self.aunit = \
                arcade.AnimatedTimeSprite(0.5, center_x=self.spawn_Point_x, center_y=self.spawn_Point_y)
            all_files = path.glob('*.png')
            # location moving to
            self.aunit.move_x = self.aunit.center_x
            self.aunit.move_y = self.aunit.center_y
            # size of unit
            self.aunit.scale = 1 / 2
            # hp of unit
            self.aunit.DMG = 25
            self.aunit.HP = 100
            textures = []
            for file_path in all_files:
                frame = arcade.load_texture(str(file_path))
                textures.append(frame)
            #print(textures)
            self.aunit.textures = textures
            self.allyUnits.append(self.aunit)
            self.Unit = None
        """self.aunit.center_x = self.spawn_Point_x
            self.aunit.center_y = self.spawn_Point_y
            #what unit may not be needed
            self.aunit.type="Unit1"
            #animation type current will replace if state changes
            self.aunit.State="idle"
            #qadds aunit to the allysprite list"""
        #self.allyUnits.append(self.aunit)
        #HP Show of last hovered building
        if (self.Unit == "Unit2") & (self.Food > 100) & (self.Wood > 40):
            # cost of unit
            self.Food = self.Food - 100
            self.Wood = self.Wood - 40
            #replace with animated sprite when done
            #self.aunit = arcade.Sprite()
            path = pathlib.Path.cwd() / 'Assets' / 'style_B' / 'PNG' / 'idle'
            self.aunit = \
                arcade.AnimatedTimeSprite(0.5, center_x=self.spawn_Point_x, center_y=self.spawn_Point_y)
            all_files = path.glob('*.png')
            # location moving to
            self.aunit.move_x = self.aunit.center_x
            self.aunit.move_y = self.aunit.center_y
            # size of unit
            self.aunit.scale = 1 / 2
            # hp of unit
            self.aunit.DMG = 25
            self.aunit.HP = 100
            textures = []
            for file_path in all_files:
                frame = arcade.load_texture(str(file_path))
                textures.append(frame)
            #print(textures)
            self.aunit.textures = textures
            self.allyUnits.append(self.aunit)
            self.Unit = None
        if (self.Unit == "Unit3") & (self.Food > 100) & (self.Wood > 40):
            # cost of unit
            self.Food = self.Food - 100
            self.Wood = self.Wood - 40
            #replace with animated sprite when done
            #self.aunit = arcade.Sprite()
            path = pathlib.Path.cwd() / 'Assets' / 'style_C' / 'PNG' / 'idle'
            self.aunit = \
                arcade.AnimatedTimeSprite(0.5, center_x=self.spawn_Point_x, center_y=self.spawn_Point_y)
            all_files = path.glob('*.png')
            # location moving to
            self.aunit.move_x = self.aunit.center_x
            self.aunit.move_y = self.aunit.center_y
            # size of unit
            self.aunit.scale = 1 / 2
            # hp of unit
            self.aunit.DMG = 25
            self.aunit.HP = 100
            textures = []
            for file_path in all_files:
                frame = arcade.load_texture(str(file_path))
                textures.append(frame)
            #print(textures)
            self.aunit.textures = textures
            self.allyUnits.append(self.aunit)
            self.Unit = None
        if (self.Unit == "Unit4") & (self.Food > 100) & (self.Wood > 40):
            # cost of unit
            self.Food = self.Food - 100
            self.Wood = self.Wood - 40
            #replace with animated sprite when done
            #self.aunit = arcade.Sprite()
            path = pathlib.Path.cwd() / 'Assets' / 'style_D' / 'PNG' / 'idle'
            self.aunit = \
                arcade.AnimatedTimeSprite(0.5, center_x=self.spawn_Point_x, center_y=self.spawn_Point_y)
            all_files = path.glob('*.png')
            # location moving to
            self.aunit.move_x = self.aunit.center_x
            self.aunit.move_y = self.aunit.center_y
            # size of unit
            self.aunit.scale = 1 / 2
            # hp of unit

            self.aunit.DMG = 25
            self.aunit.HP = 100
            textures = []
            for file_path in all_files:
                frame = arcade.load_texture(str(file_path))
                textures.append(frame)
            #print(textures)
            self.aunit.textures = textures
            self.allyUnits.append(self.aunit)
            self.Unit = None

        for i in self.allyStructs:
            if arcade.check_for_collision(self.cur, i):
                self.Current_HP = i.HP
        for i in self.allyUnits:
            if arcade.check_for_collision(self.cur, i):
                self.Current_HP = i.HP
        for i in self.enemyStructs:
            if arcade.check_for_collision(self.cur, i):
                self.Current_HP = i.HP
        for i in self.enemyUnits:
            if arcade.check_for_collision(self.cur, i):
                self.Current_HP = i.HP
        self.tc = self.tc + delta_time
        #resource show of hovered build option
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
        # menu2
        if arcade.check_for_collision(self.pointer[0], self.Menu2[1]):
            self.uMBT1.scale = 1 / 7
            self.uBCM = "Wood: 40"
            self.uBCF = "Food: 100 "
        else:
            self.uMBT1.scale = 1 / 8
            self.uBCM = " "
            self.uBCF = " "

        if arcade.check_for_collision(self.pointer[0], self.Menu2[2]):
            self.uMBT2.scale = 1 / 7
            self.uFCM = "Metal: 20"
            self.uFCW = "Food: 200"

        else:
            self.uMBT2.scale = 1 / 8
            self.uFCM = " "
            self.uFCW = " "

        if arcade.check_for_collision(self.pointer[0], self.Menu2[3]):
            self.uMBT3.scale = 1 / 7
            self.uMCF = "Food: 400"
            self.uMCW = "Wood: 300"
        else:
            self.uMBT3.scale = 1 / 8
            self.uMCF = " "
            self.uMCW = " "

        if arcade.check_for_collision(self.pointer[0], self.Menu2[4]):
            self.uMBT4.scale = 1 / 7
            self.uWCM = "Metal: 120"
            self.uWCF = "Food: 400"
        else:
            self.uWCM = " "
            self.uWCF = " "
            self.uMBT4.scale = 1 / 8
        if self.tc > 1:
            for CurA in self.allyUnits:
                for CurE in self.enemyUnits:
                    if (-60 < (CurA.center_x - CurE.center_x) < 60) or (-60 < (CurA.center_y - CurE.center_y) < 60):

                        self.intro = arcade.play_sound(arcade.load_sound("Assets/Sword.mp3"))
                        CurA.HP = CurA.HP - CurE.DMG
                        CurE.HP = CurE.HP - CurA.DMG
                        if CurE.HP==0:
                            arcade.play_sound(arcade.load_sound("Assets/death.wav"))
                            CurE.kill()
                        if CurA.HP==0:
                            arcade.play_sound(arcade.load_sound("Assets/death.wav"))
                            CurA.kill()
                for CurEB in self.enemyStructs:
                    if(-60 < (CurA.center_x - CurEB.center_x) < 60 )or( -60 < (CurA.center_y - CurEB.center_y) < 60):
                        CurEB.HP=CurEB.HP-CurA.DMG
                        if CurEB.HP==0:
                            if CurEB == self.EHQ:
                                #plays on wining a game
                                arcade.play_sound(arcade.load_sound("Assets/win.wav"))
                                self.window.show_view(MenuView())
                            CurEB.kill()
                            arcade.play_sound(arcade.load_sound("Assets/bp.wav"))
            for curUnit in self.allyUnits:
                if curUnit.move_x != curUnit.center_x:
                    print((curUnit.move_x - curUnit.center_x))
                    if (curUnit.move_x - curUnit.center_x) < -10:
                        curUnit.change_x = -1
                    elif (curUnit.move_x - curUnit.center_x) > 10:
                        curUnit.change_x = 1
                    elif (0 <(curUnit.move_x - curUnit.center_x) <= 20 ):
                        curUnit.move_x = curUnit.center_x
                        curUnit.change_x = 0
                    elif (0 > (curUnit.move_x - curUnit.center_x) >= -20):
                        curUnit.move_x = curUnit.center_x
                        curUnit.change_x = 0
                    else:
                        curUnit.change_x=0
            for curUnitg in self.allyUnits:
                if curUnitg.move_y != curUnitg.center_y:
                    print((curUnitg.move_y - curUnitg.center_y))
                    if (curUnitg.move_y - curUnitg.center_y) < -10:
                        curUnitg.change_y = -1
                    elif (curUnitg.move_y - curUnitg.center_y) > 10:
                        curUnitg.change_y = 1
                    elif (0 < (curUnitg.move_y - curUnitg.center_y) <= 20):
                        curUnitg.move_y = curUnitg.center_y
                        curUnitg.change_y = 0
                    elif (0 > (curUnitg.move_y - curUnitg.center_y) >= -20):
                        curUnitg.move_y = curUnitg.center_y
                        curUnitg.change_y = 0
                    else:
                        curUnitg.change_y=0
            self.tc = self.tc -1
            self.Wood = self.Wood + (2 * self.WFO)
            self.Metal = self.Metal + (2 * self.MFO)
            self.Food = self.Food + (2 * self.FFO)
        self.allyUnits.update()
        self.allyStructs.update()
        self.enemyStructs.update()
        self.aunit.update_animation()
        self.eunit.update_animation()
        self.bunit.update_animation()
        self.dunit.update_animation()
        self.cunit.update_animation()
        self.junit.update_animation()
        '''#change in x and y over all from start to end
            self.aunit.diff_X = 0
            self.aunit.diff_y = 0
            #location moving to to
            self.aunit.moveX=self.aunit.center_x
            self.aunit.movey=self.aunit.center_y
            #moves per update cycle
            self.aunit.moves=10
            '''
            #self.Texture_Handler()
#removed due to issues with not updateing texture after adding it in on the cycle change
    '''def Texture_Handler(self):
            for i in self.allyUnits:
                if i.State is "idle":
                    if i.cycle is 0:
                        print("im going and changing states of the animation image")
                        if i.type is "Unit1":
                            print("i should work but i dont try different arg")
                            i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'idle' / 'frame0000.png'))
                            i.cycle=1
                            i.set_texture(0)
                        if i.type is "Unit2":
                            i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_B' / 'PNG' / 'idle' / 'frame0000.png'))
                        if i.type is "Unit3":
                            i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_C' / 'PNG' / 'idle' / 'frame0000.png'))
                        if i.type is "Unit4":
                            i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_D' / 'PNG' / 'idle' / 'frame0000.png'))
                    elif i.cycle is 1:
                        if i.type is "Unit1":
                            print("i get to cycle 2 and i should still work")
                            i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'idle' / 'frame0001.png'))
                            i.cycle = 2
                            i.set_texture(1)
                            i.update()
                            if i.type is "Unit2":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_B' / 'PNG' / 'idle' / 'frame0001.png'))
                            if i.type is "Unit3":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_C' / 'PNG' / 'idle' / 'frame0001.png'))
                            if i.type is "Unit4":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_D' / 'PNG' / 'idle' / 'frame0001.png'))
                    elif i.cycle is 2:
                            if i.type is "Unit1":
                                i.cycle=3
                                i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'idle' / 'frame0002.png'))
                                i.update()
                                i.set_texture(2)
                            if i.type is "Unit2":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_B' / 'PNG' / 'idle' / 'frame0002.png'))
                            if i.type is "Unit3":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_C' / 'PNG' / 'idle' / 'frame0002.png'))
                            if i.type is "Unit4":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_D' / 'PNG' / 'idle' / 'frame0002.png'))
                    elif i.cycle is 3:
                            if i.type is "Unit1":
                                i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'idle' / 'frame0003.png'))
                                i.set_texture(3)
                                i.cycle=4
                                i.update()
                            if i.type is "Unit2":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_B' / 'PNG' / 'idle' / 'frame0003.png'))
                            if i.type is "Unit3":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_C' / 'PNG' / 'idle' / 'frame0003.png'))
                            if i.type is "Unit4":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_D' / 'PNG' / 'idle' / 'frame0003.png'))
                    elif i.cycle is 4:
                            if i.type is "Unit1":

                                i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'idle' / 'frame0004.png'))
                                i.set_texture(4)
                                i.cycle=5
                                i.update()
                            if i.type is "Unit2":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_B' / 'PNG' / 'idle' / 'frame0004.png'))
                            if i.type is "Unit3":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_C' / 'PNG' / 'idle' / 'frame0004.png'))
                            if i.type is "Unit4":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_D' / 'PNG' / 'idle' / 'frame0004.png'))
                    elif i.cycle is 5:
                            if i.type is "Unit1":
                                i.append_texture(str(pathlib.Path.cwd() / 'Assets' / 'style_A' / 'PNG' / 'idle' / 'frame0005.png'))
                                i.cycle=0
                                i.set_texture(5)
                                i.update()
                            if i.type is "Unit2":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_B' / 'PNG' / 'idle' / 'frame0005.png'))
                            if i.type is "Unit3":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_C' / 'PNG' / 'idle' / 'frame0005.png'))
                            if i.type is "Unit4":
                                i.append_texture(
                                    str(pathlib.Path.cwd() / 'Assets' / 'style_D' / 'PNG' / 'idle' / 'frame0005.png'))
    '''
    """
            #this didnt work sooo yeaaaah made my own animation def by changing from picture to picture ever cycle 
            self.AUnit = arcade.AnimatedTimeSprite(scale=4,image_x=1106,image_y=756, center_x=700, center_y=700)
            path = pathlib.Path.cwd() / 'Assets' / 'style_A' / 'spritesheet' / 'spritesheet.png'
            self.AUnit = arcade.AnimatedTimeSprite(scale=1, center_x=700,center_y=700)
            self.AUnit.HP = 100
            self.AUnit.DMG = 25
            for row in range(4):
                for col in range(6):
                    frame = arcade.load_texture(str(path), x=col * FRAME_WIDTH, y=row * FRAME_HEIGHT, width=FRAME_WIDTH,
                                                height=FRAME_HEIGHT)
                    self.AUnit.textures.append(frame)
            print(self.AUnit.textures.__sizeof__())
            self.AUnit.update_animation()
            self.AUnit.
            self.AUnit.draw()
            #self.allyUnits.append(self.AUnit)
            self.Unit = None"""
    """if (curUnit.center_x != curUnit.moveX):
                        print(curUnit.center_x)
                        print(curUnit.moveX)
                        print("i should move to the right")
                        if (curUnit.diff_X > 0 & curUnit.diff_X >= 5):
                            curUnit.center_x = curUnit.center_x + 5
                            curUnit.diff_X = curUnit.diff_X - 5
                        elif (curUnit.diff_X > 0 & 0 < curUnit.diff_X < 5):
                            curUnit.center_x=curUnit.center_x + curUnit.diff_X
                            curUnit.diff_X = 0
                        print(curUnit.center_x)
                        print(curUnit.moveX)
                        print("i do i move?")
                    if (curUnit.center_y != curUnit.movey):
                        print(curUnit.center_y)
                        print(curUnit.movey)
                        print("i should move up")
                        if (curUnit.diff_y > 0 & curUnit.diff_y >= 5):
                            curUnit.center_y = curUnit.center_y + 5
                            curUnit.diff_y = curUnit.diff_y - 5
                        elif (curUnit.diff_y > 0 & 0 < curUnit.diff_y < 5):
                            curUnit.center_y = curUnit.center_y + curUnit.diff_y
                            curUnit.diff_y = 0
                        print(curUnit.center_y)
                        print(curUnit.movey)
                        print("i do i move?")
                    if (curUnit.center_x != curUnit.moveX):
                        print(curUnit.center_x)
                        print(curUnit.moveX)
                        print("i should move left")
                        if ((curUnit.diff_X < 0 )&( curUnit.diff_X <= -5)):
                            curUnit.center_x = curUnit.center_x - 5
                            curUnit.diff_X = curUnit.diff_X + 5
                        elif ((curUnit.diff_X < 0) &( 0 > curUnit.diff_X > -5)):
                            curUnit.center_x=curUnit.center_x - curUnit.diff_X
                            curUnit.diff_X = 0
                        print(curUnit.center_x)
                        print(curUnit.moveX)
                        print("i do i move?")
                    if (curUnit.center_y != curUnit.movey):
                        print(curUnit.center_y)
                        print(curUnit.movey)
                        print("i should move sown")
                        if ((curUnit.diff_y < 0 )& (0 > curUnit.diff_y <= -5)):
                            curUnit.center_y = curUnit.center_y - 5
                            curUnit.diff_y = curUnit.diff_y + 5
                        elif ((curUnit.diff_y < 0) & (curUnit.diff_y > -5)):
                            curUnit.center_y = curUnit.center_y - curUnit.diff_y
                            curUnit.diff_y = 0
                        print(curUnit.center_x)
                        print(curUnit.moveX)
                        print("i do i move?")
                    print(curUnit.center_x)
                    print(curUnit.center_y)"""

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
