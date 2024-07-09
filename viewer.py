from ion import keydown,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_BACKSPACE,KEY_OK,KEY_MINUS,KEY_PLUS,KEY_ANS,KEY_DOT,KEY_EXP
from kandinsky import draw_string,fill_rect,color
from time import sleep

class Screen: palette = {"Background":(255,255,255),"PrimaryColor":(0,0,0),"TitleColor":"orange","PrimaryText":(0,200,200),"SecondaryText":(255,255,255),"BoundingColor":"magenta","CursorColor":"cyan"}

class Curseur:
    def __init__(self, *args, default=""): self.args, self.sens, self.default = args, "R", default
    def __next__(self): self.N += 1 if self.sens == "R" else -1 ; self.check() ; self.curs = self.args[self.N] ; return self.curs
    def __iter__(self): self.curs, self.N = self.default if self.default != ""  else self.args[-1], self.args.index(self.default) if self.default != ""  else -1 ; return self
    def check(self):
        if self.N > len(self.args)-1: self.N = 0
        elif self.N < 0: self.N = len(self.args)-1

class Picture:
    def __init__(self, picture: list[list[int]], colors: dict = {0:(255,255,255),1:(0,0,0),2:(200,0,0),3:(0,200,0),4:(0,0,200)}, name: str = "DefaultName"): self.width,self.length,self.picture,self.colors,self.name = len(picture),len(picture[0]),picture,colors,name
    def __str__(self) -> str: return str(self.name)
    def __iter__(self) -> iter: liste = [] ; _l = [[liste.append(pix) for pix in line] for line in self.picture] ; del _l ; return iter(liste)
    def __getitem__(self, xy) -> int: return self.picture[xy]
    def __setitem__(self, xy, value: int) -> int: self.picture[xy] = value
    def draw(self, x: int, y: int, t: int = 1):
        for j in range(self.width):
            for i in range(self.length): fill_rect(x+j*t,y+i*t,t,t,self.colors[self[i][j]] if isinstance(self[i][j],int) else self[i][j])

print("The size of pictures isn't implemented for the moment.")
try: from examples_pictures import * ; module = __import__("examples_pictures") ; EX = True
except ImportError: print("The module with examples pictures was not found.\nYou can't see any pictures now in 'show':\nyou have to created its") ; EX = False

