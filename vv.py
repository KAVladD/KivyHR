from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
import numpy as np
import cv2
from kivy.uix.boxlayout import BoxLayout

class LastHopeApp(App):
    def build(self):
        BL=BoxLayout(orientation='vertical')
        self.lbl=Label(text='0')
        btt=Button(text='take',on_press=self.shot)
        BL.add_widget(self.lbl)
        BL.add_widget(btt)
        self.cap=cv2.VideoCapture(0)
        return BL
    def shot(self,instance):
        ret, frame = self.cap.read()
        b,g,r=cv2.split(frame)
        self.lbl.text=str((np.sum(b)+np.sum(g)+np.sum(r))//1000)
    
if __name__=='__main__':
    LastHopeApp().run()