#  Challenge: 11. Create an image from code (png file) Hint: use Pillow

from PIL import Image, ImageDraw, ImageColor

img = Image.new('RGB', (1000, 1000), color=(0, 0, 0))

d = ImageDraw.Draw(img)

d.text((50, 50), "'Hi there' from DevOps expert (:  ", fill=(28, 167, 57))

img.save('pil_text.png')

img.show()

