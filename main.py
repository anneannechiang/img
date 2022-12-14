# convert image to black and white
# separate files for original and result

from PIL import Image
import os

for file in os.listdir('original'):
    if file.endswith('.png'):
        image_file = Image.open(os.path.join('original',file))
        image_file = image_file.convert('L') 
        image_file.save(os.path.join('result', file[:-4] + '_grey.png'))