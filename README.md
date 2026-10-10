# PixelForge 4.0 — the 2026 automation & restoration pass

![The v4 feature card](demo/25_v4_features.png)
![The new Actions panel](demo/26_actions_panel.png)

An open, cross-platform editor that aims at **the full Photoshop feature set plus the best of
Canva, PicMonkey and friends** — built on Python/PySide6 + numpy/cv2, with the Rust
[**PhotoCraft**](https://github.com/storytold/photocraft) engine (MIT/Apache-2.0) attached as a
high-fidelity verification core.

![Canva-style design](demo/21_canva_design.png)
![Live adjustments + Select Subject](demo/20_photo_adjustments.png)

**New in 2.1 — PhotoCraft's UI, as it is.** The complete chrome is a faithful port of
PhotoCraft's MIT design system: the exact Pro Medium tokens (sampled from Photoshop 2026),
the Lucide icon set, the Photoshop toolbox with group flyouts and overlapping color chips,
the frameless title bar with embedded menus, and **the entire 766-entry Photoshop menu tree** —
live where PixelForge implements a command, disabled elsewhere, exactly like PhotoCraft's model.

![PixelForge in AMOLED](demo/ui_amoled.png)

## Quick start

```sh
./scripts/setup_env.sh                     # deps (rerun after sandbox resets)
python3 app.py                             # launch (PhotoCraft-style chrome)
python3 app.py photo.psd                   # open a file
python3 main.py                            # same UI via the qt_boot launcher

# test suites (214 checks total)
python3 tests/test_pf.py                                       # 35 — engine + parity
LD_LIBRARY_PATH=runtime/lib python3 tests/test_v2.py           # 37 — engine v2/v3
LD_LIBRARY_PATH=runtime/lib python3 tests/test_v3.py           # 41 — 2026 features
LD_LIBRARY_PATH=runtime/lib QT_QPA_PLATFORM=offscreen \
    python3 tests/test_ui_interactions.py                      # 50 — real mouse/keyboard drives of every tool
LD_LIBRARY_PATH=runtime/lib QT_QPA_PLATFORM=offscreen \
    python3 tests/test_v4.py                                   # 51 — v4 automation pass
python3 tests/test_pf.py && python3 tests/test_v2.py   # 71 tests incl. engine parity
```

## Windows 10/11 app (.exe)

Ship it as a real Windows app: **`packaging\build_exe.bat`** builds a portable
`PixelForge.exe`, and `packaging\installer.iss` (Inno Setup) wraps it into
`PixelForge-4.0-Setup-win64.exe` — or let GitHub's machines build both for you
and download the artifacts (`.github/workflows/windows-build.yml`).
See **[packaging/README_BUILD.md](packaging/README_BUILD.md)**.

## The feature matrix

### The toolbox — all 52 Photoshop tools (2.2)

The complete Photoshop 2026 toolbox in PhotoCraft's exact grouping — 20 slots, corner-triangle
flyouts, every tool in its right place. **All 52 tools are live** — nothing disabled:

Move · Rect/Elliptical Marquee · Lasso, **Polygonal** & **Magnetic** (edge-snapping) ·
**Object Selection** (GrabCut), **Quick Selection**, Magic Wand · Crop · **Slice** (multi-PNG
export) & **Slice Select** · Eyedropper · **Ruler** (distance + angle) · **Notes** & **Counters** ·
**Spot Healing** (TELEA) + **Healing Brush** (high-frequency blend) + **Patch** +
**Content-Aware Move** + **Red Eye** · Brush + **Pencil** + **Mixer Brush** · Clone +
**Pattern Stamp** · **History Brush** (reveals the opened state) · Eraser + **Background
Eraser** (color-range) + **Magic Eraser** · Gradient + Bucket · **Blur / Sharpen / Smudge** ·
**Dodge / Burn / Sponge** · **Pen** (real vector paths) · Type + **Vertical Type** ·
**Path Selection** & **Direct Selection** · 6 shape tools (rect, ellipse, triangle, polygon,
line, custom) · Hand · **Rotate View** (drag-rotate the canvas) · Zoom.

Plus real **Channels** (view any channel in grayscale, Ctrl+click loads it as a selection) and
**Paths** panels (load path as selection, delete) in the Layers dock.

It also **works like Photoshop at the interaction level** (verified by 50 scripted mouse/keyboard
drives of every tool): single-letter tool keys (`V M L W C I B E G S O T U H Z P J N R Y A…`),
`[` / `]` resize the brush, `Ctrl+Z/Y` undo/redo, `Ctrl+[` / `Ctrl+]` layer order, Space or the
Hand tool or middle-drag to pan, Alt+wheel to zoom, Enter commits crops and polygon lassos,
right-click clears counters — and painting never lands on the wrong layer (type layers refuse
paint, as they should).

### Photoshop-grade editing
| Area | What you get |
|---|---|
| **Layers** | Pixel · groups (pass-through) · **live text** · **live shapes** · **live adjustment layers** (13 kinds), reorder/duplicate/merge/flatten/rasterize, blend/opacity per layer |
| **Blend modes** | All 22 (clean-room W3C/ISO math), verified against the Rust engine |
| **Layer masks** | Add/hide/from-selection, paint on masks, apply (bake), delete |
| **Layer styles** | Drop shadow · outer glow · stroke — live, composable, effect math respects the object alpha |
| **Text** | Font family picker (Inter/Roboto/Montserrat/DejaVu/JetBrains…), size, bold/italic, align, color, live re-edit by double-click, renders at compose time |
| **Shapes** | rect, roundrect, ellipse, triangle, star (n-points), arrow, speech bubble, heart, line — fill + stroke |
| **Selections** | Rect/ellipse marquee, lasso, **magic wand** (contiguous + global, tolerance), **color range**, **Select Subject** (GrabCut), feather, grow/contract, invert, stroke selection |
| **Paint** | Brush & eraser (size/hardness, live), bucket fill, gradient (linear/radial, FG→transparent or FG→BG), **clone stamp** (Alt-click source), **dodge & burn**, **blur & sharpen**, all honor selections |
| **Transform** | Free transform (scale/rotate with preview), flip layer/canvas, rotate 90/180, image size, canvas size, crop (Enter to commit), trim |
| **Filters** | 31 filters: blur family, sharpen/high-pass, noise, pixelate, distort (twirl/wave/pinch/spherize), stylize (oil paint, pencil sketch, emboss, find edges), render (lens flare, vignette, clouds), adjust — **Filter Gallery with live preview & intensity** |
| **Adjustments** | 13 live kinds: brightness/contrast, levels, curves, exposure, hue/sat, vibrance, color balance, invert, threshold, posterize, B&W, photo filter, gradient map — re-editable any time |

### Canva/PicMonkey-style creation
| Feature | How it works |
|---|---|
| **Templates** | File ▸ New from Template: 14 preset sizes (IG post/story, YT thumbnail/banner, poster A4, business card, Pinterest, wallpaper…) |
| **Collage maker** | 7 grid layouts, gaps/margins/background, crop-to-fill, builds a new document |
| **Magic resize** | Re-export the current design at any set of social sizes (or scale in place) |
| **One-click BG removal** | Create ▸ Remove Background (GrabCut, downscaled for speed) |
| **Brand kit** | Persisted color palette (right panel), one click to use as foreground |
| **Adjustments grid** | Click an icon, get a live adjustment layer, tune it in the dialog |
| **Auto-enhance** | Auto tone / auto contrast / auto enhance (Canva's one-click polish) |

### The engine bridge (why we can trust the pixels)
`pf/bridge.py` speaks JSON to the **PhotoCraft Rust engine** (`photocraft-cli serve`). The test
suites save our documents, have the Rust engine re-render them, and compare:
**11 parity tests, 97–100% of pixels within ±8/255** — including documents with text, shapes,
masks, effects and blend sandwiches. Our PSD writer embeds a *correct* merged-composite
section (a psd_tools builder gap we found and fixed), so every other tool sees the right preview.

## New in 4.0 — Actions, Batch & the PS 27.6 restoration set

Photoshop 27.6/27.11's headline features plus the Luminar/Photoroom market set — **all on-device**
(numpy/OpenCV, Haar cascades shipped with cv2 — no cloud, no credits):

| Feature | What it does |
|---|---|
| **Actions panel** (27.11 redesign) | new dock tab: ● Record captures every command you run, Stop saves it as a named set (JSON in `assets/actions/`), ▶ Play replays it — with **natural-language search** ("smooth skin", "product", "old photo") over set names, commands and keywords |
| **Batch…** (File ▸ Automate, now live) | folder → action set → folder: plays a set over every image in a directory, writes PNG/JPG, per-file error report |
| **Layer Cleanup** (27.6, File ▸ Scripts, now live) | removes empty pixel/group layers, renames the rest by what they look like (hue/tone heuristic) — exact undo restores names, order and pixels |
| **Rotate Object** (27.6) | spins/scales the active pixel layer about its own center, on canvas |
| **Product Shot** | GrabCut matte → clean studio backdrop (radial or solid) → soft AI contact shadow — the Photoroom pipeline in one click |
| **Relight** | directional scene light from a blurred-luma depth proxy (Luminar Relight AI-lite) |
| **Restore Old Photo** | dust/speckle removal → edge-preserving denoise → bounded levels stretch (structure-driven, capped slope — noise is never amplified), optional warm colorize |
| **Portrait Pro** | Haar face detection → elliptical skin smoothing + eye brighten; gentle global fallback when no face is found |
| **Find Distractions** (27.6) | median-diff speck detection, tiny ones auto-healed (TELEA), bigger ones reported |
| **Focus Stack** | Laplacian-weighted blend of focus brackets (Luminar focus stacking) |
| **Watermark** | contrast-aware text watermark on its own layer — corners or tiled, undoable |

Plus: 4 new Guided recipes ("restore old photo", "product shot", "portrait retouch",
"watermark my photo") and 4 preset action sets shipped in `assets/actions/`.
Reference: `demo/25_v4_features.png`, `demo/26_actions_panel.png`.

## AI Studio & the 2026 feature set (v3.0)

Everything the 2026 editors ship — implemented **on-device** with numpy/OpenCV. No cloud, no
credits, no uploads.

**AI Studio menu**
| Feature | What it does |
|---|---|
| **Remove Background** | GrabCut subject matte, one click |
| **Remove Object** | selection + content-aware inpaint |
| **Replace Sky** | column-scan sky detection, 6 generated skies (sunset/clear/golden/dusk/storm/teal), keeps cloud luminance structure, auto scene relight |
| **Harmonize Layer** | Lab mean/σ transfer — composites sit in the scene like PS 2026's Harmonize |
| **Smart Upscale 2×/4×** | Lanczos + high-frequency detail recovery |
| **Generative Expand** | canvas grows, TELEA inpaint invents the border |
| **Soft Portrait / Bokeh Background** | bilateral skin smoothing; GrabCut subject + iris blur |
| **Guided Actions…** | type what you want — "remove background", "blur background", "vintage", "upscale", "square"… — 29 offline recipes |

**Photoshop 27.x parity**
- **Clarity, Dehaze, Grain** — the three new 2026 adjustment layers (non-destructive, maskable)
- **Blur Gallery** — Iris Blur, Tilt-Shift, Field Blur (depth-masked, live in the catalog)
- **Color Lookup** — 9 preset packs (Teal & Orange, Warm Cinema, Noir, Fade, Vintage, Cyberpunk, Bleach, Vivid, Landscape Pop)
- **Smart Sharpen** (halo-guarded), **Dust & Scratches**, **Color Halftone**
- **Match Color** (Lab statistics from any image), **Photomerge** (cv2.Stitcher panorama), **Merge to HDR** (Mertens fusion)

**95 of the 766 catalog commands are now live** (was 93), plus the AI Studio menu and the Actions panel.
Reference: `demo/24_ai_features.png`.

## The PhotoCraft UI port

| Piece | File | What it is |
|---|---|---|
| Token themes | `ui/theme.py` | Exact ports of Pro Medium, Pro, Studio, Studio Light, Solarized Dark — plus **AMOLED (true black)**, our default: Photoshop's Pro grammar with #000 surfaces for OLED screens — colors/radii only from Tokens; global QSS + QPalette generated from them |
| Lucide icons | `ui/icons.py`, `assets/icons/` | The same SVGs PhotoCraft embeds (ISC licence kept), tinted at runtime and cached by (name, color, size) |
| Toolbox | `ui/toolbar.py` | 40px chrome column, 30px slots, icon = 52% of slot, corner-triangle flyout groups, Default/Switch color buttons over overlapping fg/bg chips, section hairlines |
| Title bar | `ui/titlebar.py` | Frameless window: brand mark, embedded menu bar, `name @ zoom (RGB/8)` doc title, min/max/close with the red hover, edge resizing |
| Menu tree | `ui/menu_catalog.py` + `ui/ids.py` | 766 entries regenerated straight from their `menu_catalog.rs`; `ids.py` maps our 89 commands onto it — unimplemented items render disabled, like PhotoCraft's early alphas |
| Theme picker | Window ▸ Theme | All six themes, live switch, persisted in QSettings |

Inter + JetBrains Mono ship in `assets/fonts/` (OFL). Attribution for everything:
[NOTICE](NOTICE). Run `PIXELFORGE_NATIVE_TITLE=1 python3 app.py` if you prefer the
OS-native title bar.

![Studio Light](demo/ui_studio_light.png)
![Solarized Dark](demo/ui_solarized_dark.png)

## Architecture (mirrors PhotoCraft's crate layering)

```
pixelforge/
  pf/            the engine (no Qt)
    geom.py color.py      L0  geometry, 22 blend modes
    doc.py                L1  document model (7 layer kinds, selection masks)
    adjust.py render.py   L2  adjustment math, text/shape rasterizers, layer effects
    filters.py            L2  31-filter library (numpy/cv2/scipy)
    compose.py            L3  compositor (the oracle)
    psdio.py              L4  layered PSD read/write + raster formats
    bridge.py             L4  PhotoCraft Rust-engine control channel
    engine.py             L5  100+ commands, undo/redo, action recording
    actions.py            L5  action sets (JSON), NL search, Batch runner
  ui/            the thin shell (PySide6)
    main_window.py canvas.py tools.py panels.py dialogs.py
  tests/         214 checks across 5 suites   scripts/  demos & setup
```

## Status / what's next
- **Done:** everything in the tables above; 214 checks green across 5 suites; pixel-identical PSD save/reopen;
  Rust-engine parity ≥97%.
- **Next:** smart objects + smart filters, pen/vector paths, layer comps, Warp, CMYK/16-bit
  (no-u8-only-path rule), GPU-accelerated canvas, plugin sandbox, snap/align guides,
  keyboard-complete PS shortcuts, per-frame performance profiler.

## License
Our code: MIT. The UI design system, icons and fonts come from PhotoCraft (MIT), Lucide (ISC)
and the OFL fonts — see [NOTICE](NOTICE). The PhotoCraft engine binary stays under its own
licences (MIT OR Apache-2.0).
Blend math and effects are clean-room from public specs (W3C Compositing & Blending, ISO 32000).
