#Captcha Generator

from PIL import Image, ImageDraw, ImageFont
import random

def getCaptcha(n = 5):
    small_case = [chr(x) for x in range(97,123)]
    digits= [str(x) for x in range(10)]
    upper_case = [chr(x) for x in range(65,91)]

    all = [small_case, digits, upper_case]

    captcha = ''
    for x in range(n):
        captcha = captcha + random.choice(all[random.randint(0,len(all)-1)])
    return captcha

def makeCaptcha(bg_file, captca_file):
    #load the captcha background
    canvas = Image.open(fp=bg_file)
    #size (w,h): canvas.size

    #to draw on a canvas, an ImageDraw object is required, get it.
    pen = ImageDraw.Draw(canvas)

    #define some attributes
    fg_color = 136,0,21 #r,g,b
    fontType = "Resource/"+ "Font"+str(random.randrange(1,6))+ ".ttf"
    fnt = ImageFont.truetype(font = fontType, size=40)

    #write on canvas
    text = getCaptcha()
    print(text)
    reqd_size = pen.textsize(text=text, font=fnt)
    pen.text(xy=((canvas.size[0]-reqd_size[0])/2,(canvas.size[1]- reqd_size[1])/2), text=text, font=fnt, fill=fg_color)

    #save the canvas
    canvas.save(captca_file)

makeCaptcha(bg_file = 'Resource/CapchaBackground.jpeg', captca_file= 'captcha_new.png')
