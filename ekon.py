from manimlib import *
from manimlib.once_useful_constructs.graph_scene import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class InNOut(Scene):
    def construct(self):
        axes = Axes(x_range=(0, 16), y_range=(0, 9), height=4.5, width=8)
        #xaxis,yaxis = 
        labels = axes.get_axis_labels(x_label_tex='Quantity', y_label_tex='Price').set_color(BLUE)
        #yaxis.arrange(UP)
        self.play(Write(axes, lag_ratio=0.01, run_time=1),Write(labels))

        MC = axes.get_graph(lambda x: 2*x if (x >= 0 and x <= 5) else -69, discontinuities=[0,5], color=GREEN)
        AVC = axes.get_graph(avc, discontinuities=[0,9], color=BLUE)
        ATC = axes.get_graph(atc, discontinuities=[1,9], color=MAROON)

        mc_label = axes.get_graph_label(MC, "MC")
        avc_label = axes.get_graph_label(AVC,"AVC", x = 8)
        atc_label = axes.get_graph_label(ATC,"ATC")

        self.play(
            ShowCreation(MC),
            FadeIn(mc_label,LEFT),
        )
        self.play(
            ShowCreation(AVC),
            FadeIn(avc_label,LEFT),
        )
        self.play(
            ShowCreation(ATC),
            FadeIn(atc_label,LEFT)
        )
        dot = Dot(color=RED).move_to(axes.i2gp(1.5, MC))
        dok = Dot(color=RED).move_to(axes.i2gp(2.25, MC))
        off = axes.get_graph(lambda x: 2*x if x == 1.5 else -69, discontinuities=[1.5,1.5], color=WHITE)
        kita = axes.get_graph(lambda x: 2*x if x == 2.25 else -69, discontinuities=[2.25,2.25], color=WHITE)
        kita_label = axes.get_graph_label(kita, Text("zero-profit point").scale(0.2),x=2.25)
        off_label = axes.get_graph_label(off,Text("shutdown point").scale(0.2),x=1.5)

        profit = axes.get_graph_label(MC, Text("profit zone").scale(0.1), x = 3)
        shutdown = axes.get_graph_label(MC, Text("shutdown zone").scale(0.1), x = 1)
        self.play(
            ShowCreation(dot),
            )
        self.play(
            FadeIn(off_label,RIGHT),
            )
        self.play(
            FadeIn(shutdown,RIGHT),
            )
        self.wait(0.5)
        self.play(FadeOut(off_label,LEFT))
        self.play(dot.animate.move_to(axes.i2gp(2.25, MC)))
        self.play(
            FadeIn(kita_label,RIGHT),
            )
        self.play(
            FadeIn(profit,LEFT),
            )
        self.wait(2)
class EntryExit(Scene):
    def construct(self):
        axes = Axes(x_range=(0, 16), y_range=(0, 9), height=4.5, width=8)
        #xaxis,yaxis = 
        labels = axes.get_axis_labels(x_label_tex='Quantity', y_label_tex='Price').set_color(BLUE)
        #yaxis.arrange(UP)
        self.play(Write(axes, lag_ratio=0.01, run_time=1),Write(labels))

        MC = axes.get_graph(lambda x: 2*x if (x >= 0 and x <= 5) else -69, discontinuities=[0,5], color=GREEN)
        AVC = axes.get_graph(avc, discontinuities=[0,9], color=BLUE)
        ATC = axes.get_graph(atc, discontinuities=[1,9], color=MAROON)

        mc_label = axes.get_graph_label(MC, "MC")
        avc_label = axes.get_graph_label(AVC,"AVC", x = 8)
        atc_label = axes.get_graph_label(ATC,"ATC")

        self.play(
            ShowCreation(MC),
            FadeIn(mc_label,LEFT),
        )
        self.play(
            ShowCreation(AVC),
            FadeIn(avc_label,LEFT),
        )
        self.play(
            ShowCreation(ATC),
            FadeIn(atc_label,LEFT)
        )
        dot = Dot(color=RED).move_to(axes.i2gp(1.5, MC))
        dok = Dot(color=RED).move_to(axes.i2gp(2.25, MC))
        off = axes.get_graph(lambda x: 2*x if x == 1.5 else -69, discontinuities=[1.5,1.5], color=WHITE)
        kita = axes.get_graph(lambda x: 2*x if x == 2.25 else -69, discontinuities=[2.25,2.25], color=WHITE)
        kita_label = axes.get_graph_label(kita, Text("zero-profit point").scale(0.2),x=2.25)
        off_label = axes.get_graph_label(off,Text("shutdown point").scale(0.2),x=1.5)

        profit = axes.get_graph_label(MC, Text("profit zone").scale(0.1), x = 3)
        shutdown = axes.get_graph_label(MC, Text("shutdown zone").scale(0.1), x = 1)
        self.play(
            ShowCreation(dot),
            )
        self.play(
            FadeIn(off_label,RIGHT),
            )
        self.play(
            FadeIn(shutdown,RIGHT),
            )
        self.wait(0.5)
        self.play(FadeOut(off_label,LEFT))
        self.play(dot.animate.move_to(axes.i2gp(2.25, MC)))
        self.play(
            FadeIn(kita_label,RIGHT),
            )
        self.play(
            FadeIn(profit,LEFT),
            )
        self.wait(2)

