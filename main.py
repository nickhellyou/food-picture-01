# food-picture-01 entry (Python 3.13, standard library only).
# The picture is the entry.png beside this file: a photorealistic
# close-up of a smash burger, glossy brioche bun, melted cheddar
# dripping over the patty, steam rising, one dish filling the frame
# so it still reads at ~300 pixels across. The program copies it
# byte for byte to /output/entry.png (MAKEFUN_OUTPUT_DIR outside
# the grader's container). The file is named entry.png and holds
# JPEG bytes, which the rules allow ("the name stays entry.png
# either way"). No network, no nondeterminism, no clock:
# two runs write identical bytes.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
