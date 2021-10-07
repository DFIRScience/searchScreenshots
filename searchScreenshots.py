#!/usr/bin/python3

# by Antonio "Visi@n" Broi antonio@tsurugi-linux.org
# https://tsurugi-linux.org
# 20191201

# 
# LICENSE M.I.T.  https://opensource.org/licenses/MIT
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
#OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
#OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Example: searchScreenshots.py -i images/ -o matchInages/


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

destinationFileDirectory = str((datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))

if not os.path.exists(destinationFileDirectory):
	os.makedirs(destinationFileDirectory)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputDirectory", required=True,
	help = "the input images directory to search for width height and pixel")
ap.add_argument("-o", "--outputDirectory", default="matchInages" ,
	help = "the output images directory where to write the result")
ap.add_argument("-w", "--width", default=720,
	help = "the images width")
ap.add_argument("-e", "--height", default=1440,
	help = "the images height")
ap.add_argument("-p", "--pixel", default=400,
	help = "the images pixel")
	
args = vars(ap.parse_args())

if not os.path.exists(args["outputDirectory"]):
	os.makedirs(args["outputDirectory"])

global filename
global filenamecsv
global image_file

filenamecs = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+".csv"
filenamecsv = open(destinationFileDirectory+"/"+filenamecs, "w")

filenamecsv.write("filename"+","+"width"+","+"height"+","+"MD5"+","+"SHA1"+"\n")

# the directory to searching images
images = os.listdir(args["inputDirectory"])

# Image.Image.'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getexif', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection'
# loop for scanning images
for image in images:
	img = Image.open((args["inputDirectory"]) + image)
	image_file = open((args["inputDirectory"]) + image).read()
	widthImg = Image.Image.width.__get__(img)
	heightImg = Image.Image.height.__get__(img)
	print(widthImg)
	print(heightImg)

	if (widthImg == int(args["width"]) and heightImg == int(args["height"])):#like: 
		img.show()

		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()

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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")

		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		
	elif (widthImg == 720 and heightImg == 1280):# like: Asus Z017D
		img.show()
		
		img.save((args["outputDirectory"])+"/"+ str(image))
		
		print(str(image))
		print("widthImg : " + str(widthImg)) 
		print("heightImg : " + str(heightImg))
		
		hash_object_md5 = hashlib.md5(image_file).hexdigest()
		print(hash_object_md5)
		
		hash_object_sha1 = hashlib.sha1(image_file).hexdigest()
		print(hash_object_sha1)
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")

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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
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
		
		filenamecsv.write(str(image)+","+str(widthImg)+","+str(heightImg)+","+hash_object_md5+","+hash_object_sha1+"\n")
		print("   ")
		
		time.sleep(3)
		# hide image
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()

	else:
		print("Not Screen Shot present in this directory")	
		
filenamecsv.close()
#image_file.close()
exit
