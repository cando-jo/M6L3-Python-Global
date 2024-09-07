#pgzero

WIDTH = 600
HEIGHT = 400
FPS = 30
TITLE = "Hayvan Avcısı"

arkaplan = Actor("arkaplan")
zurafa = Actor("zürafa", (150, 250))
puan = 0
artis_miktari = 1000
mod = "menu"
bonus1 = Actor("bonus", (450, 100))
bonus2 = Actor("bonus", (450, 200))
oyna = Actor("oyna", (300, 100))

def draw():
    if mod == "menu":
        arkaplan.draw()
        oyna.draw()
        screen.draw.text(puan, center=(30, 30), color="white", fontsize=30)
    if mod == "oyun":
        arkaplan.draw()
        zurafa.draw()
        screen.draw.text(puan, center=(150, 100), color="white", fontsize=96)
        bonus1.draw()
        bonus2.draw()
        screen.draw.text("Her 2 saniye 1$", center=(450, 75), color="black", fontsize=19)
        screen.draw.text("Ücret: 15 Puan", center=(450, 110), color="black", fontsize=19)
        screen.draw.text("Her 2 saniye 15$", center=(450, 175), color="black", fontsize=19)
        screen.draw.text("Ücret: 200 Puan", center=(450, 210), color="black", fontsize=19)

def on_mouse_down(button, pos):
    global puan
    global mod
    if button == mouse.LEFT:
        if oyna.collidepoint(pos):
            mod = "oyun"
            
        # eger carpiya tiklarsak modu menu yapcaz
        if zurafa.collidepoint(pos):
            puan += artis_miktari
            zurafa.y = 200
            animate(zurafa, tween='bounce_end', duration=0.5, y=250)
            
        if bonus1.collidepoint(pos) and puan >= 15:
            schedule_interval(bonus_1_icin, 2)
            puan = puan - 15
            
        if bonus2.collidepoint(pos) and puan >= 200:
            schedule_interval(bonus_2_icin, 2)
            puan = puan - 200
        
def bonus_1_icin():
    global puan
    puan += 1
    
def bonus_2_icin():
    global puan
    puan += 15
