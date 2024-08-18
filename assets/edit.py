from PIL import Image


for i in range(1,24):
    img=  Image.open(f'mummy{i}.png')
    mirrored=img.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored.save(f'rmummy{i}.png')