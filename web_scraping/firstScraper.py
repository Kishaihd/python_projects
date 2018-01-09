import json
import itertools
import os
import sys
import uuid
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import logging
import re
import csv


def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('[%(asctime)s %(levelname)s %(module)s]: %(message)s'))
    logger.addHandler(handler)
    return logger

logger = configure_logging()


numImages = 10
imageList = []
save_directory = '/home/kaden/Pictures/scraping'
serebro_insta = 'https://www.instagram.com/serebro_official/'

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

#ser_img = 
#for texts in ser_soup.find_all("img"):
    #if texts.
    #print(img)
#name_box = ser_soup.find('div', attrs={'class': '_4rbun'})

def extract_images_from_soup(soup):
    image_elements = soup.find_all("img")
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records

def get_raw_image(url):
    req = Request(url, headers=REQUEST_HEADER)
    resp = urlopen(req)
    return resp.read()

def save_image(raw_image, image_type, save_directory):
    extension = image_type if image_type else 'jpg'
    file_name = uuid.uuid4().hex
    save_path = os.path.join(save_directory, file_name)
    with open(save_path, 'wb') as image_file:
        image_file.write(raw_image)

def download_images_to_dir(images, save_directory, num_images):
    for i, url in enumerate(images):
        # print("i = %s" %i)
        # print("image type = %s" %image_type)
        try:
            # logger.info("Making request (%d/%d): %s", i, num_images, url)
            raw_image = get_raw_image(url)
            save_image(raw_image, 'jpg', save_directory)
        except Exception as e:
            logger.exception(e)

def main():
    #loginfo = 'Opening page %s...' %(serebro_insta)
    #logger.info(loginfo)
    ser_page = urlopen(Request(serebro_insta, headers=REQUEST_HEADER))
    #logger.info("Getting soup...")
    ser_soup = BeautifulSoup(ser_page, 'lxml')
    splitified = str(ser_soup).split("\"")
    # print(splitified)
    #print("\n\nfor line in splitified...\n\n")
    for line in splitified:
    #    print(line)
        if line.lower().endswith('.jpg'): # , '.gif', '.png'):
    #        print("Picture!")
            imageList.append(line)
    if (len(imageList) > 0):
        print(imageList)
    else:
        print("List is empty!")
    # print(ser_soup.prettify())
    # logger.info("\nGetting link types...")
    # link_type_records = extract_images_from_soup(ser_soup)
    # print(link_type_records)
    # logger.info("Getting images...")
    # images = itertools.islice(link_type_records, numImages)
    # print(images)
    downloadMsg = "\n\nDownloading images to %s...\n\n" %(save_directory)
    logger.info(downloadMsg)
    download_images_to_dir(imageList, save_directory, numImages)

if __name__ == '__main__':
    main()
