#import necessary libraries
from bs4 import BeautifulSoup as bs
import os
import requests
import boto3

s3 = boto3.client('s3')

#function to download the images, takes 2 parameters: List of image links and folder name to download the images
def download_images(images, folder_name='images/'):
    count=0

    print(f"Total {len(images)} found")

    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                #get the link of the each images
                image_link = image["src"]

                #print(image_link)

                #fetch the content of the image
                r = requests.get(image_link).content

                #create a distinct key for each object and put it in images folder
                key = 'images/Enverus_Sample_Image_' + str(count)

                #change the name of bucket
                s3.put_object(Body=r, Bucket='enverusdemoscapper20220826', Key=key)

                count += 1

            except:
                pass

#main function
def lambda_handler(event, context):


    #get the request for a specific link
    req =  requests.get('https://www.google.com/search?q=enverus&tbm=isch&ved=2ahUKEwj-ocjg5N35AhUbkmoFHeTRA04Q2-cCegQIABAA&oq=enverus&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAELEDEEM6CAgAEIAEELEDOggIABCxAxCDAToLCAAQgAQQsQMQgwE6CggAELEDEIMBEEM6BAgAEENQwRBYoCBgxiFoAHAAeACAAYoBiAGGB5IBAzIuNpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=lDYFY_6HGZukqtsP5KOP8AQ&bih=898&biw=1785&rlz=1C5CHFA_enUS1006US1006/')

    # Parse HTML Code
    soup = bs(req.text, 'html.parser')

    #find all images in URL
    images = soup.find_all('img')
    print(images)

    #call the download function
    download_images(images)

    #s3.create_bucket(Bucket='navneetrt35705')
