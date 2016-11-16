from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *
import random
import math 
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        i =0;
        l=0;
        with self.canvas:
            x = 0;
            y=0;
            sizeCircle = 0.01
            wid = 50
            array = [[0,0], [1,1], [2,2], [3,3],[4,4], [5,5],[6,6],[7,7],[8,8],[9,9]]
            
            for i in range(0, 5):
                Color (random.randint (0,1) ,random.randint (0,1),random.randint (0,1))
                j = random.randint (0,600)
                k = random.randint (0,600)
                if (i>0) :
                     for l in range (0,i):
                        dis = math.sqrt(math.pow((j- array [l][0] ),2) + math.pow((k- array [l][1] ),2))
                        if (dis < (wid +sizeCircle)*2):
                            Color (1. ,0,0)
                            
                
                Line(circle= (self.center_x + j ,self.center_y+k ,sizeCircle), width=wid)
                
                if (i >0):
                    Line (points=[self.center_x+ array[i-1][0]-7 , self.center_y+ array [i-1][1] -7,self.center_x+ j, self.center_y+ k])
                

                        

                array [i][0] = j;
                array [i][1] = k;
        

class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
