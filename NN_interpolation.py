from PIL import Image
import numpy as np

factor = 2

original_img = Image.open("book.jpg")
np_original_img = np.asarray(original_img)
original_h, original_w, c = np_original_img.shape

new_w = original_w * factor
new_h = original_h * factor

np_new_img = np.zeros((new_h, new_w, c))

for i in range(new_h):
    for j in range(new_w):
        x = min(round(i/factor), original_h-1)
        y = min(round(j/factor), original_w-1)

        np_new_img[i, j, :] = np_original_img[x, y, :]


new_img = Image.fromarray(np_new_img.astype(np.uint8), mode="RGB")
new_img.save("edited by NN.png")
new_img.show()
