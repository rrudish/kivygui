from random import random

from kivy.app import App
from kivy.graphics import Color, Line
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1.0, 1.0)
        with self.canvas:
            Color(*color, mode='hsv')
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, *args):
        self.painter.canvas.clear()


if __name__ == '__main__':
    app = MyPaintApp()
    app.run()
