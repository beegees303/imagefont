import random
from PIL import Image, ImageDraw, ImageFont

img = Image.open('james.jpg').convert("RGBA")
txt = Image.new('RGBA', img.size, (255,255,255,0))

text = "noexpect.tistory.com"
font = ImageFont.truetype("arial.ttf", 82)

d = ImageDraw.Draw(txt)

width, height = img.size 
textwidth, textheight = d.textsize(text, font)
x=width/2-textwidth/2
y=height/2-textheight/2

d.text((x,y), text, fill=(255,255,255,230), font=font)

watermarked = Image.alpha_composite(img, txt)
watermarked.save(r'cake_watermarked50.png')