def avc(x):
    if (x >= 1.5 and x<=9):
        return 0.1*(x-1.5)**2 + 3
    elif (x>=0 and x<1.5):
        return (x-1.5)**2 + 3
    else:
        return -69

def atc(x):
    if (x >= 2.25 and x<=9):
        return 0.1*(x-2.25)**2 + 4.5
    elif (x>=1 and x<2.25):
        return (x-2.25)**2 + 4.5
    else:
        return -69

def latc(x):
    if (x>=0 and x <=12):
        return 0.0014*(x-6)**4 + 4.2
    else:
        return -69

class Monopolyo(GraphScene):
    def construct(self):
        CONFIG = {
        "x_min": 0,
        "x_max": 16,
        "x_axis_width": 8,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 9,
        "y_axis_height": 4.5,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }
        axes = setup_axes()
        axes = Axes(x_range=(0, 16), y_range=(0, 9), height=4.5, width=8)
        #axes.add_coordinate_labels()
        labels = axes.get_axis_labels(x_label_tex='Quantity', y_label_tex='Price').set_color(TEAL).shift(LEFT*2)

        self.play(Write(axes, lag_ratio=0.01, run_time=1),Write(labels))

        # Axes.get_graph will return the graph of a function
        demand = axes.get_graph(lambda x: -1*x + 9 if (x >= 0 and x <= 9) else -69,discontinuities=[0,9],color=BLUE)

        supply = axes.get_graph(lambda x: (2/3)*x if (x >= 0 and x <= 9) else -79,discontinuities=[0,9],color=GREEN)

        suplay = axes.get_graph_label(supply, Text("Marginal Cost").scale(0.3))
        dimand = axes.get_graph_label(demand, Text("Demand").scale(0.3))

        dot = Dot(color=RED).move_to(axes.i2gp(3,demand))

        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
        ShowCreation(demand),
        FadeIn(dimand,RIGHT),
        ShowCreation(supply),
        FadeIn(suplay,RIGHT)
        )
        self.play(
        ShowCreation(dot),
        ShowCreation(h_line),
        ShowCreation(v_line),
        )

        rect = self.get_riemann_rectangles(demand, dx=0.2)
        rect.set_color(YELLOW_D)
        rect.set_stroke(WHITE, 1)

        self.play(ShowCreation(rect), run_time=5)

class MarketWerpa(Scene):
    def construct(self):
        axes = Axes(x_range=(0, 16), y_range=(0, 9), height=4.5, width=8)
        labels = axes.get_axis_labels(x_label_tex='Quantity', y_label_tex='Price').set_color(TEAL).shift(LEFT*2)

        firmd = Text("Firm Demand").set_color(BLUE)
        self.play(Write(firmd))

        self.play(Write(axes, lag_ratio=0.01, run_time=1),Write(labels))

        perpek = axes.get_graph(lambda x: 5 if (x>=0 and x<=12) else -69,discontinuities=[0,12],color=BLUE)
        low = axes.get_graph(lambda x: -0.5*(x-5)+5 if (x>=0 and x<=12) else -69, discontinuities=[0,12], color=BLUE)
        high = axes.get_graph(lambda x: -2*(x-5)+5 if (x>=3 and x<=7) else -69, discontinuities=[3,7], color=BLUE)

        pek = axes.get_graph_label(perpek,Text("Perfect Competition").scale(0.3),x=6)
        lo = axes.get_graph_label(low,Text("Low Market Power").scale(0.3),x=6)
        hi = axes.get_graph_label(high,Text("High Market Power").scale(0.3),x=5)
        self.play(
            ReplacementTransform(firmd,perpek),
            FadeIn(pek, RIGHT),

        )
        self.play(
            ReplacementTransform(perpek,low),
            FadeTransform(pek,lo)
        )
        self.play(
            ReplacementTransform(low,high),
            FadeTransform(lo,hi)
        )
