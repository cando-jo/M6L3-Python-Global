#pgzero

WIDTH = 600
HEIGHT = 400
FPS = 30
TITLE = "Hayvan Avcısı"

arkaplan = Actor("arkaplan")
zurafa = Actor("zürafa", (150, 250))
puan = 0
artis_miktari = 1

bonus1 = Actor("bonus", (450, 100))
bonus2 = Actor("bonus", (450, 200))

def draw():
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
    if button == mouse.LEFT:
        if zurafa.collidepoint(pos):
            puan += artis_miktari
            zurafa.y = 200
            animate(zurafa, tween='bounce_end', duration=0.5, y=250)
            
    

