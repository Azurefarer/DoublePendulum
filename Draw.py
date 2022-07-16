import pygame as pg
import numpy as np

g = 9.8

class PendulumDraw:

    def __init__(self, Win, object):

        self.object = object
        self.Win = Win

    
    def draw(self):

        state = self.object.get_state()

        x = self.object.xaxis + self.object.l * np.sin(state[0])
        y = self.object.yaxis + self.object.l * np.cos(state[0])
                    
        pg.draw.lines(self.Win, self.object.color, False, [(self.object.xaxis, self.object.yaxis), (x, y)], 2)
        pg.draw.circle(self.Win, self.object.color, (x, y), 20)       
        pg.draw.circle(self.Win, (255, 255, 255), (self.object.xaxis, self.object.yaxis), 6)


    def draw_data(self):

        state = self.object.get_state()
        
        if len(self.object.data) >= 1500:
            self.object.data.pop(0)
            self.object.data.append((6000 - g * self.object.l - (.5 * (state[1] * self.object.l)**2 - g * self.object.l * np.cos(state[0])) * 1000000) / 7)
        else:
            self.object.data.append((6000 - g * self.object.l - (.5 * (state[1] * self.object.l)**2 - g * self.object.l * np.cos(state[0])) * 1000000) / 7)

        #pairing index values with the list values in a new list
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y) for x, y in enumerate(self.object.data)], 1)




class DblPendulumDraw:

    def __init__(self, Win, object):

        self.object = object
        self.Win = Win

    
    def draw(self):

        state = self.object.get_state()

        x1 = self.object.xaxis + self.object.l1 * np.sin(state[0][0])
        y1 = self.object.yaxis + self.object.l1 * np.cos(state[0][0])

        x2 = x1 + self.object.l2 * np.sin(state[0][1])
        y2 = y1 + self.object.l2 * np.cos(state[0][1])
                    
        pg.draw.lines(self.Win, self.object.color, False, [(self.object.xaxis, self.object.yaxis), (x1, y1)], 2)
        pg.draw.circle(self.Win, self.object.color, (x1, y1), 20)       
        pg.draw.circle(self.Win, (255, 255, 255), (self.object.xaxis, self.object.yaxis), 6)
        pg.draw.lines(self.Win, self.object.color, False, [(x1, y1), (x2, y2)], 2)
        pg.draw.circle(self.Win, self.object.color, (x2, y2), 20)     


    def draw_data(self):

        state = self.object.get_state()

        Energy = self.object.get_energy(state)
        
        if len(self.object.data) >= 1500:
            self.object.data.pop(0)
            self.object.data.append(50 - (Energy[1] - Energy[0]) * 100000000)
        else:
            self.object.data.append(50 - (Energy[1] - Energy[0]) * 100000000)

        #pairing index values with the list values in a new list
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y) for x, y in enumerate(self.object.data)], 1)