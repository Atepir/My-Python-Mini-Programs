"""Procedural Functions Drawing 2D GUI"""

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
import string

Window.clearcolor = (1, 1, 1, 1)

def f(x):
    try :
        x.isascii()
        return str(x)
    except:
        return x ** 2

def intervalle(i, j):
    if i >= j:
        return i
    else:
        print("%.2f\n"%i)
        return intervalle(i+0.01, j)

intervalle(1, 2)

class Axes(Widget):
    def build(self):
        self.parent = FloatLayout()
        self.y_text = Label(text='[color=ff3333]Y[/color]', markup=True, size_hint=(0.15, 0.1),
                            pos_hint={'x': 0.41, 'y': 0.91})
        self.x_text = Label(text='[color=3333ff]X[/color]', markup=True, size_hint=(0.15, 0.1),
                            pos_hint={'x': 0.90, 'y': 0.42})
        self.title = Label(text='[color=ff33ff]f(x) = %s[/color]'%f('x²'), markup=True, size_hint=(0.15, 0.1),
                            pos_hint={'x': 0.5, 'y': 0.4})

        self.parent.add_widget(self.title)
        self.parent.add_widget(self.x_text)
        self.parent.add_widget(self.y_text)
        with self.parent.canvas.before:
            #Axes
            Color(0, 0, 0, 1, mode="rgba")
            self.rect = Rectangle(pos=(400, 0), size=(2, 1000))
            Color(0, 0, 0, 1, mode="rgba")
            self.rect = Rectangle(pos=(0, 300), size=(1000, 2))
            # Numérotation
            for i in range(0, 1000):
                if i % 50 == 0:
                    Color(0, 0, 0, 1, mode="rgba")
                    self.rect = Rectangle(pos=(i, 300), size=(1, 10))
            for j in range(0, 1000):
                if j % 50 == 0:
                    Color(0, 0, 0, 1, mode="rgba")
                    self.rect = Rectangle(pos=(400, j), size=(10, 1))
            for x in range(0, 500, 50):
                Color(1, 0, 0, 1, mode="rgba")
                self.rect = Rectangle(pos=(x + 400, x ** 2), size=(3, 3))
                """for x1 in range(x, x+50):
                    Color(0, 1, 1, 1, mode="rgba")
                    self.rect = Rectangle(pos=(x1 + 400, f(x1) + 300), size=(3, 3))"""
        return self.parent

class Windows(App):

    def build(self):
        return Axes().build()


if __name__ == "__main__":
    Windows().run()