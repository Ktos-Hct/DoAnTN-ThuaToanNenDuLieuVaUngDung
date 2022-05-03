from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
import cv2
from kivy.clock import Clock

from kivy.graphics.texture import Texture
#
class Manphu(MapMarkerPopup):
    DulieuNode=[]
    def on_release(self):
        self.momanhinhphu()
    def momanhinhphu(self):
        ####
        self.image=Image(pos_hint={'center_x':0.4,'center_y':0.5},size_hint=(1, 1))
        self.capture=cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video,1.8/38.8)
        ####
        layout=GridLayout(cols=2,spacing=[1,1])
        #tieude=FloatLayout()
        floatlayout1=FloatLayout(size_hint=(0.2,0.3))
        floatlayout2=FloatLayout(size_hint=(0.2,0.7))
        button=Button(text="Up-File",size_hint=(0.2,0.1),pos_hint={'center_x':0.1,'center_y':0.9},background_color=[0, 0, 1, 1])
        button1 = Button(text="Run", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.1, 'center_y': 0.8},background_color=[0, 0, 1, 1])
        button2 = Button(text="Exit", size_hint=(0.1, 0.1), pos_hint={'center_x': 0, 'center_y': 0.05},background_color=[1, 1, 1, 1],on_press=self.tat)
        IdNode=Label(text="ID: "+str(self.DulieuNode[0]),pos_hint={'center_x': 0.05,'center_y':0.7})
        Thongbao1 = Label(text="Hinh anh tu Camera " , pos_hint={'center_x': 0.4, 'center_y': 0.95})
        Trangthai=Label(text="Status: "+str(self.DulieuNode[2]),pos_hint={'center_x': 0.15,'center_y':0.65})
        #tieude1 = Label(text="Status: " + str(self.DulieuNode[1]), pos_hint={'center_x': 0.15, 'center_y': 0.65})
        #tieude.add_widget(tieude1)
        layout.add_widget(floatlayout1)
        layout.add_widget(floatlayout2)
        floatlayout1.add_widget(button)
        floatlayout1.add_widget(button1)
        floatlayout1.add_widget(IdNode)
        floatlayout1.add_widget(Trangthai)
        floatlayout2.add_widget(Thongbao1)
        floatlayout2.add_widget(button2)
        floatlayout2.add_widget(self.image)
        self.popupWindow = Popup( title="Tram Phat Quang Cao "+str(self.DulieuNode[1]), content=layout, size_hint=(0.5, 0.5),auto_dismiss=False,title_align='center',title_color=[0, 1, 1, 1])
        self.popupWindow.open()  # show the popup
        #if()

    def load_video(self,*args):
        ret,frame=self.capture.read()
        self.image_frame=frame
        buffer=cv2.flip(frame,0).tostring()
        texture=Texture.create(size=(frame.shape[1],frame.shape[0]),colorfmt='bgr')
        texture.blit_buffer(buffer,colorfmt='bgr',bufferfmt='ubyte')
        self.image.texture=texture
    def tat(self,*args):
        self.capture.release()
        cv2.destroyAllWindows()
        self.popupWindow.dismiss()

