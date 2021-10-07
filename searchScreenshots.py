#!/usr/bin/python3

# by Antonio "Visi@n" Broi antonio@tsurugi-linux.org
# https://tsurugi-linux.org
# 20211007

# 
# LICENSE M.I.T.  https://opensource.org/licenses/MIT
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
#OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
#OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Example: searchScreenshots.py -i images/ -o matchImages/


from PIL import Image
import time
from datetime import datetime
from os import listdir
import argparse
import os
import cv2
import sys
import re
import hashlib
import psutil


global destinationFileDirectory
global filename
global filenamecsv
global image_file

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputDirectory", required=True,
	help = "the input images directory to search for width height and pixel")
ap.add_argument("-o", "--outputDirectory", default="matchImages" ,
	help = "the output images directory where to write the result")
ap.add_argument("-w", "--width", default=720,
	help = "the images width")
ap.add_argument("-e", "--height", default=1440,
	help = "the images height")
ap.add_argument("-p", "--pixel", default=400,
	help = "the images pixel")
	
args = vars(ap.parse_args())

def setup(OUTDIR):
	print("Create output folders and files")
	# Only use output directory - check if exists or
	# Create random file name
	if not os.path.exists(OUTDIR):
		os.makedirs(OUTDIR)
		filenamecs = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+".csv"
		filenamecsv = open(OUTDIR+"/"+filenamecs, "w")
		filenamecsv.write("filename"+","+"width"+","+"height"+","+"MD5"+","+"SHA1"+"\n")
	else:
		print("The output directory folder exists. Please try another name.")
		#destinationFileDirectory = str((datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))

def processImage(image, filenamecsv):
		#img.show()
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg) + " heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
""" 		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill() """

# the directory to searching images
# Add ecursion
images = os.listdir(args["inputDirectory"]) 

# Image.Image.'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getexif', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection'
# loop for scanning images
for image in images:
	img = Image.open((args["inputDirectory"]) + image) # Image properties
	image_file = open((args["inputDirectory"]) + image).read() # Image contents data
	widthImg = Image.Image.width.__get__(img)
	heightImg = Image.Image.height.__get__(img)
	print("Found image width: " + widthImg + " height: " + heightImg)
	#print(widthImg)
	#print(heightImg)

	if (widthImg == int(args["width"]) and heightImg == int(args["height"])): #like: 
        processImage(image, filenamecsv)
	if (widthImg == 720 and heightImg == 1440):#like: moto g(6)play P4 XT1922-1 #
		img.show()
	
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")

		print("   ")
		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
				
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
				
	elif (widthImg == 2048 and heightImg == 2732):# like: Ipad Pro
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		#filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")
		
		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()

	else:
		print("Not Screen Shot present in this directory")	
		
#filenamecsv.close()
#image_file.close()
exit
