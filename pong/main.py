from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    ReferenceListProperty,
)
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongPaddle(Widget):
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def bouce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2.0)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + (offset * 2.0)

    def move(self, ball):
        self.velocity_y = ball.velocity_y * (3.0 / 5.0)
        if self.velocity_y > 10.0:
            self.velocity_y = 10.0
        self.pos = Vector(*self.velocity) + self.pos


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.paused = False

    def _on_keyboard_down(self, *args):
        if args[1][1] == 'spacebar':
            self.paused = not self.paused

    def serve_ball(self, vel=(4.0, 0.0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        self.player2.center_y = self.center_y

    def update(self, dt):
        if self.paused:
            return
        self.ball.move()
        self.player1.bouce_ball(self.ball)
        self.player2.bouce_ball(self.ball)
        self.player2.move(self.ball)
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4.0, 0.0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4.0, 0.0))

    def on_touch_move(self, touch):
        if self.paused:
            return
        if touch.y <= self.player1.height / 2.0:
            self.player1.x = self.x
        elif touch.y >= (self.height - self.player1.height / 2.0):
            self.player1.top = self.height
        else:
            self.player1.center_y = touch.y


class PongApp(App):

    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    app = PongApp()
    app.run()
