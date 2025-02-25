from manim import *
from numpy.polynomial.laguerre import lagmul
from pydub.effects import speedup

config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = "#bdf2f0"

style = {"color": BLACK}

def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Circle(
        radius=0.5, stroke_color=color,
    )
    text = MathTex(string, color=color).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result


class Intro(Scene):
	def construct(self):
		text1 = Text("Úlohy s číselnou osou", color=DARK_GRAY).scale(1.5)
		text2 = Text("Úlohy pro pátou třídu", color=DARK_GRAY).scale(1).next_to(text1, DOWN)
		self.play(Write(text1), Write(text2), lag_ratio=0.5)
		self.wait(2)

		self.play(FadeOut(text1), FadeOut(text2))

		uloha1 =  NumberLine(
            x_range=[0,10, 2],
			include_numbers=False,
            length=10,
            color=BLACK,
            label_direction=UP,
			font_size=90
		).set_color(BLACK)

		uloha1_labels = [MathTex("2", **style), MathTex("8", **style), MathTex("A", **style)]
		uloha1.add_labels({2:uloha1_labels[0], 8:uloha1_labels[1], 4:uloha1_labels[2]})
		uloha1.shift(UP*3)
		uloha1_wrap = VGroup(uloha1)

		uloha2 = NumberLine(
			x_range=[-2, 5 ],
			numbers_to_include=[0],
			length=10,
			color=BLACK,
			label_direction=UP,
			font_size=90
		).set_color(BLACK)

		uloha2_labels = [MathTex("A", **style),  MathTex("B", **style)]
		uloha2.add_labels({-1: uloha2_labels[0], 3:uloha2_labels[1]})
		arrow = CurvedArrow(start_point=uloha2.n2p(-1), end_point=uloha2.n2p(3), color=BLACK)
		arrow_text = create_textbox(BLACK, "+4").next_to(arrow.get_center(), DOWN*2.5)

		uloha2_wrap = VGroup(uloha2, arrow, arrow_text, uloha2_labels)
		uloha2_wrap.shift(DOWN * 2)
		self.play(FadeIn(uloha1_wrap), FadeIn(uloha2_wrap))
		self.wait(2)

		self.play(FadeOut(uloha2_wrap), uloha1_wrap.animate.shift(-uloha1_wrap.get_center()).scale(1.3))
		self.wait(2)
		self.play(*[Indicate(i) for i in uloha1_labels[0:2]])
		self.wait(1)
		arrow_tmp = CurvedArrow(start_point=uloha1.n2p(2), end_point=uloha1.n2p(8), color=BLACK)
		arrow_tmp_text = create_textbox(BLACK, "+6").next_to(arrow_tmp.get_bottom(), DOWN)
		uloha1_wrap.add(arrow_tmp, arrow_tmp_text)
		self.play(Write(arrow_tmp), Write(arrow_tmp_text))
		self.wait(1)

		self.play(uloha1_wrap.animate.shift(2*UP))
		self.wait(2)

		uloha1_text = Text("3 dílky = 6\n1 dílek = 2", **style).align_to(uloha1_wrap, DOWN).shift(LEFT*3+DOWN*3)
		self.play(Write(uloha1_text), speed_factor=2)
		self.wait(1)

		arrow_tmp2 = CurvedArrow(start_point=uloha1.n2p(2), end_point=uloha1.n2p(4), color=BLACK)
		arrow_tmp_text2 = create_textbox(BLACK, "+2").next_to(arrow_tmp2.get_bottom(), DOWN)

		self.play(Transform(arrow_tmp, arrow_tmp2), Transform(arrow_tmp_text, arrow_tmp_text2))
		self.wait(2)
		uloha1_text2 = Text("A=4", **style).align_to(uloha1_text, DOWN).shift(DOWN*1)
		self.play(Write(uloha1_text2))
		self.wait(5)

		self.play(FadeOut(uloha1_text), FadeOut(uloha1_text2), FadeOut(uloha1_wrap))
		self.play(FadeIn(uloha2_wrap.shift(-uloha2_wrap.get_center()).scale(1.3)))

		self.wait(1)
		self.play(*[Indicate(i) for i in uloha2_labels])
		self.wait(1)
		self.play(uloha2_wrap.animate.shift(2 * UP))
		uloha2_text = Text("4 dílky = 4\n1 dílek = 1", **style).align_to(uloha2_wrap, DOWN).shift(LEFT * 3 + DOWN * 3)
		self.play(Write(uloha2_text), speed_factor=2)
		self.wait(1)
		vzdalenost = (uloha2.n2p(0) - uloha2.n2p(3))[0]
		arrow_tmp2 = CurvedArrow(start_point=uloha2.n2p(0), end_point=uloha2.n2p(3), color=BLACK, radius=-vzdalenost)
		arrow_tmp2_text = create_textbox(BLACK, "+3").next_to(arrow_tmp2.get_bottom(), DOWN)
		self.play(FadeOut(arrow_text), FadeOut(arrow), FadeIn(arrow_tmp2, arrow_tmp2_text))
		self.wait(2)
		uloha2_text2 = Text("A = -1\nB = 3", **style).align_to(uloha2_text, DOWN).shift(DOWN*1)
		self.play(Write(uloha2_text2), speed_factor=2)
		self.wait(2)
		self.clear()

		uloha3 = NumberLine(
			x_range=[9, 27, 3],
			numbers_to_include=[9],
			length=10,
			color=BLACK,
			label_direction=UP,
			font_size=90
		).set_color(BLACK)

		uloha3_labels = [MathTex("A", **style),  MathTex("B", **style)]
		uloha3.add_labels({15: uloha3_labels[0], 26:uloha3_labels[1]})
		arrow3 = CurvedArrow(start_point=uloha3.n2p(9), end_point=uloha3.n2p(18), color=BLACK)
		arrow_tmp_text3 = create_textbox(BLACK, "\cdot 2").next_to(arrow3.get_bottom(), DOWN)
		uloha3_text = Text("Vyzkoušejte si sami!", **style).shift(DOWN*3)
		self.play(FadeIn(uloha3), FadeIn(arrow3), FadeIn(arrow_tmp_text3, uloha3_text))

		self.wait(10)

