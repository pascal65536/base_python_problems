import os
import random
import datetime
import requests
import textwrap
from cairosvg import svg2png
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont


def get_medium(a_big, a_small):
    return (a_big - a_small) // 2


if __name__ == "__main__":
    print("3" * 80)
    filename = "1"
    folder = "data"
    if not os.path.exists(folder):
        os.makedirs(folder)

    pic_width = 800
    pic_height = 800
    black_w = 734
    black_h = 424
    black_row_w = 734
    black_row_h = 34
    delta = 3  # Зазор для круглого квадрата
    radius = 0  # Радиус скругления
    opacity = 255
    R = 251
    G = 195
    B = 60
    font_color = (R, G, B)

    # Создадим фон
    yellow_im = Image.new(
        "RGB", (pic_width, pic_height), color=R + (G * 256) + (B * 256 * 256)
    )
    black_im = Image.new("RGB", (black_w, black_h), color=0)

    black_row = Image.new("RGB", (black_row_w, black_row_h), color=0)

    yellow_im.paste(
        black_im, (get_medium(pic_width, black_w), get_medium(pic_height, black_h))
    )

    yellow_im.paste(
        black_row,
        (
            get_medium(pic_width, black_w),
            get_medium(pic_height, black_h) - black_row_h * 2,
        ),
    )
    yellow_im.paste(
        black_row,
        (
            get_medium(pic_width, black_w),
            get_medium(pic_height, black_h) + black_h + black_row_h,
        ),
    )

    text = "Не только сила, острый глаз и меткая рука решают успех дела; лишь соединившись с умом и мудростью, качества эти помогут человеку стать великим охотником"

    unicode_text = "\n".join(textwrap.wrap(text, width=45))
    draw = ImageDraw.Draw(yellow_im)
    unicode_font = ImageFont.truetype(os.path.join("fonts", "GAZRUBPL.TTF"), size=45)

    new_box = draw.textbbox(
        (0, 0), unicode_text, font=unicode_font, align="center", spacing=2
    )
    text_width = new_box[2] - new_box[0]
    text_height = new_box[3] - new_box[1]
    text_top = get_medium(pic_height, text_height) - 50
    text_left = get_medium(pic_width, text_width)

    draw.text((text_left, text_top), unicode_text, font=unicode_font, fill=font_color)

    output_path = os.path.join(folder, f"{filename}.png")
    yellow_im.save(output_path, format="PNG", dpi=[72, 72])
