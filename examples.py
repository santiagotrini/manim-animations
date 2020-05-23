#!/usr/bin/env python

from manimlib.imports import *

class Distributive(Scene):
    def construct(self):
        title = TextMobject("Propiedad distributiva")
        title.scale(2)
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
        self.play(Write(title))
        self.wait()
        self.play(FadeOutAndShift(title,direction=UP))
        self.play(Write(groupB))
        self.play(Write(groupC))
        self.play(Write(labelA))
        self.play(Write(formula[0]))
        groupB = VGroup(squareB, labelB, labelA)
        groupC = VGroup(squareC, labelC, labelA)
        self.play(ReplacementTransform(groupB.copy(), formula[1]))
        self.play(Write(formula[2]))
        self.play(ReplacementTransform(groupC.copy(), formula[3]))
        self.wait(3)


class AndGate(Scene):
    def construct(self):
        # titulo
        title = TextMobject("Lógica Digital")
        subtitle = TextMobject("Compuerta AND")
        self.play(Write(title))
        self.wait()
        self.play(FadeOutAndShift(title, direction=DOWN))
        self.play(Write(subtitle))
        self.wait()
        self.play(FadeOutAndShift(subtitle, direction=DOWN))
        # logica proposicional
        title = TextMobject(r"\underline{Logica proposicional}")
        title.to_edge(UP)
        self.play(Write(title))
        table = TextMobject(r"""
        \begin{tabular}{c|c|c}
        $p$ & $q$ & $p \land q$ \\
        \hline
        F & F & F \\
        F & V & F \\
        V & F & F \\
        V & V & V \\
        \end{tabular}
        """)
        table.to_edge(LEFT)
        self.play(Write(table))
        text = TextMobject(r"""
        La conjunción es verdadera \\
        si y solo si ambas proposiciones \\
        son verdaderas
        """)
        text.next_to(table, RIGHT,buff=1.5)
        self.play(Write(text))
        formula = TextMobject(r"""
        $p \land q =$ V $\Longleftrightarrow p =$ V y $q=$ V
        """)
        formula.next_to(table, RIGHT,buff=1.5)
        self.wait(2)
        self.play(Transform(text, formula))
        self.wait(2)
        all = VGroup(title, table, text)
        self.play(FadeOut(all))
        # algebra de boole
        title = TextMobject(r"\underline{Álgebra de Boole}")
        title.to_edge(UP)
        self.play(Write(title))
        table = TextMobject(r"""
        \begin{tabular}{c|c|cc}
        $A$ & $B$ & $AB$ & $\boldsymbol{\leftarrow}$ \\
        \cline{1-3}
        0 & 0 & 0 & $\boldsymbol{\leftarrow}$ \\
        0 & 1 & 0 & $\boldsymbol{\leftarrow}$ \\
        1 & 0 & 0 & $\boldsymbol{\leftarrow}$ \\
        1 & 1 & 1 & $\boldsymbol{\leftarrow}$ \\
        \end{tabular}
        """)
        table.to_edge(LEFT)
        self.play(
            Write(table[0][0:6]),
            Write(table[0][7:12]),
            Write(table[0][14:18]),
            Write(table[0][20:24]),
            Write(table[0][26:30])
            )
        # dibujar circuito
        gate = SVGMobject("andgate")
        gate.scale(1)
        gate.next_to(table, RIGHT,buff=1.5)
        gate.set_style(fill_opacity=0,stroke_opacity=1)
        labelA = TexMobject("A")
        labelB = TexMobject("B")
        labelB.next_to(labelA,DOWN,buff=0.85)
        inputs = VGroup(labelA, labelB)
        inputs.next_to(gate, LEFT)
        output = TexMobject("AB")
        output.next_to(gate, RIGHT)
        self.play(Write(gate), Write(inputs), Write(output))
        # animacion circuito
        # 1era fila
        self.play(
            Write(table[0][13]),
            table[0][8].set_color, RED,
            table[0][10].set_color, RED
        )
        table[0][12].set_color(RED)
        auxA = table[0][8].copy()
        auxB = table[0][10].copy()
        auxQ = table[0][12].copy()
        auxQ.move_to(output.get_center())
        self.play(
            FadeOut(inputs),
            auxA.move_to, labelA.get_center(),
            auxB.move_to, labelB.get_center()
        )
        dotA = Dot(opacity=0.8).scale(1.5).move_to(auxA.get_center()).set_color(RED)
        dotB = Dot(opacity=0.8).scale(1.5).move_to(auxB.get_center()).set_color(RED)
        self.play(
            Transform(auxA, dotA),
            Transform(auxB, dotB)
        )
        self.play(
            FadeOutAndShift(auxA, direction=RIGHT * 2),
            FadeOutAndShift(auxB, direction=RIGHT * 2)
        )
        dotQ = Dot(opacity=0.8).scale(1.5).move_to(auxQ.get_center()).set_color(RED)
        self.play(
            FadeOut(output),
            FadeInFrom(dotQ, direction=LEFT * 2)
        )
        self.play(Transform(dotQ, auxQ))
        self.play(Transform(dotQ, table[0][12]))
        # 2da fila
        self.play(ReplacementTransform(table[0][13], table[0][19]))
        self.play(
            table[0][8].set_color, WHITE,
            table[0][10].set_color, WHITE,
            table[0][12].set_color, WHITE,
            table[0][14].set_color, RED,
            table[0][16].set_color, GREEN
        )
        table[0][18].set_color(RED)
        auxA = table[0][14].copy()
        auxB = table[0][16].copy()
        auxQ = table[0][18].copy()
        auxQ.move_to(output.get_center())
        self.play(
            auxA.move_to, labelA.get_center(),
            auxB.move_to, labelB.get_center()
        )
        dotA = Dot(opacity=0.8).scale(1.5).move_to(auxA.get_center()).set_color(RED)
        dotB = Dot(opacity=0.8).scale(1.5).move_to(auxB.get_center()).set_color(GREEN)
        self.play(
            Transform(auxA, dotA),
            Transform(auxB, dotB)
        )
        self.play(
            FadeOutAndShift(auxA, direction=RIGHT * 2),
            FadeOutAndShift(auxB, direction=RIGHT * 2)
        )
        dotQ = Dot(opacity=0.8).scale(1.5).move_to(auxQ.get_center()).set_color(RED)
        self.play(
            FadeInFrom(dotQ, direction=LEFT * 2)
        )
        self.play(Transform(dotQ, auxQ))
        self.play(Transform(dotQ, table[0][18]))
        # 3era fila
        self.play(ReplacementTransform(table[0][19], table[0][25]))
        self.play(
            table[0][14].set_color, WHITE,
            table[0][16].set_color, WHITE,
            table[0][18].set_color, WHITE,
            table[0][20].set_color, GREEN,
            table[0][22].set_color, RED
        )
        table[0][24].set_color(RED)
        auxA = table[0][20].copy()
        auxB = table[0][22].copy()
        auxQ = table[0][24].copy()
        auxQ.move_to(output.get_center())
        self.play(
            auxA.move_to, labelA.get_center(),
            auxB.move_to, labelB.get_center()
        )
        dotA = Dot(opacity=0.8).scale(1.5).move_to(auxA.get_center()).set_color(GREEN)
        dotB = Dot(opacity=0.8).scale(1.5).move_to(auxB.get_center()).set_color(RED)
        self.play(
            Transform(auxA, dotA),
            Transform(auxB, dotB)
        )
        self.play(
            FadeOutAndShift(auxA, direction=RIGHT * 2),
            FadeOutAndShift(auxB, direction=RIGHT * 2)
        )
        dotQ = Dot(opacity=0.8).scale(1.5).move_to(auxQ.get_center()).set_color(RED)
        self.play(
            FadeInFrom(dotQ, direction=LEFT * 2)
        )
        self.play(Transform(dotQ, auxQ))
        self.play(Transform(dotQ, table[0][24]))
        # 4ta fila
        self.play(ReplacementTransform(table[0][25], table[0][31]))
        self.play(
            table[0][20].set_color, WHITE,
            table[0][22].set_color, WHITE,
            table[0][24].set_color, WHITE,
            table[0][26].set_color, GREEN,
            table[0][28].set_color, GREEN
        )
        table[0][30].set_color(GREEN)
        auxA = table[0][26].copy()
        auxB = table[0][28].copy()
        auxQ = table[0][30].copy()
        auxQ.move_to(output.get_center())
        self.play(
            auxA.move_to, labelA.get_center(),
            auxB.move_to, labelB.get_center()
        )
        dotA = Dot(opacity=0.8).scale(1.5).move_to(auxA.get_center()).set_color(GREEN)
        dotB = Dot(opacity=0.8).scale(1.5).move_to(auxB.get_center()).set_color(GREEN)
        self.play(
            Transform(auxA, dotA),
            Transform(auxB, dotB)
        )
        self.play(
            FadeOutAndShift(auxA, direction=RIGHT * 2),
            FadeOutAndShift(auxB, direction=RIGHT * 2)
        )
        dotQ = Dot(opacity=0.8).scale(1.5).move_to(auxQ.get_center()).set_color(GREEN)
        self.play(
            FadeInFrom(dotQ, direction=LEFT * 2)
        )
        self.play(Transform(dotQ, auxQ))
        self.play(Transform(dotQ, table[0][30]))
        self.play(
            table[0][26].set_color, WHITE,
            table[0][28].set_color, WHITE,
            table[0][30].set_color, WHITE,
            FadeOut(table[0][31]),
            FadeIn(inputs),
            FadeIn(output)
        )
        # final
        self.wait(3)
        # TODO: refactor code, un ciclo no estaria mal para la tabla
