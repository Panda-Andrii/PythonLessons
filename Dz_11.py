import cv2
from PIL import Image

image_patch = 'cat2.jpg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image = cv2.imread(image_patch)
cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_patch)
glasses = Image.open('glasses2.png')
hat = Image.open('hat1.png')

cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')
hat = hat.convert('RGBA')

for (x, y, w, h) in cat_face:
    glasses_resized = glasses.resize((w, int(h / 3)))
    cat.paste(glasses_resized, (x, int(y + h / 4)), glasses_resized)

    hat_resized = hat.resize((w, int(h / 2)))
    cat.paste(hat_resized, (x, int(y - h / 4.5)), hat_resized)

cat.save("cat_with_accessories.png")

cat_with_accessories = cv2.imread("cat_with_accessories.png")
cv2.imshow("cat_with_accessories", cat_with_accessories)
cv2.waitKey(0)