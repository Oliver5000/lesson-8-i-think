import random
import pgzrun
WIDTH = 500
HEIGHT = 400
no_of_satellites=10
next=0
lines = []
sats = []
for i in range(no_of_satellites):
    satellite = Actor("satellite")
    satellite.x = random.randint(50,WIDTH-50)
    satellite.y = random.randint(50,HEIGHT-50)
    sats.append(satellite)
def draw():
    screen.blit("background",(0,0))
    number = 1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+20))
        number += 1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,0,0))
def on_mouse_down(pos):
    global lines, next,sats
    if next < no_of_satellites:
        if sats[next].collidepoint(pos):
            if next>0:
                lines.append((sats[next-1].pos,sats[next].pos))
                print(lines)
            next += 1
        else:
            lines=[]
            next=0
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
pgzrun.go()