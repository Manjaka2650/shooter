import os
import shutil

for i in range(1,24):
    i+=1
    source=f'rmummy{i}.png'
    coping=f'rmummy{i+24}.png'
    shutil.copy(source,coping)