import argparse
import itertools
import json
import logging
import os
import sys
import uuid
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

google_strings = ['g', 'G', 'google', 'Google', 'GOOGLE', 'goog', 'Goog']
instagram_strings = ['i', 'I', 'instagram', 'Instagram', 'INSTAGRAM', 'insta', 'Insta']
tumblr_strings = ['t', 'T', 'tumblr', 'Tumblr', 'tumbler', 'Tumbler', 'tmblr', 'Tmblr']

def configure_logger():
    _log = logging.getLogger()
    _log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('[%(asctime)s %(levelname)s %(module)s]: %(message)s'))
    _log.addHandler(handler)
    return _log

_log = configure_logger()

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

def get_soup(url, header):
    response = urlopen(Request(url, headers=header))
    return BeautifulSoup(response, 'lxml')

def get_query_url(query):
    return "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" %(query)

def extract_images_from_google_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records

def extract_images_from_insta_soup(soup):
    image_elements = soup.find_all("img")
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records

def extract_google_images(query, num_images):
    url = get_query_url(query)
    _log.info("Getting soup")
    soup = get_soup(url, REQUEST_HEADER)
    _log.info("Extracting image urls")
    link_type_records = extract_images_from_google_soup(soup)
    print("Link type records = %s" %(link_type_records))
    return itertools.islice(link_type_records, num_images)

def extract_insta_images_from_page(link, num_images):
    pass
    
def extract_insta_images_by_query(query, num_images):
    pass

def extract_insta_images_by_query_from_page(query, link, num_images):
    pass

def get_raw_response(url):
    request = Request(url, headers=REQUEST_HEADER)
    response = urlopen(request)
    return response.read()

def save_images(raw_image, image_type, save_directory):
    extension = image_type if image_type else 'jpg'
    file_name = uuid.uuid4().hex
    save_path = os.path.join(save_directory, file_name)
    with open(save_path, 'wb') as image_file:
        image_type.write(raw_image)

def download_images_to_directory(images, save_directory, num_images):
    for i, (url, image_type) in enumerate(images):
        try:
            _log.info("Making request (%d/%d): %s", i, num_images, url)
            raw_images = get_raw_response(url)
            save_images(raw_images, image_type, save_directory)
        except Exception as e:
            _log.exception(e)

def run_google(query, save_directory, num_images):
    if (query == ''):
        query = 'halloween costumes'
    query = '+'.join(query.split())
    _log.info("Extracting image links")
    images = extract_google_images(query, num_images)
    print("Images (from itertools) = %s" %(images))
    _log.info("Downloading images")
    download_images_to_directory(images, save_directory, num_images)
    _log.info("Finished")

def run_instagram(query, link, save_directory, num_images):
    if (query == '' and link != ''):
        #Grab from page provided
        images = extract_insta_images_from_page(link, num_images)
    elif (query != '' and link == ''):
        #Search instagram for #query
        images = extract_insta_images_by_query(query, num_images)
    elif (query != '' and link != ''):
        #Search the page for #query
        images = extract_insta_images_by_query_from_page(query, link, num_images)
    download_images_to_directory(images, save_directory, num_images)

def main():
    parser = argparse.ArgumentParser(description="Multi-source image scraper")
    parser.add_argument('-s', '--search', default='', type=str, help='Search term')
    parser.add_argument('-n', '--num_images', default=1, type=int, help='Number of images to save')  
    parser.add_argument('-d', '--directory', default='~/Pictures/scraping', type=str, help='Save directory')
    parser.add_argument('-u', '--use', default='google', type=str, help='Specify image source. google, tumbler, instagram, etc')
    parser.add_argument('-l', '--link', default='', type=str, help='Provide a link to a page, i.e. instagram, tumblr')
    args = parser.parse_args()
    if args.link != '' :
        #A specific page has been given
    elif args.use in google_strings :
        run_google(args.search, args.directory, args.num_images)
    elif 
    else:
        print("One or more inputs was incorrect!")