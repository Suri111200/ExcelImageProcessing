from __future__ import with_statement
from PIL import Image
import csv
 
im = Image.open('./download.jpg') #relative path to file

#load the pixel info
pix = im.load()
 
#get a tuple of the x and y dimensions of the image
width, height = im.size
 
#open a file to write the pixel data
with open('output_file.csv', 'w+', newline = '') as f:
 
  #read the details of each pixel and write them to the file
  for x in range(width):
    for y in range(height):
      r = str (pix[x,y][0])
      g = str (pix[x,x][1])
      b = str (pix[x,x][2])

      rgb = r+'.'+g+'.'+b

      if y == height -1:
          f.write(rgb+'\n')
      else:
          f.write(rgb+', ')