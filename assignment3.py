import argparse
# other imports go here
import csv
import requests
import re

def downloadData(url):
    """
    Reads data from the URL and returns the data as a string
    :param url: 
    :return: 
    """
    response = requests.get(url)
    return response.text

def processData(url):
    """
    Reads data row by row and searches images and browsers
    :param url:
    :return:
    """
    data = downloadData(url)
    rows = data.split('\r\n')
    image_hits = []
    firefox_hits = []
    chrome_hits = []
    intExp_hits = []
    line_count = 0

    #image search Regex. Searching for .jpg, .gif. and .png
    image_Regex = re.compile(r'jp(e)?g|jpg|gif|png', re.I)
    #browser search Firefox Regex
    firefox_Regex = re.compile(r'Firefox')
    #browser search Chrome Regex
    chrome_Regex = re.compile(r'Chrome')
    #browser search Internet Explorer Regex
    intExp_Regex = re.compile(r'MSIE')
    for row in rows:
        #search row for image hits and add to image_hits list if found
        if image_Regex.search(row):
            image_hits.append(row)
        #search row for Firefox hits and add to firefox_hits if found
        if firefox_Regex.search(row):
            firefox_hits.append(row)
        #search row for Chrome hits and add to chrome_hits if found
        elif chrome_Regex.search(row):
            chrome_hits.append(row)
        #search row Internet Explorer hits and add to intExp_hits if found
        elif intExp_Regex.search(row):
            intExp_hits.append(row)

    #calculate what percentage of hits were for images and print result
    image_perc = (len(image_hits) * 100) / len(rows)
    trunc_perc = ("{:.1f}".format(image_perc))
    print(f"Image requests account for {trunc_perc}% of all requests.")

    #figure out which browser had the most hits
    if len(firefox_hits) >= len(chrome_hits):
        if len(firefox_hits) >= len(intExp_hits):
            print("Firefox is the most popular browser today.")
        elif len(chrome_hits) >= len(intExp_hits):
            print("Chrome is the most popular browser today.")




def main(url):
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    print(f"Running main with URL = {url}...")



if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)



    