class SuplayDimand(Scene):
    def construct(self):
        axes = Axes(x_range=(0, 16), y_range=(0, 9), height=4.5, width=8)
        #axes.add_coordinate_labels()
        labels = axes.get_axis_labels(x_label_tex='Quantity', y_label_tex='Price').set_color(TEAL).shift(LEFT*2)

        self.play(Write(axes, lag_ratio=0.01, run_time=1),Write(labels))

        # Axes.get_graph will return the graph of a function
        demand = axes.get_graph(lambda x: -(9/5)*(x-2) + 9 if (x >= 2 and x <= 7) else -69,discontinuities=[2,7],color=BLUE)

        supply = axes.get_graph(lambda x: 2*x if (x >= 0 and x <= 5) else -79,discontinuities=[0,5],color=GREEN)
        shortedad = axes.get_graph(lambda x: 45/11 if (x>=30/11 and x<=52/11) else -69, discontinuities=[30/11,52/11], color=WHITE)

        shortage = Brace(Line(axes.c2p(30/11,45/11),axes.c2p(52/11,45/11)))

        label = shortage.get_text("Shortage")

        suplay = axes.get_graph_label(supply, Text("Supply").scale(0.5))
        dimand = axes.get_graph_label(demand, Text("Demand").scale(0.5))
        self.play(
            ShowCreation(demand),
            FadeIn(dimand,RIGHT)
        )
        #self.wait(1)
        self.play(
            ShowCreation(supply),
            FadeIn(suplay,RIGHT)
        )
        dot = Dot(color=RED).move_to(axes.i2gp(63/19, supply))
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        eq = axes.get_graph(lambda x: 2*x if x == 63/19 else -69, discontinuities=[63/19,63/19], color=WHITE)
        eqlab = axes.get_graph_label(eq, Text("equilibrium price").scale(0.2),x=63/19)
        ek = axes.get_graph(lambda x: 2*x if x == 45/19 else -69, discontinuities=[45/19,45/19], color=WHITE)
        eklab = axes.get_graph_label(ek, Text("equilibrium price").scale(0.2),x=45/19)

        self.play(FadeIn(dot, scale=0.5), ShowCreation(h_line),ShowCreation(v_line),FadeIn(eqlab,LEFT))
        #self.wait(1)
        self.play(
            FadeOut(eqlab,RIGHT),
            demand.animate.shift(LEFT*1),
            dimand.animate.shift(LEFT)
        )
        self.play(dot.animate.move_to(axes.i2gp(45/19, supply)))
        self.play(FadeIn(eklab,LEFT))
        self.play(
            FadeOut(demand, LEFT),
            FadeOut(dimand, LEFT),
            FadeOut(eklab,RIGHT)
        )

        MC = axes.get_graph(lambda x: 2*x if (x >= 0 and x <= 5) else -69, discontinuities=[0,5], color=GREEN)
        AVC = axes.get_graph(avc, discontinuities=[0,9], color=BLUE)
        ATC = axes.get_graph(atc, discontinuities=[1,9], color=MAROON)

        mc_label = axes.get_graph_label(MC, "MC")
        avc_label = axes.get_graph_label(AVC,"AVC", x = 8)
        atc_label = axes.get_graph_label(ATC,"ATC")

        self.bring_to_front(dot)
        self.bring_to_back(MC)
        self.play(
            ReplacementTransform(supply,MC),
            FadeTransform(suplay, mc_label),
        )
        self.bring_to_back(MC)
        self.bring_to_back(ATC)
        self.play(
            ShowCreation(ATC),
            FadeIn(atc_label,LEFT)
        )
        
        '''
        dot = Dot(color=RED).move_to(axes.i2gp(1.5, MC))
        dok = Dot(color=RED).move_to(axes.i2gp(2.25, MC))
        '''
        off = axes.get_graph(lambda x: 2*x if x == 1.5 else -69, discontinuities=[1.5,1.5], color=WHITE)
        kita = axes.get_graph(lambda x: 2*x if x == 2.25 else -69, discontinuities=[2.25,2.25], color=WHITE)
        kita_label = axes.get_graph_label(kita, Text("zero-profit point").scale(0.2),x=2.25)
        off_label = axes.get_graph_label(off,Text("shutdown point").scale(0.2),x=1.5)

        profit = axes.get_graph_label(MC, Text("profit zone").scale(0.1), x = 3)
        shutdown = axes.get_graph_label(MC, Text("shutdown zone").scale(0.1), x = 1)
        self.play(
            dot.animate.move_to(axes.i2gp(2.25, MC))
            )
        self.play(
            FadeIn(kita_label,RIGHT),
            )
        self.play(
            FadeIn(profit,LEFT),
            )
        self.play(FadeOut(kita_label,LEFT))
        self.bring_to_back(AVC)
        self.play(
            ShowCreation(AVC),
            FadeIn(avc_label,LEFT),
        )
        self.play(dot.animate.move_to(axes.i2gp(1.5, MC)))
        self.play(
            FadeIn(off_label,RIGHT),
            )
        self.play(
            FadeIn(shutdown,RIGHT),
            )
        self.wait(2)

        self.play(
            FadeOut(AVC, LEFT),
            FadeOut(avc_label,LEFT),
            FadeOut(off_label,LEFT)
        )
        #kita_label = axes.get_graph_label(kita,Text("shutdown point").scale(0.2),x=1.5)
        LATC = axes.get_graph(latc,discontinuities=[0,12],color=MAROON)
        atc_label = axes.get_graph_label(LATC,"ATC")
        tite_label = axes.get_graph_label(kita, Text("zero-profit point \n\n and shutdown point").scale(0.2),x=2.25)
        self.play(
            ReplacementTransform(ATC, LATC)
        )
        self.bring_to_back(LATC)
        self.play(dot.animate.move_to(axes.i2gp(2.25, MC)))
        self.play(FadeIn(tite_label,RIGHT))


