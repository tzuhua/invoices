from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
BG = (48, 84, 150, 255)
FG = (255, 255, 255, 255)
SIZES = [192, 512]


def find_font(size):
    candidates = [
        r"C:\Windows\Fonts\msjh.ttc",
        r"C:\Windows\Fonts\msjhbd.ttc",
        r"C:\Windows\Fonts\mingliu.ttc",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


for size in SIZES:
    img = Image.new("RGBA", (size, size), BG)
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.18)
    radius = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=radius, outline=FG, width=max(2, size // 64))
    line_y = pad + (size - 2 * pad) // 3
    for i in range(3):
        y = line_y + i * (size // 12)
        draw.line([pad + size // 12, y, size - pad - size // 12, y], fill=FG, width=max(2, size // 80))

    text = "發票"
    font = find_font(int(size * 0.22))
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (size - tw) // 2 - bbox[0]
    ty = int(size * 0.06)
    draw.text((tx, ty), text, fill=FG, font=font)

    out = os.path.join(OUT_DIR, f"icon-{size}.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")
