# BitSquiggles identity view

The `View Identity` menu displays the numeric master fingerprint with the
BitSquiggles canonical black-and-white exact raster.

The frozen `shared/bitsquiggle32.py` core and
`shared/bitsquiggle32_renderer_framebuffer.py` are source copies from the
BitSquiggles MicroPython port. COLDCARD imports the framebuffer entry point:

```python
from bitsquiggle32_renderer_framebuffer import (
    BLACK_AND_WHITE, PIXEL_WIDTH, pixels, render_raster,
)
```

COLDCARD stores its fingerprint integer in little-endian order, while
`xfp2str()` displays the fingerprint's four bytes in standard big-endian order.
The integration byte-swaps that internal integer before calling
`pixels(bits, BLACK_AND_WHITE)`, so the numeric value encoded by BitSquiggles
matches the eight displayed hexadecimal digits. For example, internal
`0x2ae94002` is displayed as `0240E92A` and rendered as canonical input
`0x0240e92a`.

`render_raster(dis.dis, grid, ...)` only paints the canonical grid using the
SSD1306 framebuffer's `fill_rect` interface. The OLED color mapper converts the
canonical `#000000` and `#ffffff` colors into the framebuffer's `0` and `1`
values.

The optional LVGL renderer is not frozen or imported on COLDCARD.
