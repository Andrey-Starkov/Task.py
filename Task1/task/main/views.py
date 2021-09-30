from django.shortcuts import render
from PIL import Image
# Create your views here.
from django.views.decorators.csrf import csrf_protect
import eel
import time


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)

#eel.init('web')

@csrf_protect
def index(request):
    contex = {}
    if request.method == 'POST':
        uploded_file= request.FILES['f']
        a = {}
        im = Image.open(uploded_file)
        pix = im.load()
        width, height = im.size
        for x in range(width):
            for y in range(height):
                if rgb_to_hex(pix[x, y][0], pix[x, y][1], pix[x, y][2]) not in a:
                    a[rgb_to_hex(pix[x, y][0], pix[x, y][1], pix[x, y][2])] = 1
                else:
                    a[rgb_to_hex(pix[x, y][0], pix[x, y][1], pix[x, y][2])] += 1
        if ('#000000' in a) and ('#ffffff' in a):
            if a['#000000'] > a['#ffffff']:
                contex['temp'] = 'Больше чёрного'
            else:
                contex['temp'] = 'Больше белого'
        elif ('#000000' not in a) and ('#ffffff' in a):
            contex['temp'] = 'Больше белого'
        elif ('#000000' in a) and ('#ffffff' not in a):
            contex['temp'] = 'Больше чёрного'
        else:
            contex['temp'] = 'Нету ни белого, ни чёрного'
        #showMessage()
    return render(request, 'main/index.html', contex)


#@eel.expose
#def showMessage():
#    return "Здарова, ёпта"


#eel.start('index.html')