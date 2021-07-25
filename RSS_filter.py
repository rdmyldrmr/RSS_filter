unreadNewsparameter = 1
#from PIL import ImageGrab
import time
import pyautogui
from datetime import datetime
#from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
import pytesseract
found_wanted_word_count = 0
news_marked_as_undread_count = 0
found_word_list= []
#secreenshot = ImageGrab.grab(bbox =(350,194,1100,350))
forbidden_words = ['Apple','apple','microsoft','Microsoft','Tesla','Tesla,','Samsung','samsung','iphone','iphones','iPhones','iPhone','ipad','iPad','xbox','XBOX',
                   'twitter','Twitter','Amazon','Galaxy','Huawei','Elon','Elan','Musk','Bezos','Spacex','SpaceX','Windows','GOOGLE','Xbox',
                   'Google','OnePlus','ios','AMD','GTA','HUAWEI','iOS','Facebook','PlayStation','OPPO','Oppo','Snapdragon','Qualcomm',
                   'Youtube','YouTube','Xiaomi','Toshiba','ChromeBook','WhatsApp','Instagram','iRobot','Roomba','Nvidia','Alexa','Porsche',
                   'Xiaomi','XIAOMI','Sony','SONY','AMD','ZTE','Disney+','MacBook','Macbook','macOS','MacOS','AT&T','Nokia','NOKIA','watchOS','TikTok',
                   'Tiktok','ChromeBook','Chromebook','Lenovo','Bitcoin','Pokemon','Android','Redmi','RedMi','Volkswagen','Mercedes','Volvo',
                   'Renault','T-mobile','T-Mobile','Xperia','Philips','Airpods','AirPods','PS4','PS5','ClubHouse','Clubhouse','NVIDIA','Seat',
                   'Steam','Token','token','Ripple','Qualcomm','Nissan','Honda','Pinterest','HarmonyOS','Uber','UBER','Starlink','Hyundai'
                   'Vivo','lnstagram','Robinhood','Marvel','NSA','Realme','NFT','Covid-19','Branson','Toyota','blockchain','CRISPR','HBO',
                   'Broadcom','Netflix','Hulu','iPadOS','Fiat','COVID-19','Boeing','Maserati','POCO','Mitsubishi','Yahoo','YAHOO','Bugatti',
                   'Peugeot','Skoda','Skoda','Opel','Nikon','Nintendo','HomePod','Homepod','iMac','Snyder','Firefox','Netflix','Biden',
                   'Trump','Marvel','MARVEL','COVID','Covid','Verizon','Peacock','Bentley']
def wordHunt(text):
    if len(text) == 0:
        #print('no caption')
        return False
    else:
        text_lower = text.lower()
        print(text_lower)
    news_headline_words = text.split()
    for words in forbidden_words:
        for wantedWord in news_headline_words:
            if words == wantedWord:
                print('buldum :' + words)
                found_word_list.append(words)
                return True
for x in range(unreadNewsparameter):
    print(x)
    pyautogui.moveTo(320,190,0.2)
    pyautogui.click()
    current_news_headline = pyautogui.screenshot(region=(350,196,750,154))
    current_news_headline.show()
    time.sleep(3)
    current_news_headline_rgb = current_news_headline.convert('RGB')
    current_news_headline_rgb.show()
    time.sleep(3)
    current_news_headline_grayscale = ImageOps.grayscale(current_news_headline_rgb)
    current_news_headline_grayscale.show()
    time.sleep(3)
    current_news_headline_inverted = ImageOps.invert(current_news_headline_grayscale)
    current_news_headline_inverted.show()
    time.sleep(3)
    current_news_headline_inverted_edge_more = current_news_headline_inverted.filter(ImageFilter.EDGE_ENHANCE_MORE)
    current_news_headline_inverted_edge_more.show()
    time.sleep(3)
    #current_news_headline_sharpness = ImageEnhance.Sharpness(current_news_headline_inverted_edge_more)
    #current_news_headline_sharpness_enhanced = current_news_headline_sharpness.enhance(8)
    #current_news_headline_sharpness_enhanced.show()
    #time.sleep(3)
    #current_news_headline_contrast = ImageEnhance.Contrast(current_news_headline_sharpness_enhanced)
    #current_news_headline_contrast_enhanced = current_news_headline_contrast.enhance(8)
    #current_news_headline_contrast_enhanced.show()
    #time.sleep(3)
    #current_headline_text = pytesseract.image_to_string(current_news_headline_contrast_enhanced)
    current_headline_text = pytesseract.image_to_string(current_news_headline_inverted_edge_more)
    current_headline_text = current_headline_text.replace("'",' ')
    current_headline_text = current_headline_text.replace(",",' ')
    current_headline_text = current_headline_text.replace(":",' ')
    current_headline_text_lower = current_headline_text.lower()
    #print(current_headline_text_lower)
    wordhunt_function_returned_state = wordHunt(current_headline_text_lower)
    if wordhunt_function_returned_state:
    # append word to found forbidden words list
    #add code here for this
        pyautogui.press('j')
        print('marked:read')
        found_wanted_word_count += 1
        print('found wanted word count :' + str(found_wanted_word_count))
    else:
        pyautogui.press('m')
        print('marked:UN_read')
        news_marked_as_undread_count += 1
        print('news marked as undread count :'+ str(news_marked_as_undread_count))
        pyautogui.press('j')
    pyautogui.moveTo(1080,190,0.2)
    pyautogui.click()
    print("---------------------------------------------------------------")
print('news marked as undread  :'+ str(news_marked_as_undread_count))
print('found forbidden words  :' + str(found_wanted_word_count))
print(found_word_list)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
write_date=open('rsslog.txt','a')
write_date.write('\n')
write_date.write('--------------------------------\n')
write_date.write(dt_string)
write_date.write('\n')
write_date.write('reviewed total news headlines :' + str(unreadNewsparameter))
write_date.write('\n')
write_date.write('news marked as unread count :'+ str(news_marked_as_undread_count))
write_date.write(' \n')
write_date.write('found word count :' + str(found_wanted_word_count))
write_date.write('\n')
write_date.close()
with open('rsslog.txt', 'a') as f:
    for item in found_word_list:
        f.write("%s " % item)
