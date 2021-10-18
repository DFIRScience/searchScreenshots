#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
searchScreenshots compares image sizes to a list of common screenshot resolutions and saves matches.
Custom image sizes based on either a given height or width can also be searched.

LICENSE M.I.T.  https://opensource.org/licenses/MIT
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Built-in/Generic Imports
import os
import argparse
import datetime
import hashlib

# Libs
from PIL import Image
from datetime import datetime

__author__ = 'Antonio "Visi@n" Broi, Andrea Canepa (A-725-K), Joshua James (DFIRScience)'
__copyright__ = 'Copyright 2021, searchScreenshots'
__credits__ = ['Tsurugi Linux Team, https://tsurugi-linux.org']
__license__ = 'MIT'
__version__ = '1.0.1'
__maintainer__ = 'Joshua James (DFIRScience)'
__email__ = 'antonio@tsurugi-linux.org, andrea.canepa.12@protonmail.com, joshua@dfirscience.org'
__status__ = 'active, 2021-10-15'

# Constants
ASCII_ART = 'header.txt'


# Initialize the list of screenshot sizes
# Arguments: width read from CLI, height read from CLI
# Returns: a lookup list of screenshots sizes with format w:h:type
def init_ss_sizes(width, height):
    if int(width) > 0 and int(height) > 0:
        print('[!!] Custom resolution defined. Searching only for custom size.\n')
        return [f'{width}:{height}:Custom']
    elif int(width) > 0 or int(height) > 0:
        print('/!\\ Error: To define a custom resolution you must specify both width and heigth.')
        exit(1)

    # EDIT THIS LIST to add new known ss sizes
    # Apple device resolutions from https://w3codemasters.in/most-common-screen-resolutions/
    return [
        '720:1440:moto g(6)play P4 XT1922-1',
        '2048:2732:Ipad Pro',
        '720:1280:Asus Z017',
        '1920:1080:Generic Display',
        '360:640:Mobile Device',
        '375:667:iPhone 6/7/8/SE',
        '414:896:iPhone 11 Pro Max/XS/XR',
        '375:812:iPhone 11 Pro / X / XS',
        '414:736:iPhone 6/7/8 Plus',
        '320:568:iPhone 5 / iPod touch',
        '320:480:iPhone 4',
        '834:1194:iPad Pro',
        '810:1080:iPad 7th gen',
        '834:1112:iPad Pro/Air',
        '768:1024:iPad 5th gen/Pro/mini/air',
        '1024:1366:iPad Pro'
    ]


# Construct the argument parse and parse the arguments
# Arguments: None
# Returns: CLI arguments as strings
def parse_cli_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--inputDirectory', required=True, help='the root directory to search for images')
    ap.add_argument('-o', '--outputDirectory', default='output', help='the output images directory where to write the result')
    ap.add_argument('-c', '--csv', default= f'report_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.csv', help='the name of the csv report')
    ap.add_argument('-w', '--width', default=0, help='a custom image width')
    ap.add_argument('-e', '--height', default=0, help='a custom image height')
    # ap.add_argument('-p', '--pixel', default=400, help='the image pixel')
    return ap.parse_args()


# setup creates the output directory and CSV file
# Arguments: Output directory name and output CSV filename
# Returns: file handle for the csv output file
def setup(outdir, filename):
    # Check output directory. Exit if exists.
    if os.path.exists(outdir):
        print('/!\\ The output directory folder exists. Please try another name.')
        exit(1)

    print('Creating output folders and files...\n' + '_'*50 + '\n')
    os.makedirs(outdir)
    os.makedirs(f'{outdir}/images')
    
    filenamecsv = open(f'{outdir}/{filename}', 'w')
    filenamecsv.write('Filename,Width,Height,MD5,SHA1,Type\n')
    return filenamecsv


# process_image gets image attributes and to the output CSV file
# Arguments: image, output name, image content, csv report file name, output directory and screen type
# Returns: None
def process_image(image, image_name, image_file_content, filenamecsv, outputDir, type='unknown'):
    # image.show()
    try:
        image.save(f'{outputDir}/images/{image_name.split("/")[-1]}')
    except Exception as e:
        print(f'/!\\ Cannot save image because: {e}')
        exit(1)

    widthImg = Image.Image.width.__get__(image)
    heightImg = Image.Image.height.__get__(image)

    hash_object_md5 = hashlib.md5(image_file_content).hexdigest()
    hash_object_sha1 = hashlib.sha1(image_file_content).hexdigest()
    
    print(f'|--> image MD5: {hash_object_md5}')
    print(f'|--> image SHA1: {hash_object_sha1}\n')

    filenamecsv.write(f'{image_name},{widthImg},{heightImg},{hash_object_md5},{hash_object_sha1},{type}\n')

    # hide image
    '''
    time.sleep(3)
    for proc in psutil.process_iter():
        if proc.name() == 'display':
            proc.kill()
    '''


# ss_size_matches give sizes and known size list
# Arguments: current images width and height, known size list
# Returns: true/false, if true return image type
def ss_size_matches(widthImg, heightImg, known_ss_sizes):
    for size in known_ss_sizes:
        e = size.split(":")
        if e[2] == "Custom": # Custom find EITHER the width OR the height
            if e[0] == str(widthImg) or e[1] == str(heightImg):
                return True, e[2] # e[2] is the image type
        elif e[0] == str(widthImg) and e[1] == str(heightImg):
            return True, e[2] # e[2] is the image type
    return False, False


# process_dir_tree scans the input directory and sub-directories for images
# Arguments: input directory, outfile CSV file, output directory
# Returns: None
def process_dir_tree(directory, filenamecsv, outdir, known_ss_sizes):
    files = [os.path.join(path, f) for path, _, files in os.walk(directory) for f in files]

    # loop for scanning images
    for file in files:
        img = None
        try:
            img = Image.open(f'{file}')  # Image properties
        except Exception:
            # print(f'/!\\ {file} is not an image, skipping...\n')
            continue

        # print(f'[!!] Found image: {file}...')
        image_file = open(f'{file}', 'rb')
        image_content = image_file.read()  # Image contents data

        widthImg = Image.Image.width.__get__(img)
        heightImg = Image.Image.height.__get__(img)

        # print(f'|--> image width: {widthImg}')
        # print(f'|--> height: {heightImg}')

        match, typeImg = ss_size_matches(widthImg, heightImg, known_ss_sizes)
        if match:
            print(f'[!!] Screenshot resolution matched: {file}')
            process_image(img, file, image_content, filenamecsv, outdir, typeImg)

        img.close()
        image_file.close()


# Main execution function gets CLI arguments, call setup, process input dir
# Arguments: None
# Returns: None
def main():
    args = parse_cli_args()
    known_ss_sizes = init_ss_sizes(args.width, args.height)
    filenamecsv = setup(args.outputDirectory, args.csv)
    process_dir_tree(args.inputDirectory, filenamecsv, args.outputDirectory, known_ss_sizes)


if __name__ == '__main__':
    with open(ASCII_ART, 'r') as header:
        print(f'{header.read()}v{__version__} started at {datetime.now()}\n\n')
    main()
