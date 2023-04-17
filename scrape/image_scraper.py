from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
import time
import pandas as pd

def scraper(size):
    # Define the list of anime shows to search for
    a = pd.read_csv(r"D:\dataset\encoding\anime_frame.csv")
    #anime_list = ["Fullmetal Alchemist (TV)", "Death Note (TV)", "Cowboy Bebop (TV)", "Spirited Away (movie)", "Princess Mononoke (movie)", "(The) Melancholy of Haruhi Suzumiya (TV)", "Elfen Lied (TV)", "Neon Genesis Evangelion (TV)", "Code Geass: Lelouch of the Rebellion (TV)", "Bleach (TV)", "Code Geass: Lelouch of the Rebellion R2 (TV)"]
    anime_list = a["title"]
    serv = Service(r"C:\Users\titot\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    driver = webdriver.Chrome(service=serv)
    dims = ""
    # Create a new folder to store the downloaded images
    if size == "s":
        dims = "&tbs=isz:ex,iszw:300,iszh:300"       
        if not os.path.exists('anime_covers_small'):
            os.makedirs('anime_covers_small')
    elif size == "b":
        if not os.path.exists('anime_covers_large'):
            os.makedirs('anime_covers_large')


    for anime in a.iterrows():
        search_terms = anime[1][1] + ' anime cover' #anime title + anime cover
        encoded_terms = urllib.parse.quote(search_terms, safe=":/")
        full_url = 'https://www.google.com/search?tbm=isch&q='+encoded_terms+dims+"&tbs=ift:jpg"
        driver.get(full_url)
        #print(full_url)
        #get rid of cookies window  
        button = driver.find_elements(By.CSS_SELECTOR,"button.VfPpkd-LgbsSe")
        if len(button)>0:
            button[0].click()
        img_elements = driver.find_elements(By.CSS_SELECTOR,'a.wXeWr')
        #time.sleep(3)
        #print(anime)
        print(f"{len(img_elements)} small images")
        first_image = img_elements[0]
        first_image.click()

        real_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]')))
        #find the child image
        #real_img = driver.find_elements(By.CSS_SELECTOR, '#Sva75c > div.DyeYj > div > div.dFMRD > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.n4hgof > div.MAtCL.b0vFpe > a > img.r48jcc.pT0Scc.iPVvYb')
        #print(len([real_img]))
 
        img_link = real_img.get_attribute("href")
        driver.get(img_link)
        #print(img_link)
        
        img_urlx = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.r48jcc.pT0Scc.iPVvYb')))
        img_url = img_urlx.get_attribute("src")
        print(img_url)
        #save image to folder
        #img_name = anime[1][1].replace(' ', '_') + ".jpg"
        img_name = str(anime[1][0]) + ".jpg" #anime_id.jpg
        img_path = os.path.join('anime_covers_large', img_name)
        urllib.request.urlretrieve(img_url, img_path)

    while True:
        pass
scraper("b")