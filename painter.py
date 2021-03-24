import pygame as pg
from random import randint
W = 1600
H = 900
pg.init()
win = pg.display.set_mode((W, H))


WHITE = (255, 255, 255)
typep = 1
size = 10

win.fill(WHITE)
pg.display.update()

def painton():
    pg.time.delay(50)    
    if typep == 1:
        pg.draw.circle(win, (0, 0, 0), mouse, 3*size)
        pg.display.update()
    elif typep == 2:
        pg.draw.rect(win, (0, 0, 0), (mouse[0]-20, mouse[1]-20, 6*size, 6*size))
        pg.display.update()
    elif typep == 3:
        pg.draw.polygon(win, (0, 0, 0), 
        [[mouse[0]-4*size, mouse[1]-1*size], [mouse[0]-1*size, mouse[1]-1*size], 
        [mouse[0], mouse[1]-4*size], [mouse[0]+1*size, mouse[1]-1*size],
        [mouse[0]+4*size, mouse[1]-1*size], [mouse[0]+1.75*size, mouse[1]+0.6*size],
        [mouse[0]+3*size, mouse[1]+4*size], [mouse[0], mouse[1]+2*size],
        [mouse[0]-3*size, mouse[1]+4*size], [mouse[0]-1.75*size, mouse[1]+0.6*size]])
        pg.display.update()



while 1:        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit() #можно ли это оформить также как строчки 43-45


    
    mouse = pg.mouse.get_pos()
    clicked = pg.mouse.get_pressed(5) 
    key = pg.key.get_pressed()
    
    if clicked[0]==1:   
        painton()

    if clicked[2]==1 or key[pg.K_TAB]:
        typep +=1
        if typep == 4:
            typep = 1 
        pg.time.delay(200)


    if clicked[1]==1 or key[pg.K_SPACE]:
        win.fill(WHITE)
        pg.display.update()


    if clicked[4]==1 or key[pg.K_UP]:
        size+=1
        pg.time.delay(100)
    if clicked[3]==1 or key[pg.K_DOWN]:
        size-=1    
        pg.time.delay(100)
        
# ЛКМ - рисовать
# ПКМ/TAB - сменить фигуру
# Колесико/Пробел - стереть
# 4-5 Кнопки мыши/Стрелки - менять размер