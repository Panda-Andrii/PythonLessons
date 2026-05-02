import cv2
from PIL import Image

image_patch = 'cat1.png'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_patch)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_patch)
glasses = Image.open('Sunglasses.png')
cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y + h/4)), glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("cat_with_glasses", cat_with_glasses)
    cv2.waitKey(0)