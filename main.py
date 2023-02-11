
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.image import Image
Builder.load_string('''
<Mygridlayout>
    id:my_widget
     
    BoxLayout:
        size:root.height ,root.width
        
        orientation:'vertical'
        spacing:29
        padding:30
        Image:
            source:''
            id:my_image
        FileChooserIconView:
            id:filechoser
            on_selection:my_widget.seleceted(filechoser.selection)
        RoundedButton:
            text:'submit'
            pos_hint:{'center_y':5.5}
            size_hint:(0.8,.2)
            on_press:print('shiva')
<RoundedButton@Button>
    background_normal:''
    background_color:(0,0,0,0)
    canvas.before:
        Color:
            rgba:(48/255,84/255,150/255,1)
        RoundedRectangle:
            pos:self.pos
            size:self.size
            radius:[50]
            



''')
class Mygridlayout(Widget):
    def seleceted(self,filename):
        a=self.ids.my_image.source=filename[0]
        self.Image.save(a)
class Myapp(App):
    def build(self):
        return  Mygridlayout()
if __name__=='__main__':
    Myapp().run()