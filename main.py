# food-picture-01 entry: Python 3.13, standard library only.
# The picture is entry.png next to this file: a photorealistic
# close-up of a smash burger, glossy toasted brioche bun, melted
# cheddar dripping down the patty, a little steam, one dish filling
# the whole frame so it still reads at about 300 pixels across.
# This program copies that file byte for byte to entry.png inside
# MAKEFUN_OUTPUT_DIR (default /output), creating the folder first.
# The file is named entry.png and holds JPEG bytes, which the rules
# allow: the name stays entry.png either way, whatever format the
# bytes are. No network, no clock, no randomness, so two runs write
# byte-identical output.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
