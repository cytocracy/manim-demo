from manim import *

class Shift(Scene):
    def construct(self):
        sq = Square()
        animation = Succession(sq.animate.shift(UP), Write(Tex('hi')))
        self.play(animation)