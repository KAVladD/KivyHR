from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class HeheApp(App):
    def build(self):
        bl1=BoxLayout(orientation='vertical')
        bl2=BoxLayout()
        
        bt1=Button(text='10',on_press=self.f)
        bt2=Button(text='30')
        bt3=Button(text='60')
        self.lbl=Label(text='0')
        
        bl2.add_widget(bt1)
        bl2.add_widget(bt2)
        bl2.add_widget(bt3)
        
        bl1.add_widget(self.lbl)
        bl1.add_widget(bl2)
        
        return bl1
    def f(self,instance):
        self.lbl.text='72'
        
if __name__=='__main__':
    HeheApp().run()