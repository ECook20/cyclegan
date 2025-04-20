import os
from PIL import Image

for directory in ["./trainA", "./testA", "./trainB", "./testB"]:
    i = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        new_f = directory + "/" + str(i) + ".jpg"

        i += 1
        os.rename(f, new_f)
