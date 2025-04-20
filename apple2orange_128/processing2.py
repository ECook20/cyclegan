import os
from PIL import Image

for directory in ["./trainA", "./testA", "./trainB", "./testB"]:
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        im = Image.open(f)
        im = im.resize((128, 128))
        im.save(f)

