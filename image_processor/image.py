import sys
import os
from PIL import Image

#grab the first and second argument
jpg_folder=sys.argv[1]
png_folder=sys.argv[2]
#check if JPGimage folder exists, if not create it
if not os.path.exists(png_folder):
    os.makedirs(png_folder)
#loop through all images in JPGimage folder
for file_name in os.listdir(jpg_folder):
    current_image=Image.open(f'{jpg_folder}\\{file_name}')
    clean_name=os.path.splitext(file_name)[0]
    #convert jpg images to Png images
    # save the jpg in new folder
    current_image.save(f'{png_folder}\\{clean_name}.png','png',)
    print('all done')
