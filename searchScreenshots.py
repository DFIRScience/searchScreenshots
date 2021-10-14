#!/usr/bin/python3

# by Antonio "Visi@n" Broi antonio@tsurugi-linux.org
# by Andrea Canepa (A-725-K) andrea.canepa.12@protonmail.com
# https://tsurugi-linux.org
# 20211014

#
# LICENSE M.I.T.  https://opensource.org/licenses/MIT
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time
import argparse
import os
import hashlib
import psutil

from PIL import Image
from datetime import datetime


# construct the argument parse and parse the arguments
def parse_cli_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--inputDirectory', required=True, help='the input images directory to search for width height and pixel')
    ap.add_argument('-o', '--outputDirectory', default='output', help='the output images directory where to write the result')
    # ap.add_argument('-w', '--width', default=720, help='the images width')
    # ap.add_argument('-e', '--height', default=1440, help='the images height')
    # ap.add_argument('-p', '--pixel', default=400, help='the images pixel')
    return ap.parse_args()


def setup(OUTDIR):
    print('Creating output folders and files...\n' + '_'*50 + '\n')
    # Only use output directory - check if exists or
    # Create random file name
    if os.path.exists(OUTDIR):
        print('The output directory folder exists. Please try another name.')
        exit(1)

    os.makedirs(OUTDIR)
    os.makedirs(f'{OUTDIR}/images')
    
    filename = f'report_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.csv'
    filenamecsv = open(f'{OUTDIR}/{filename}', 'w')
    filenamecsv.write('filename,width,height,MD5,SHA1,type\n')
    return filenamecsv


def process_image(image, image_name, image_file_content, filenamecsv, outputDir, type):
    image.show()
    try:
        image.save(f'{outputDir}/images/{image_name.split("/")[-1]}')
    except Exception as e:
        print(f'Cannot save image because: {e}')
        exit(1)

    widthImg = Image.Image.width.__get__(image)
    heightImg = Image.Image.height.__get__(image)

    hash_object_md5 = hashlib.md5(image_file_content).hexdigest()
    hash_object_sha1 = hashlib.sha1(image_file_content).hexdigest()
    
    print(f'|--> image MD5: {hash_object_md5}')
    print(f'|--> image SHA1: {hash_object_sha1}\n')

    filenamecsv.write(f'{image_name},{widthImg},{heightImg},{hash_object_md5},{hash_object_sha1},{type}\n')

    time.sleep(3)

    # hide image
    for proc in psutil.process_iter():
        if proc.name() == 'display':
            proc.kill()


# process the input directory and all its sub-directories
def process_dir_tree(directory, filenamecsv, outdir):
    files = [os.path.join(path, f) for path, _, files in os.walk(directory) for f in files]

    # loop for scanning images
    for file in files:
        img = None
        try:
            img = Image.open(f'{file}')  # Image properties
        except Exception as e:
            print(f'/!\\ {file} is not an image, skipping...\n')
            continue

        print(f'[!!] Found image: {file}...')
        image_file = open(f'{file}', 'rb')
        image_content = image_file.read()  # Image contents data

        widthImg = Image.Image.width.__get__(img)
        heightImg = Image.Image.height.__get__(img)

        print(f'|--> image width: {widthImg}')
        print(f'|--> height: {heightImg}')

        if (widthImg == 720 and heightImg == 1440):  # like: moto g(6)play P4 XT1922-1 #
            process_image(img, file, image_content, filenamecsv, outdir, 'moto g(6)play P4 XT1922-1')
        elif (widthImg == 2048 and heightImg == 2732):  # like: Ipad Pro
            process_image(img, file, image_content, filenamecsv, outdir, 'Ipad Pro')
        elif (widthImg == 720 and heightImg == 1280):  # like: Asus Z017
            process_image(img, file, image_content, filenamecsv, outdir, 'Asus Z017')
        else:
            print('|--> [??] Unknown ScreenShot size [??]\n')

        img.close()
        image_file.close()


def main():
    args = parse_cli_args()
    filenamecsv = setup(args.outputDirectory)
    process_dir_tree(args.inputDirectory, filenamecsv, args.outputDirectory)


main()
