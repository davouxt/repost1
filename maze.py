from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, imagen, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(imagen), (70,70))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed 

    def reset(self):
        ventana.blit(self.image, (self.rect.x, self.rect.y))

class muro(sprite.Sprite):
    def __init__(self, width, height,pared_x, pared_y, color1= 0, color2=0, color3= 0):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.image = ((self.color1, self.color2, self.color3))
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = pared_x
        self.rect.y = pared_y

    def dib_wall(self):
        draw.rect(ventana, (self.color1, self.color2, self.color3), (self.rect.x, self.rect.y, self.width, self.height)) 



class Player(GameSprite):
    def actualizar(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.x < vent_v -65:
            self.rect.x += self.speed
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed

class Enemy(GameSprite):
    def actualizar(self):
        if self.rect.x > vent_v -65:
            self.direccion = "izquierda"
        if self.rect.x <500:
            self.direccion = "derecha"

        if self.direccion == "derecha":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed





ventana =display.set_mode([700,500])

vent_h = 500
vent_v = 700
backg = transform.scale(image.load("background.jpg"), (700, 500))
jugador = Player("hero.png", 0, 100, 5)
enemigo = Enemy("cyborg.png", 0, 0, 5)
murop1 = muro(25, 220, 100, 150, 184, 129, 39)
murop2 = muro(25, 270, 450, 100, 10, 104, 39)
murop3 = muro(450, 40, 50, 470, 184, 129, 39)
murop4 = muro(25, 350, 275, 200, 184, 129, 39)
murop5 = muro(265, 20, 210, 100, 184, 129, 39)
murop6 = muro(25, 200, 450, 150)
murop7 = muro(25, 350, 100, 50)
murop8 = muro(25, 150, 450, 50)
#DIAGONAL
#___________Width, ALtura, X, Y, colores
murod1 = muro(25, 30, 100, 120, 184, 129, 39)
murod2 = muro(45, 10, 100, 110, 10, 104, 39)
murod3 = muro(25, 30, 110, 100, 184, 129, 39)
murod4 = muro(45, 10, 110, 90, 10, 104, 39)
murod5 = muro(25, 30, 120, 80, 184, 129, 39)
murod6 = muro(45, 10, 120, 70, 10, 104, 39)
murod7 = muro(25, 30, 130, 60, 184, 129, 39)
murod8 = muro(45, 10, 130, 50, 10, 104, 39)
murod9 = muro(25, 30, 140, 40, 184, 129, 39)
murod10 = muro(45, 10, 140, 30, 10, 104, 39)
murod11 = muro(25, 30, 150, 20, 184, 129, 39)
murod12= muro(45, 10, 150, 10, 10, 104, 39)
#abajo
morda1 = muro(25, 30, 170, 10, 10, 104, 39)
morda2 = muro(45, 10, 170, 20, 184, 129, 39)
morda3 = muro(25, 30, 180, 30, 10, 104, 39)
morda4 = muro(45, 10, 180, 40, 184, 129, 39)
morda5 = muro(25, 30, 190, 50, 10, 104, 39)
morda6 = muro(45, 10, 190, 60, 184, 129, 39)
morda7 = muro(25, 30, 200, 70, 10, 104, 39)
morda8 = muro(45, 10, 200, 80, 184, 129, 39)
morda9 = muro(25, 30, 210, 90, 10, 104, 39)
morda10 = muro(45, 10, 210, 100, 184, 129, 39)




#Comando html color madera 184, 129, 39
#comando html color hoja 10, 104, 39



clock =time.Clock()
fps = 60
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    ventana.blit(backg,(0,0))
    
    
    murop1.dib_wall()
    murop2.dib_wall()
    murop3.dib_wall()
    murop4.dib_wall()
    murop5.dib_wall()
    #murop6.dib_wall()
    #murop7.dib_wall()
    #murop8.dib_wall()
    
    murod1.dib_wall()
    murod2.dib_wall()
    murod3.dib_wall()
    murod4.dib_wall()
    murod5.dib_wall()
    murod6.dib_wall()
    murod7.dib_wall()
    murod8.dib_wall()
    murod9.dib_wall()
    murod10.dib_wall()
    murod11.dib_wall()
    murod12.dib_wall()

    morda1.dib_wall()
    morda2.dib_wall()
    morda3.dib_wall()
    morda4.dib_wall()
    morda5.dib_wall()
    morda6.dib_wall()
    morda7.dib_wall()
    morda8.dib_wall()
    morda9.dib_wall()
    morda10.dib_wall()


    jugador.reset()
    enemigo.reset()

    jugador.actualizar()
    enemigo.actualizar()




    display.update()
    clock.tick(fps)