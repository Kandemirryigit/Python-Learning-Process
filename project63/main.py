# all chrome tabs should be close while this code running

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

liked_songs_path="C:/Users/CASPER/Desktop/python_projects/project63/liked.txt"
hadi_songs_path="C:/Users/CASPER/Desktop/python_projects/project63/hadi.txt"
fav_songs_path="C:/Users/CASPER/Desktop/python_projects/project63/fav.txt"
aes_songs_path="C:/Users/CASPER/Desktop/python_projects/project63/aes.txt"
acses_songs_path="C:/Users/CASPER/Desktop/python_projects/project63/acses.txt"


paths=[hadi_songs_path,aes_songs_path,liked_songs_path,fav_songs_path,acses_songs_path]

liked_songs_list=[]
hadi_songs_list=[]
fav_songs_list=[]
aes_songs_list=[]
acses_songs_list=[]

list=[hadi_songs_list,aes_songs_list,liked_songs_list,fav_songs_list,acses_songs_list]

count=0
for i in range(len(paths)):
    with open(paths[count],"r",encoding="UTF-8") as f:
        lines=f.readlines()
    lines=[line.strip() for line in lines]
    list[count].append(lines)
    count+=1




options = webdriver.ChromeOptions()

# This is your real Chrome user data path
options.add_argument("user-data-dir=C:\\Users\\CASPER\\AppData\\Local\\Google\\Chrome\\User Data")

# Optional: Start maximized (just looks nicer)
options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=options)

# Go to YouTube Music — and you're already logged in!
driver.get("https://music.youtube.com")

wait=WebDriverWait(driver,10)


FL_CLASS=".style-scope.ytmusic-playlist-add-to-option-renderer"
AES=10
ACSESI=18
FAV=26
HADI=34
LIKED=42


indexs=[HADI,AES,LIKED,FAV,ACSESI]



song_count=0
list_count=4


while len(list[list_count][0])!=song_count:
 
        time.sleep(3)

        search_youtube= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Şarkı, albüm, sanatçı veya podcast arayın']")))
        search_youtube.clear()
        search_youtube.send_keys(list[list_count][0][song_count],Keys.ENTER)
            
        try:

            save= wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Oynatma listesine kaydet']")))
            save.click()
            time.sleep(1)
    
            # If you want to change your library you should change this block
            library= wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,FL_CLASS)))[indexs[list_count]]
            library.click()

            song_count+=1
        except:
            with open("C:/Users/CASPER/Desktop/python_projects/project63/passed.txt","a",encoding="UTF-8") as file:
                file.writelines(f"From {indexs[list_count]}, Song: {list[list_count][0][song_count]}"+"\n")
            song_count+=1



                

   























# I took songs like this ı manually took every list




# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id="5c254d72e4bc4e658eeff25511f76d7a",
#     client_secret="b7268d421fef4cce8725e158c56b8314",
#     redirect_uri="http://127.0.0.1:8888/callback",
#     scope="playlist-read-private",
# ))



# aesı="19oS7mqhbgAq1TcNhM5EHr"
# fav="69N0Pzw9XWPQCn1sRaFjPo"
# acses="2K0ClYwqrBeavbyVGFkvnU"
# hadi="5dZmHKsVBuEioTdiJzj1Xq"



# aes=[]
# x=0
# while len(aes)!=56:
#     results=sp.playlist_tracks(aesı,limit=6,offset=50)
#     for item in results["items"]:
#             track=item["track"]
#             track_name=track["name"]
#             aes.append(track_name)
#             with open("C:/Users/CASPER/Desktop/python_projects/project63/aes.txt","a",encoding="UTF-8") as f:
#                     f.writelines(track_name+"\n")
#     x+=50
    

# print(aes)



















