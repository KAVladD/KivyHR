from kivy.uix.camera import Camera
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from scipy.signal import find_peaks_cwt

import matplotlib.pyplot as plt

class camApp(App):   
    def build(self):
        self.cam=Camera(index=0, resolution=(1,1))
        bl=BoxLayout()
        btt=Button(text='1',on_press=self.g)
        self.lbl=Label(text='0')
        bl.add_widget(self.cam)
        bl.add_widget(self.lbl)
        bl.add_widget(btt)
        self.i=0
        self.a=[] 
        return bl
    
    def g(self,instance):
        Clock.schedule_interval(self.f,0.1)
    
    def f(self,instance):
        if self.i==52:
            for j in range(52):
                
                #print(self.a[j])
                
                self.a[j]=sum(self.a[j].pixels)
                
            print(*self.a)
            
            c=[]
            for j in range(50):
                c.append((self.a[j]+self.a[j+1]+self.a[j+2])/3)
            ln=[[j] for j in range(1,6+1)]
            #points=find_peaks_cwt(c,ln)
            #d=0 
            #for j in range(len(points)-1): 
                #d+=points[j+1]-points[j] 
            #tau=d/(len(points)-1)*0.1
            
            #print(tau)
            plt.plot(range(52),self.a)
            plt.plot(range(50),c)
            plt.show()
            
            #self.lbl.text=str(int(60/tau))
            self.i=0
            self.a=[]
            return False
        #frame=self.cam.texture
        self.a.append(self.cam.texture)
        print(self.a[-1])
        self.i+=1       
      
if __name__=='__main__':
    camApp().run()