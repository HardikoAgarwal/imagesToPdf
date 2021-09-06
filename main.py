# script to convert all images (stored in a folder) in a single pdf file

from PIL import Image
import os


data = os.listdir('images')
print("Images found in the folder :")
for image in data:
	print(image)
print("----------------------------")

print("Adding images to Queue")

allImages =[]

for image in data:
	im = Image.open(f'images/{image}').convert('RGB')
	allImages.append(im)

print("Converting to PDF")

firstImage = allImages[0]
allImages.pop(0)

try:
	firstImage.save('myPdf.pdf', save_all=True, append_images=allImages)
	print("Completed!")

except Exception as err:
	print("Following Error occured :\n",err)
	print("Conversion Failed")

