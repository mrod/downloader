#!/usr/bin/python3

import sys
import urllib.request
import os 

def main(argv):
   source_url = sys.argv[1]
   dir_path = os.path.dirname(os.path.realpath(__file__))

   print(dir_path)

   print('\nDownloading video...')       
   source_url = source_url.replace('audio', 'video')
   download(source_url, 'video')
              
   print('\nDownloading audio...')       
   source_url = source_url.replace('video', 'audio')
   download(source_url, 'audio')


def download(source_url, suffix):
   for x in range(1000):
       url = source_url.replace('segment-0', 'segment-' + str(x))
       try:
           print('\nDownloading: ' + url)
           urllib.request.urlretrieve(url, 'segment-' + str(x) + '.'+ suffix + '.m4s')
       except urllib.error.HTTPError:
           print('\nNo more segments')
           break    
    

if __name__ == "__main__":
   main(sys.argv[1:])