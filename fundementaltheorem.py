from types import BuiltinFunctionType
from manim import *

class FirstScene(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(x_range = [-2, 2], y_range = [-2, 2], z_range = [-2, 2])
        parabola = ax.get_parametric_curve(
            lambda t: np.array([t, t, t**2]),
            t_range = [0, 2],
            stroke_color = BLUE,
            stroke_opacity = 1
        )
        labelz = ax.get_z_axis_label(Tex("z"))
        labelx = ax.get_x_axis_label("x")
        labely = ax.get_y_axis_label("y")
        #point1 = parabola.get_point_from_function(1)
        sphere1 = Sphere(center = ax.c2p(0.5, 0.5, 0.25), radius = 0.05)
        sphere2 = Sphere(center = ax.c2p(1, 1, 1), radius = 0.05)
        text1 = MathTex("A").next_to(sphere1, DR, buff = 0.01)
        text2 = MathTex("B").next_to(sphere2, DR)
        caption1 = MathTex("F(b)-F(a)")
        caption1.to_edge(UL)
        caption2 = MathTex("\Delta{F}\\approx{\\frac{\partial{F}}{\partial{x}}\Delta{x}}")
        caption2.to_edge(UL)
        vector1 = Line(start = sphere1.get_center(),end=[0.75, 1, 1]).add_tip()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(ax, labelz, labely, labelx)
        self.wait()
        self.play(Create(parabola))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(caption1)
        self.add(sphere1, sphere2)
        self.add_fixed_in_frame_mobjects(text1, text2)
        self.play(Create(vector1))
        self.wait()
        sphere3 = Sphere(center = ax.c2p(1, 0.5, 0.25), radius = 0.05)
        sphere4 = Sphere(center = ax.c2p(1, 1, 0.25), radius = 0.05)
        self.play(Create(sphere3))
        self.play(Create(sphere4))
        vector2 = DashedLine(start = sphere1.get_center(),end=sphere3.get_center())
        self.play(Create(vector2))
        vector3 = DashedLine(start = sphere3.get_center(),end=sphere4.get_center())
        self.play(Create(vector3))
        vector4 = DashedLine(start = sphere4.get_center(),end=sphere2.get_center())
        self.play(Create(vector4))
        self.remove(caption1)
        self.wait()
        self.add_fixed_in_frame_mobjects(caption2)
        self.wait()
        
class SecondScene(Scene):
    def construct(self):
        tex = MathTex("\int_{A}^{B}\\nabla{F}\cdot\,{d\\vec{r}} = F(B)-F(A)")
        self.play(Write(tex))

class SixthScene(Scene):
    def construct(self):
        text = MathTex("\int_{A}^{B}\\nabla{f}\cdot{\,{d\\vec{r}}} = \int_{t=a}^{t=b}\\nabla{f(r(t))}\cdot{r'(t)}dt \\\=\int_{a}^{b}\\frac{d}{dt}f(r(t))dt  \\\= f(r(b))-f(r(a))  \\\= f(B)-f(A)")
        #\int_{A}^{B}\\nabla{f}\cdot{\,{d\\vec{r}} = \int_{t=a}^{t=b}\\nabla{f(r(t))}\cdot{r'(t)}dt = \\\\int_{a}^{b}\\frac{d}{dt}f(r(t))dt = \\\ f(r(b))-f(r(a)) = \\\ f(B)-f(A)
        self.play(Write(text))
        self.wait()
        
class ThirdScene(Scene):
    def construct(self):
        text = MathTex("F(1,2,3)=7\\\F(3,6,1)=9")
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))
        self.wait()

class FourthScene(Scene):
    def construct(self):
        text = MathTex("\\nabla{F}=\\begin{pmatrix}{\\partial F}/{\\partial x}\\\{\\partial F}/{\\partial y}\\\{\\partial F}/{\\partial z}\\end{pmatrix}")
        self.play(Write(text))
        self.wait(12)
        self.play(Unwrite(text))
class FifthScene(Scene):
    def construct(self):
        text = MathTex("\int_{A}^{B}\\nabla{F}\cdot\,{d\\vec{r}} = F(B)-F(A)\\\{\int_{A}^{B}f'(x)dx = f(B)-f(A)}")
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))
        self.wait()
class SeventhScene(Scene):
    def construct(self):
        text = MathTex("\Delta{F}\\approx\sum\\nabla{F}\cdot\\vec{\Delta{r}}\\\\\Delta{F}=\int\\nabla{F}\cdot{d\\vec{r}}")
        #\Delta{F}\\approx\sum\\nabla{F}\cdot\\vec{\Delta{r}\\\}
        self.play(Write(text))
class EighthScene(Scene):
    def construct(self):
        text1 = MathTex("\Delta{F}_{\\text{along first step}}\\approx\\frac{\partial{F}}{\partial{x}}\Delta{x}").to_edge(UP, buff = 1.5)
        text2 = MathTex("\Delta{F}_{\\text{along second step}}\\approx\\frac{\partial{F}}{\partial{y}}\Delta{y}").next_to(text1, DOWN)
        text3 = MathTex("\Delta{F}_{\\text{along third step}}\\approx\\frac{\partial{F}}{\partial{z}}\Delta{z}").next_to(text2, DOWN)
        text4 = MathTex("\Delta{F}_{\\text{total}}\\approx\\frac{\partial{F}}{\partial{x}}\Delta{x}+\\frac{\partial{F}}{\partial{y}}\Delta{y}+\\frac{\partial{F}}{\partial{z}}\Delta{z} = \\begin{pmatrix}{\partial F}/{\partial x}\\\{\partial F}/{\partial y}\\\{\partial F}/{\partial z}\end{pmatrix}\cdot\\begin{pmatrix}\Delta{x}\\\{\Delta{y}}\\\{\Delta{z}}\end{pmatrix}").next_to(text3, DOWN)
        self.play(Write(text1))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.wait()
        self.play(Write(text4))
        
        
        
