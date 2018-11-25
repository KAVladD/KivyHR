from kivy.uix.camera import Camera
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from time import time

class camApp(App):   
    def build(self):
        self.cam=Camera(play=False,index=0, resolution=(1,1))
        bl=BoxLayout()
        btt=Button(text='1',on_press=self.g)
        btc=Button(text='вкл', on_press=self.pw)
        self.lbl=Label(text='0')
        bl.add_widget(self.cam)
        bl.add_widget(self.lbl)
        bl.add_widget(btt)
        bl.add_widget(btc)
        return bl
    
    def pw(self,instance):
        self.cam.play=True
        #self.cam=Camera(index=0, resolution=(1,1))
       # if self.cam.play==False:
         #   self.cam.play=True
           # instance.text='выкл'
        #else:
            #self.cam.play=False
            #instance.text='вкл'
    
    def g(self,instance):
        Clock.schedule_interval(self.f,0.1)
    
    def f(self,instance):
        global i,a,b
        if i==50:
            i=0
            for i in range(len(b)-1):
                b[i]=b[i+1]-b[i]
            b.pop(-1)
            s=str(max(b)-min(b))
            self.lbl.text=s
            for i in range(50):
                a[i]=sum(a[i].pixels)
            print(*a)
            b=[]
            a=[]
            return False
        frame=self.cam.texture
        a.append(frame)
        b.append(time())
        i+=1       

i=0
a=[]
b=[]       
if __name__=='__main__':
    camApp().run()