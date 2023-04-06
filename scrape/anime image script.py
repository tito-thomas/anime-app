import os
import urllib.request
from bs4 import BeautifulSoup
import time

def scraper(size):
    # Define the list of anime shows to search for
    anime_list = ['Attack on Titan']#, 'One Piece', 'Naruto', 'Death Note']

    # Create a new folder to store the downloaded images
    if size == "s":
        if not os.path.exists('anime_covers_small'):
            os.makedirs('anime_covers_small')
    elif size == "b":
        if not os.path.exists('anime_covers_large'):
            os.makedirs('anime_covers_large')

    # Loop through the anime list and search google images for each show
    for anime in anime_list:
        search_terms = anime + ' anime cover'
        encoded_terms = urllib.parse.quote(search_terms, safe=":/")
        dims = "&tbs=isz:ex,iszw:800,iszh:600"
        if size == "s":
            dims = "&tbs=isz:ex,iszw:300,iszh:300"

        full_url = 'https://www.google.com/search?tbm=isch&q='+encoded_terms+dims
        #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36', 'Cookie':''}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
        print(full_url)
        req = urllib.request.Request(full_url, headers=headers)
        html = urllib.request.urlopen(req).read()
    
        soup = BeautifulSoup(html, 'html.parser')
        img_link = soup.find("img",attrs={"class": "rg_i"})
        #big_img = soup.find("div")
        #children = soup.find_all("div")
        #print(big_img)
        #for i in children:
            #for x in i.children:
                #print(x)
                
        
        print(img_link)
        #print(children)
        #img_name = anime.replace(' ', '_') + ".jpg"
        #img_path = os.path.join('anime_covers_small', img_name)
        #urllib.request.urlretrieve(img_link, img_path)

        print('Downloaded cover image for', anime)
        
    print('All images downloaded successfully!')

scraper("b")