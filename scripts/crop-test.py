import cv2
from PIL import Image

# Load with OpenCV instead of PIL for easier cropping
img = cv2.imread(r"C:\Users\home\Desktop\New folder\CSD- Images\2401-2B.jpg")

# Draw a rectangle (start with estimated coordinates — adjust as needed)
# Try cropping the top-right quadrant
h, w, _ = img.shape
x1, y1 = int(w * 0.759), int(h * 0.803)
x2, y2 = int(w * 0.98), int(h * 0.98)

# Draw the rectangle
img_box = img.copy()
cv2.rectangle(img_box, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Show it using PIL
Image.fromarray(cv2.cvtColor(img_box, cv2.COLOR_BGR2RGB)).show()
