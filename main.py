# Time,Schedule and instabot imported
from instabot import Bot 
import schedule
import time

bot = Bot() 

# login
usr = "user_name" # username
pwd = "user_password" # password

def random_picture():
     
    bot.login(username = usr,password = pwd)

    # Recommended to put the photo you want to upload in the same 
    # directory where this Python code is located else you will have  
    # to provide full path for the photo 
    bot.upload_photo("image.jpg", caption ="caption_for_photo") 

schedule.every(0.2).minutes.do(random_picture) 
schedule.every(4).hours.do(random_picture) 

while True:
    schedule.run_pending() # waiting for schedule
    time.sleep(1) # countdown 1 second
