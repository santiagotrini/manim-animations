#!/usr/bin/env python

from manimlib.imports import *

class Distributive(Scene):
    def construct(self):
        squareB = Square()
        squareB.shift(LEFT * 1)
        squareC = Rectangle(height=2, width=3)
        squareB.set_fill(BLUE, opacity=0.6)
        squareC.set_fill(RED, opacity=0.6)
        squareC.next_to(squareB, RIGHT, buff=0)
        labelB = TexMobject("b")
        labelC = TexMobject("c")
        labelA = TexMobject("a")
        labelB.next_to(squareB, DOWN)
        labelC.next_to(squareC, DOWN)
        labelA.next_to(squareB, LEFT)
        groupB = VGroup(squareB, labelB)
        groupC = VGroup(squareC, labelC)
        formula = TexMobject("a(b+c) =", "ab", "+", "ac")
        formula[1].set_color(BLUE);
        formula[3].set_color(RED);
        formula.next_to(groupB, DOWN, buff=1)
        formula.shift(RIGHT * 1)
        formula.scale(1.5)
        self.play(Write(groupB))
        self.play(Write(groupC))
        self.play(Write(labelA))
        self.play(Write(formula[0]))
        self.play(ReplacementTransform(groupB.copy(), formula[1]))
        self.play(Write(formula[2]))
        self.play(ReplacementTransform(groupC.copy(), formula[3]))
        self.wait(3)
