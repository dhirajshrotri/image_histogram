import cv2
import numpy as np
import matplotlib.pyplot as plt	
import math

# img = cv2.imread("C:\\Users\\Nitesh\\Pictures\\FoodUnited.PNG", 0)
# img = cv2.imread("C:\\Users\\Nitesh\\Desktop\\histogram_test.bmp", 0)
img = cv2.imread("LenaDark.png", 0)

hist_data = [0] * 256; # Histogram Data
hist_eq = [0] * 256	# Equalized Histogram Data
cdf = [0]*256 # CDF
px = [0]*256 # PDF
size = img.size
img_eq = np.zeros(shape=(img.shape[0], img.shape[1]), dtype="uint8")

# Calculate Histogram data of image
for i in range(0, img.shape[0]) :
	for j in range(0, img.shape[1]) :
		pixel_val = img[i][j]
		hist_data[pixel_val] = hist_data[pixel_val] + 1
	
# Calculate PDF, CDF and Normalized CDF
for i in range(0, 256) :
	px[i] = float(hist_data[i])/float(size) # Calculate PDF
	for j in range(0, i) :
		cdf[i] = cdf[i] + px[j] # Calculate CDF
	cdf[i] = math.floor(cdf[i]*255) # Calculate Normalized CDF

# Calculate Equalized Histogram
for i in range(0, 256) :
	int_cdf = int(cdf[i])
	hist_eq[int_cdf] = hist_eq[int_cdf] + hist_data[i]

# Generate Equalized Image
for i in range(0, img.shape[0]) :
	for j in range(0, img.shape[1]) :
		img_eq[i][j] = int(cdf[img[i][j]]) # Maps Old Image to New Image via CDF
		
# Uncomment if necessary :-

# print "Histogram Data: "
# print hist_data
# print "PDF: "
# print px
# print "CDF: "
# print cdf
# print "Equalized Histogram Data: "
# print hist_eq

cv2.imshow("Image", img)
cv2.imshow("Equalized Image", img_eq)

plt.figure(1)
plt.subplot(211)
plt.title("Histogram")
plt.plot(hist_data)
plt.subplot(212)
plt.title("Equalized Histogram")
plt.plot(hist_eq, color="g")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()