class GUI:
    time,size,pas,default_color,I_canal,rgb = 0.1,16,1,"white",iter(Curseur("red","green","blue",default="red")),{"red":0,"green":1,"blue":2}
    PICTURES,PICT_EDIT = [Picture(module.picture_cursor,module.colors_cursor,"Cursor"),Picture(module.picture_bloc,module.colors_bloc,"Block")] if EX else [],Picture([[(255,255,255) for _ in range(16)] for _ in range(16)])
    if EX:
        for name in dir(module): PICTURES.append(Picture(eval(name))) if name not in ["picture_cursor","colors_cursor","picture_bloc","colors_bloc"] and name[0] != "_" else None
    @staticmethod
    def clean(): fill_rect(0,0,320,222,Screen.palette["Background"])
    @staticmethod
    def main(): GUI.Menu.draw()
    class Menu:
        @staticmethod
        def draw():
            def draw_curseur(curseur):
                if curseur == "edit":
                    draw_string(" >  edit  <",105,100,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("  show        ",115,130,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("  settings        ",95,160,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                elif curseur == "show":
                    draw_string("  edit        ",115,100,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string(" >  show  <",105,130,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("  settings        ",95,160,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                elif curseur == "settings":
                    draw_string("  edit        ",115,100,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("  show        ",115,130,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string(" >  settings  <",85,160,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            GUI.clean() ; I = iter(Curseur("edit","show","settings"))
            draw_string("Pictures Viewer",88,50,Screen.palette["TitleColor"],Screen.palette["SecondaryText"])
            draw_string("  edit  ",115,100,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("  show  ",115,130,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("  settings  ",95,160,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            while True:
                if keydown(KEY_UP): I.sens = "L" ; next(I) ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_DOWN): I.sens = "R" ; next(I) ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_OK) and I.curs == "edit": GUI.Edit.draw() ; break
                if keydown(KEY_OK) and I.curs == "show" and len(GUI.PICTURES) != 0: GUI.Show.draw() ; break
                if keydown(KEY_OK) and I.curs == "settings": GUI.Settings.draw() ; break
    class Edit:
        @staticmethod
        def draw():
            def draw_curs(x,y,color=Screen.palette["CursorColor"]): fill_rect(80+x*10+2,35+y*10+2,10-4,10-4,color)
            def update_arrow(): draw_curs(x,y) ; draw_string(str(GUI.PICT_EDIT[y][x])+" "*12,85,202,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"]) ; sleep(GUI.time)
            def update_minus_plus(): GUI.PICT_EDIT[y][x] = tuple(GUI.PICT_EDIT[y][x]) ; fill_rect(80+x*10,35+y*10,10,10,GUI.PICT_EDIT[y][x]) ; draw_curs(x,y) ; draw_string(str(GUI.PICT_EDIT[y][x])+" "*12,85,202,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"]) ; sleep(GUI.time)
            def _print(picture):
                for i in range(len(picture)): print(str(picture[i])+",") if i+1 != len(picture) else print(str(picture[i])+"]")
            GUI.clean() ; x,y = 0,0
            fill_rect(79,34,162,162,Screen.palette["BoundingColor"])
            draw_string("Edit",139,10,Screen.palette["TitleColor"],Screen.palette["SecondaryText"])
            draw_string(GUI.I_canal.curs,10,100,GUI.I_canal.curs,Screen.palette["SecondaryText"])
            draw_string(str(GUI.PICT_EDIT[y][x])+" "*12,85,202,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            GUI.PICT_EDIT.draw(80,35,10) ; draw_curs(x,y) ; sleep(GUI.time)
            while True:
                if keydown(KEY_OK) and keydown(KEY_LEFT): GUI.I_canal.sens = "L" ; next(GUI.I_canal) ; draw_string(GUI.I_canal.curs+" "*2,5,100,GUI.I_canal.curs,Screen.palette["SecondaryText"]) ; sleep(0.15)
                if keydown(KEY_OK) and keydown(KEY_RIGHT): GUI.I_canal.sens = "R" ; next(GUI.I_canal) ; draw_string(GUI.I_canal.curs+" "*2,5,100,GUI.I_canal.curs,Screen.palette["SecondaryText"]) ; sleep(0.15)
                if keydown(KEY_UP) and not keydown(KEY_OK) and y > 0: draw_curs(x,y,GUI.PICT_EDIT[y][x]) ; y -= 1 ; update_arrow()
                if keydown(KEY_DOWN) and not keydown(KEY_OK) and y < 15: draw_curs(x,y,GUI.PICT_EDIT[y][x]) ; y += 1 ; update_arrow()
                if keydown(KEY_LEFT) and not keydown(KEY_OK) and x > 0: draw_curs(x,y,GUI.PICT_EDIT[y][x]) ; x -= 1 ; update_arrow()
                if keydown(KEY_RIGHT) and not keydown(KEY_OK) and x < 15: draw_curs(x,y,GUI.PICT_EDIT[y][x]) ; x += 1 ; update_arrow()
                if keydown(KEY_PLUS) and GUI.PICT_EDIT[y][x][GUI.rgb[GUI.I_canal.curs]] + GUI.pas <= 255: GUI.PICT_EDIT[y][x] = list(GUI.PICT_EDIT[y][x]) ; GUI.PICT_EDIT[y][x][GUI.rgb[GUI.I_canal.curs]] += GUI.pas ; update_minus_plus()
                if keydown(KEY_MINUS) and GUI.PICT_EDIT[y][x][GUI.rgb[GUI.I_canal.curs]] - GUI.pas >= 0: GUI.PICT_EDIT[y][x] = list(GUI.PICT_EDIT[y][x]) ; GUI.PICT_EDIT[y][x][GUI.rgb[GUI.I_canal.curs]] -= GUI.pas ; update_minus_plus()
                if keydown(KEY_ANS): GUI.PICTURES.append(GUI.PICT_EDIT) ; print("[",end="") ; _print(GUI.PICT_EDIT.picture) ; GUI.PICT_EDIT = Picture([[(color(GUI.default_color)) for _ in range(16)] for _ in range(16)]) ; GUI.PICT_EDIT.draw(80,35,10) ; x,y = 0,0 ; draw_curs(x,y,GUI.PICT_EDIT[y][x]) ; sleep(0.15)
                if keydown(KEY_DOT): GUI.PICT_EDIT = Picture([[color(GUI.default_color) for _ in range(16)] for _ in range(16)]) ; GUI.PICT_EDIT.draw(80,35,10) ; x,y = 0,0 ; draw_curs(x,y,Screen.palette["CursorColor"]) ; sleep(GUI.time)
                if keydown(KEY_EXP): GUI.PICT_EDIT[y][x] = color(GUI.default_color) ; fill_rect(80+x*10,35+y*10,10,10,GUI.PICT_EDIT[y][x]) ; draw_curs(x,y) ; draw_string(str(GUI.PICT_EDIT[y][x])+" "*12,85,202,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"]) ; sleep(GUI.time)
                if keydown(KEY_BACKSPACE): GUI.clean() ; GUI.Menu.draw() ; break
    class Show:
        @staticmethod
        def draw():
            def update(): I.curs.draw(80,35,10) ; draw_string(str(I.curs.name)+" "*10 if I.curs.name != "DefaultName" else " "*20,130,202,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"]) ; sleep(0.10)
            GUI.clean() ; I = iter(Curseur(*GUI.PICTURES,default=GUI.PICTURES[0]))
            draw_string("Show",139,10,Screen.palette["TitleColor"],Screen.palette["SecondaryText"]) ; update()
            while True:
                if keydown(KEY_LEFT) or keydown(KEY_UP): I.sens = "L" ; next(I) ; update()
                if keydown(KEY_RIGHT) or keydown(KEY_DOWN): I.sens = "R" ; next(I) ; update()
                if keydown(KEY_BACKSPACE): GUI.clean() ; GUI.Menu.draw() ; break
    class Settings:
        @staticmethod
        def draw():
            def draw_curseur(curseur):
                if curseur == "pas":
                    draw_string(">   "+str(GUI.pas)+"   <    ",165,80,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("    "+str(GUI.size)+"        ",165,110,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("    "+GUI.default_color+"        ",165,170,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                elif curseur == "size":
                    draw_string("    "+str(GUI.pas)+"       ",165,80,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string(">   "+str(GUI.size)+"   <    ",165,110,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("    "+str(GUI.time)+"        ",165,140,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                elif curseur == "time":
                    draw_string("    "+str(GUI.size)+"       ",165,110,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string(">   "+str(GUI.time)+"   <    ",165,140,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("    "+GUI.default_color+"        ",165,170,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                elif curseur == "default base color":
                    draw_string("    "+str(GUI.pas)+"       ",165,80,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string("    "+str(GUI.time)+"        ",165,140,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
                    draw_string(">   "+GUI.default_color+"   <    ",165,170,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            GUI.clean() ; I = iter(Curseur("pas","size","time","default base color")) ; I_pas = iter(Curseur(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,default=GUI.pas)) ; I_size = iter(Curseur(16,24,32,default=GUI.size)) ; I_time = iter(Curseur(0,0.01,0.05,0.1,0.15,0.2,default=GUI.time)) ; I_default_color = iter(Curseur("white","black","blue","red","green","pink","purple","magenta","brown","yellow","orange",default=GUI.default_color))
            draw_string("Settings",110,30,Screen.palette["TitleColor"],Screen.palette["SecondaryText"])
            draw_string("pas",25,80,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("size",25,110,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("time",25,140,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("default color",25,170,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("    "+str(GUI.pas)+"       ",165,80,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("    "+str(GUI.size)+"        ",165,110,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("    "+str(GUI.time)+"        ",165,140,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            draw_string("    "+GUI.default_color+"        ",165,170,Screen.palette["PrimaryText"],Screen.palette["SecondaryText"])
            while True:
                if keydown(KEY_RIGHT) and I.curs == "pas": I_pas.sens = "R" ; next(I_pas) ; GUI.pas = I_pas.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_LEFT) and I.curs == "pas": I_pas.sens = "L" ; next(I_pas) ; GUI.pas = I_pas.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_RIGHT) and I.curs == "size": I_size.sens = "R" ; next(I_size) ; GUI.size = I_size.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_LEFT) and I.curs == "size": I_size.sens = "L" ; next(I_size) ; GUI.size = I_size.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_RIGHT) and I.curs == "time": I_time.sens = "R" ; next(I_time) ; GUI.time = I_time.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_LEFT) and I.curs == "time": I_time.sens = "L" ; next(I_time) ; GUI.time = I_time.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_RIGHT) and I.curs == "default base color": I_default_color.sens = "R" ; next(I_default_color) ; GUI.default_color = I_default_color.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_LEFT) and I.curs == "default base color": I_default_color.sens = "L" ; next(I_default_color) ; GUI.default_color = I_default_color.curs ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_UP): I.sens = "L" ; next(I) ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_DOWN): I.sens = "R" ; next(I) ; draw_curseur(I.curs) ; sleep(0.15)
                if keydown(KEY_BACKSPACE): GUI.clean() ; GUI.Menu.draw() ; break

GUI.main()