import pygame as pg 

y, step, head = segments = [15, 16, 17]
n, apple = step, 99
screen_fill = pg.display.set_mode([225]* 2, pg.SCALED).fill

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            step = (event.key % 4 * 17 + 15) % 49 - n
    
    segments = segments[apple != head:] + [head + step]
    screen_fill("black")
    if apple == head:
        apple = segments[0]
    for i, v in enumerate([apple] + segments):
        screen_fill('green' if i else 'red',
                    ((v - 1) % n * y,  (v - n) // n * y, y, y))
    pg.display.flip()
    head += step
    pg.time.wait(100)
