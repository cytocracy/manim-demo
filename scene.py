
from manim import *
from manim.opengl import *
from networkx import center
from random import random, uniform


class Fader(Scene):
    def construct(self):
        
        fader = VGroup().add(Line([0,0,0], [0,2,0]).center(), Rectangle(width=.2, height=.3).set_fill(WHITE, opacity=1).center().shift(DOWN*.9))
        # self.add(fader)
        line = Circle()
        arr = VGroup().add(*[Mobject.copy(fader) for i in range(20)])
        self.add(arr)
        
        test = arr.copy()
        test.arrange()
        for k in VGroup().add(*[x[1] for x in test]): k.shift(UP*.9)
        
        
        self.play(AnimationGroup(*[Transform(arr[i], test[i]) for i in range(len(arr))], lag_ratio=.008))
        
        
        knobs = VGroup().add(*[x[1] for x in arr])
        # self.play(AnimationGroup(*[knob.animate.shift(UP*.9) for knob in knobs], lag_ratio=.05, run_time=1))
        kn = knobs[0]
        self.play(AnimationGroup(*[knob.animate(rate_func=wiggle).shift(UP*.6) for knob in knobs], lag_ratio=.2, run_time=4))
        self.play(AnimationGroup(*[knob.animate(rate_func=there_and_back).shift(UP*(uniform(-1,1))) for knob in knobs]))