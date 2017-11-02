
#Import 'kivy'
import kivy

#Import subclasses
from kivy.app import App
from kivy.uix.button import Label

class HelloWorld(App):
    def build(self):
        return Label()
        
if __name__ == "__main__":
    HelloWorld().run()