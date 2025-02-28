from caro import caro
from napbanco import naphinhco
import random
import numpy
cr = caro(20, 20)

print(numpy.array(cr.diagram))

xo = cr.xo

def maydi():
    L = cr.lay_L_nuoc_di()
    print("Những nước đi có sự ảnh hưởng:", L)
    x, y = random.choice(L)
    cr.botmove(x, y)

naphinhco(cr)

while cr.chay():
    if xo != cr.xo:
       maydi()
       xo = cr.xo