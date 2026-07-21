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

`pixels(xfp, BLACK_AND_WHITE)` remains the canonical identity-to-raster
operation. `render_raster(dis.dis, grid, ...)` only paints that grid using the
SSD1306 framebuffer's `fill_rect` interface. The OLED color mapper converts
the canonical `#000000` and `#ffffff` colors into the framebuffer's `0` and
`1` values.

The optional LVGL renderer is not frozen or imported on COLDCARD.