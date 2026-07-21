# (c) Copyright 2026 by Coinkite Inc. This file is covered by license found in COPYING-CC.
#

def test_renderer_reexports_public_core_surface(sim_eval):
    renderer = "__import__('bitsquiggle32_renderer_framebuffer')"
    core = "__import__('bitsquiggle32')"
    expression = (
        "all(getattr(%s, name) is getattr(%s, name) for name in %s.__all__)"
        " and 'render_raster' in %s.__all__"
    ) % (renderer, core, core, renderer)
    assert sim_eval(expression) == "True"