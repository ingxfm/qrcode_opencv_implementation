# Standard libraries

# 3rd-party libraries
import cv2
import matplotlib.pyplot as plt

# Local libraries
#####

# 1. Image read correctly - 6 points
imgPath = 'IDCard-fre.png'
img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. Created a QRCodeDetector object with correct variable name - 6 points
qrDecoder = cv2.QRCodeDetector()

# 3. Detect QR Code in the image - 6 points
opencvData, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)

# 4. Print decoded text - 6 points
if opencvData is not None:
    print("QR code detected: ", opencvData, ".")
else:
    print("QR code not detected.")

# 5. Final output image saved correctly - 6 points
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 0, 255)
n = bbox.shape[1]

for j in range(n):
    # cv2.line requires tuples by definition
    cv2.line(img, tuple(bbox[0][j]), tuple(bbox[0][(j + 1) % n]), color, 3)
    # a=(j+1) % n #this is a value for seeing what is going on with the indexes

plt.imshow(img)
plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

filename = "result.jpg"
cv2.imwrite(filename, img)

