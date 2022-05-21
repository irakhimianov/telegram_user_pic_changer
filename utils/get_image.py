from io import BytesIO
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw
from .get_weather_info import get_weather_info
from .get_current_time import get_current_time


def add_text(
        image: Image,
        xy: tuple[int],
        text: str,
        font: ImageFont,
        spacing=0,
        fill=(0, 0, 0),
        stroke_width=0,
        stroke_fill=(0, 0, 0)
) -> Image:

    draw = ImageDraw.Draw(image, "RGB")
    draw.text(xy=xy,
              text=text,
              font=font,
              align='center',
              spacing=spacing,
              fill=fill,
              stroke_width=stroke_width,
              stroke_fill=stroke_fill)
    return image


def text_align_center(image: Image, font: ImageFont, text: str, pos: str) -> float | tuple[float]:
    width, height = image.size
    if '\n' in text:
        text_width, text_height = font.getsize_multiline(text)
    else:
        text_width, text_height = font.getsize(text)
    if pos.lower() == 'h':
        return width // 2 - text_width // 2
    if pos.lower() == 'v':
        return height // 2 - text_height // 2
    if pos.lower() == 'hv':
        return (width // 2 - text_width // 2,
                height // 2 - text_height // 2)


def get_image() -> BytesIO:
    font_path = Path('utils', 'static', 'fonts', 'a_lcdnova_italic.ttf')
    image = Image.new(mode="RGB", size=(512, 512), color=(0, 0, 0))
    #time
    font = ImageFont.truetype(str(font_path), size=146)
    time = get_current_time()
    centered_xy = text_align_center(image=image, font=font, text=time, pos='hv')
    image = add_text(image=image, xy=centered_xy, text=time, font=font, fill=(9, 227, 67))
    #weather
    font = ImageFont.truetype(str(font_path), size=24)
    weather = get_weather_info()
    centered_x = text_align_center(image=image, font=font, text=weather, pos='h')
    image = add_text(image=image, xy=(centered_x, 350), text=weather, font=font, fill=(9, 227, 67))
    image_io = BytesIO()
    image_io.name = "image.jpeg"
    image.save(image_io, 'JPEG')
    image_io.seek(0)

    return image_io

