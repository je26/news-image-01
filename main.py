"""news-image-01 entry: copy the broadsheet image beside this file to
/output/entry.png. The image sums up Friday 13 November 2026's world news
(FAA nationwide ground stop, Senate summons ex-NVIDIA CEO, Hormuz tankers,
Ukraine talks, Taiwan drills, Microsoft outage, Kane's record cap, and more).
Stdlib only; MAKEFUN_OUTPUT_DIR stands in for /output outside the grader."""

import os
import shutil
import struct

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)

# Fail loudly rather than ship a bad file: the gate takes a whole PNG of at
# most 1 MiB and 1024x1024. Check the copy's size and IHDR dimensions.
size = os.path.getsize(OUT)
assert size <= 1048576, f"entry.png too large: {size} bytes"
with open(OUT, "rb") as f:
    header = f.read(24)
assert header[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
width, height = struct.unpack(">II", header[16:24])
assert width <= 1024 and height <= 1024, f"entry.png too big: {width}x{height}"
