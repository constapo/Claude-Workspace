"""Manim scene (Code2Video-style, made free: Claude plans/codes/critiques, Manim renders).
Line 7.5-7.7: wall -> membrane -> adhesive -> tile cross-section, then water path when the membrane is missing.
DIAGRAM: only usable if the owner allows a diagram for this scene (CLAUDE.md video rule 2).

Render: ~/.venvs/manim/bin/manim -qh --format mp4 -o waterproof_layers.mp4 \
        --media_dir inonda-youtube-videos/production/v01/build/gfx waterproof_layers.py WaterproofLayers
"""
from manim import (BLUE_D, DOWN, GREY_B, GREY_D, LEFT, RIGHT, UP, WHITE, Arrow, Create, FadeIn,
                   FadeOut, Rectangle, Scene, Text, VGroup, Write, config)

config.background_color = "#1e2226"
FONT = "DejaVu Sans"
LAYERS = [  # (Greek label, colour, width)
    ("Τοίχος", "#8d8478", 2.6),
    ("Στεγανωτική μεμβράνη", "#5b7fa6", 0.35),
    ("Κόλλα πλακιδίων", "#c9c3b5", 0.3),
    ("Πλακάκι", "#e8e4dc", 0.45),
]


class WaterproofLayers(Scene):
    def construct(self):
        title = Text("Τι κρύβεται πίσω από το πλακάκι", font=FONT, font_size=40, color=WHITE).to_edge(UP)
        self.add(title)
        self.wait(0.3)

        x, blocks, labels = -4.6, VGroup(), VGroup()
        for name, colour, w in LAYERS:
            r = Rectangle(width=w, height=4.6, fill_color=colour, fill_opacity=1, stroke_width=0)
            r.move_to([x + w / 2, -0.4, 0])
            x += w
            blocks.add(r)
            lab = Text(name, font=FONT, font_size=24, color=WHITE)
            labels.add(lab)
        for i, (r, lab) in enumerate(zip(blocks, labels)):
            lab.move_to([0.6, 1.4 - i * 0.95, 0], aligned_edge=LEFT)
            arrow = Arrow(lab.get_left() + LEFT * 0.1, r.get_right() + LEFT * (r.width / 2), buff=0.05,
                          stroke_width=3, color=GREY_B, max_tip_length_to_length_ratio=0.08)
            self.play(FadeIn(r, shift=RIGHT * 0.3), FadeIn(lab), Create(arrow), run_time=0.8)
        self.wait(1.2)

        membrane, mem_label = blocks[1], labels[1]
        self.play(membrane.animate.set_fill(GREY_D, opacity=0.25), mem_label.animate.set_color(GREY_D), run_time=1.0)
        water = VGroup(*[Arrow([0.4, 1.6 - k * 1.1, 0], [-3.0, 1.2 - k * 1.1, 0], buff=0, color=BLUE_D,
                               stroke_width=6) for k in range(3)])
        down = Arrow([-3.2, -1.4, 0], [-3.2, -2.9, 0], buff=0, color=BLUE_D, stroke_width=6)
        self.play(*[Create(a) for a in water], run_time=1.4)
        self.play(Create(down), run_time=0.8)
        note = Text("Χωρίς μεμβράνη: το νερό μπαίνει στον τοίχο", font=FONT, font_size=30,
                    color="#ffcf6b").to_edge(DOWN)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(VGroup(water, down, note)), run_time=0.6)
