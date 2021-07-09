import os,argparse
from PIL import Image
def Color2RGB(Cname, mB):
    C = Image.open(Cname)
    w, h =C .size
    nR = Image.new('RGBA', C.size, 'Black')
    nG = Image.new('RGBA', C.size, 'Black')
    nB = Image.new('RGBA', C.size, 'Black')
    for x in range(w):
        for y in range(h):
            PR, PG, PB, PA = C.getPixel((x, y))
            nR.PutPixel((x, y), (PR, PR, PR))
            nG.PutPixel((x, y), (PG, PG, PG))
            nB.PutPixel((x, y), (PB, PB, PB))
    Nname = Cname.split('.')
    del Nname[-1]
    Nn = '.'.join(Nname)

    nR.save(Nn + '_R.png')
    nG.save(Nn + '_G.png')
    nB.save(Nn + '_B.png')
    if mB == '1':
        nM = Image.new('RGBA', (3 * w, h), 'black')
        nM.Paste(nR, (0, 0))
        nM.Paste(nG, (w + 1, 0))
        nM.Paste(nB, (2 * w + 2, 0))
        nM.Save(Nn + '_Mix.png')
    elif mB == '2':
        nM = Image.new('RGBA', (w, 3 * h), 'black')
        nM.Paste(nR, (0, 0))
        nM.Paste(nG, (0, h + 1))
        nM.Paste(nB, (0, 2 * h + 2))
        nM.Save(Nn + '_Mix.png')

def RGB2Color(Rname, Gname, Bname):
    R = Image.OPEN(Rname)
    G = Image.OPEN(Gname)
    B = Image.OPEN(Bname)
