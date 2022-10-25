import random as rn
import pygame as pg

## Oppgave 1##
pg.init()

w = 600
h = 650

background = pg.display.set_mode((600, 650))
pg.display.set_caption('Oppgave 1 - Trykk R for å tegne en ny figur')
black = (0, 0, 0)
pg.draw.rect(background, black, [0, 0, 600, 650])
pg.display.flip()

def RandomShape():
    width = rn.randint(1, 40)
    height = rn.randint(1, 40)
    x = rn.randint(0, 600)
    y = rn.randint(0, 650)
    pg.draw.rect(background, (rn.randint(10, 255), rn.randint(10, 255), rn.randint(10, 255)), [x, y, width, height])
    pg.display.flip()


carryOn = True
while carryOn:
    clock = pg.time.Clock()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            carryOn = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_r]:
        RandomShape()

    clock.tick(20)

pg.quit()