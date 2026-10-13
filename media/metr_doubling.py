"""Horizonte de tareas de agentes de IA: días de duplicación según METR, Time Horizon 1.1.

Cifras (Tabla 1 del paper, fuente: METR, 29 de enero de 2026): 196.5, 130.8 y 88.6 días.
No se proyecta ni se interpola nada: solo se muestran esas tres cifras y la advertencia de METR.
"""
import manimgx as m

NIGHT = "#090D14"
SURFACE = "#101925"
LINE = "#26384C"
MUTED = "#A5B6C9"
SAPPHIRE = "#1557A6"
ON_DARK = "#64A3FF"
WHITE = "#FFFFFF"
FONT = "Inter"
FONT_DIR = "/Users/ricardomartinez/Documents/ChatGPT/Nullghost/NullGhost-Organizado/01-Marca/fonts"

LOGO = "/Users/ricardomartinez/Documents/ChatGPT/Nullghost/NullGhost-Organizado/01-Marca/logos/nullghost-horizontal-reverse.svg"

ROWS = [
    ("Serie completa", 196.5, LINE),
    ("Desde 2023", 130.8, SAPPHIRE),
    ("Desde 2024", 88.6, ON_DARK),
]
BAR_MAX = 6.6  # ancho de la barra de 196.5 días, en unidades de escena


def txt(s, size, color=WHITE, weight="NORMAL"):
    return m.Text(s, font=FONT, font_paths=[FONT_DIR], font_size=size, color=color, weight=weight)


class MetrDoubling(m.Scene):
    def construct(self) -> None:
        m.config.background_color = NIGHT
        self.camera.background_color = NIGHT

        title = txt("Horizonte de tareas de los agentes de IA", 44, WHITE, "BOLD")
        title.to_edge(m.UP, buff=0.7)
        sub = txt("Días que tarda en duplicarse (METR, Time Horizon 1.1)", 26, MUTED)
        sub.next_to(title, m.DOWN, buff=0.25)

        self.play(m.FadeIn(title, shift=0.2 * m.UP), run_time=0.9)
        self.play(m.FadeIn(sub), run_time=0.6)

        labels, bars, nums, trackers = [], [], [], []
        x_label = -5.9
        x_bar = -2.6
        for i, (name, val, color) in enumerate(ROWS):
            y = 1.45 - i * 1.05
            lab = txt(name, 28, MUTED)
            lab.move_to([x_label, y, 0], aligned_edge=m.LEFT)
            w = BAR_MAX * val / ROWS[0][1]
            bar = m.Rectangle(width=w, height=0.62, fill_color=color, fill_opacity=1, stroke_width=0)
            bar.move_to([x_bar, y, 0], aligned_edge=m.LEFT)
            tr = m.ValueTracker(0)
            num = m.always_redraw(
                lambda tr=tr, bar=bar: txt(f"{tr.get_value():.1f}", 34, WHITE).next_to(bar, m.RIGHT, buff=0.3)
            )
            labels.append(lab); bars.append(bar); nums.append(num); trackers.append(tr)

        for lab, bar, num, tr, (_, val, _) in zip(labels, bars, nums, trackers, ROWS):
            self.add(num)
            self.play(
                m.FadeIn(lab, shift=0.15 * m.RIGHT),
                m.GrowFromEdge(bar, m.LEFT),
                tr.animate.set_value(val),
                run_time=1.6,
                rate_func=m.smooth,
            )
            self.wait(0.35)

        hint = txt("Menos días: duplicación más rápida", 24, ON_DARK)
        hint.next_to(bars[-1], m.DOWN, buff=0.45).align_to(bars[-1], m.LEFT)
        self.play(m.FadeIn(hint, shift=0.15 * m.UP), run_time=0.7)
        self.wait(1.2)

        caveat = txt(
            "METR: los intervalos de confianza son muy amplios y la tendencia\n"
            "es sensible a la composición de tareas.",
            23, MUTED,
        )
        caveat.to_edge(m.DOWN, buff=1.05)
        self.play(m.FadeIn(caveat, shift=0.15 * m.UP), run_time=0.8)
        self.wait(2.6)

        src = txt("Fuente: METR, Time Horizon 1.1 (29 ene 2026)", 22, MUTED)
        src.to_edge(m.DOWN, buff=0.55)
        self.play(m.FadeIn(src), run_time=0.6)
        self.wait(1.2)

        everything = m.Group(*self.mobjects)
        self.play(m.FadeOut(everything), run_time=0.8)

        logo = m.SVGMobject(LOGO, height=0.9)
        tag = txt("De la IA actual a la superinteligencia · nullghost.io/research", 24, MUTED)
        end = m.VGroup(logo, tag).arrange(m.DOWN, buff=0.45)
        self.play(m.FadeIn(end, shift=0.1 * m.UP), run_time=0.9)
        self.wait(2.0)
