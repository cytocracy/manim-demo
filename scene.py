from manim import *
from manim.opengl import * 


class Fader(Scene):
    def construct(self):
        
        fader = VGroup().add(Line([0,0,0], [0,2,0]).center(), Square(side_length=.2).set_fill(WHITE, opacity=.5))
        # self.add(fader)
        line = Circle()
        arr = VGroup().add(*[Mobject.copy(fader) for i in range(20)])
        self.add(arr)
        self.play(arr.animate.arrange())
        self.wait()
        
        gr = Succession()
        
        
        knobs = VGroup().add(*[x[1] for x in arr])
        kn = knobs[0]
        self.play(AnimationGroup(*[knob.animate(rate_func=there_and_back).shift(UP*.6) for knob in knobs], lag_ratio=.1, run_time=2))