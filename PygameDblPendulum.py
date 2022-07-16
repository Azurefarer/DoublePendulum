from operator import truediv
from xml.dom.expatbuilder import theDOMImplementation
import pygame as pg
import numpy as np
from Integrator import RK4Integrator as RK4
import Draw
from DoublePendulum import DblPendulum
pg.init()


#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Pendulum")

g = 9.8


def main():
    run = True
    clock = pg.time.Clock()
    t = 0

    ad = DblPendulum(200, 300, 1, 1, np.deg2rad(181), np.deg2rad(0), (200, 200, 200))

    rkad = RK4(ad)
    rk = [rkad, ad]

    dad = Draw.DblPendulumDraw(Win, ad)

    counter = 0

    while run:
        
        
        dt = 1/100
        t += dt
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False


        #get state, integrate, set state
        rk[1].set_state1(rk[0].integrate(rk[1].get_state(), dt))


        

        if counter % 50 == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            dad.draw()
            dad.draw_data()
            pg.display.update()

        counter += 1

    pg.quit()


main()