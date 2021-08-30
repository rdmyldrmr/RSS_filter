unreadNewsparameter = 180
import pyautogui
from datetime import datetime
from PIL import ImageOps
from PIL import ImageFilter
import pytesseract
found_wanted_word_count = 0
news_marked_as_undread_count = 0
found_word_list= []
forbidden_words = ['apple','microsoft','tesla','samsung','iphone','iphones','amazon','twitter','ipad','galaxy','xbox','huawei','harmonyos','qualcomm',
                   'elon','elan','musk','bezos','spacex','windows','google','xbox','oneplus','ios','amd','gta','facebook','playstation','marvel','ipados',
                   'oppo','snapdragon','qualcomm','youtube','xiaomi','toshiba','chromebook','whatsapp','instagram','irobot','roomba','nvidia','alexa',
                   'sony','amd','zte','disney+','macbook','macos','at&t','nokia','watchos','tiktok','lenovo','porsche','clubhouse','nissan','yahoo',
                   'bitcoin','pokemon','android','redmi','volkswagen','mercedes','volvo','renault','xperia','philips','airpods','airpod','ps4','ps5','netflix',
                   'imac','homepod','realme','boeing','skoda','broadcom','branson','starlink','hyundai','biden','trump','vivo','robinhood','hbo',
                   'bugatti','t-mobile','ripple','seat','steam','token','nissan','honda','pinterest','blockchain','uber','firefox','mitsubishi','nsa',
                   'hulu','lnstagram','snyder','opel','maserati','poco','nft','covid-19','toyota','crispr','nintendo','nikon','covid','verizon',
                   'fiat','peugeot','peacock','bentley','mitsubishi','marvel','ps5','motorola','ps4','covld-19','vodafone','tencent','wechat','honor',
                   'audi','ford','fortnite','roku','quibi','brexit','salesforce','lamborghini','jaguar','ferrari','mclaren','chevrolet','spotify','pokémon','aston',
                   'airbnb','p85','cadillac','bmw','corvette','wearos','comcast','peloton','p55','p54'
                   ]
def wordHunt(text):
    if len(text) == 0:
        return False
    else:
        text_lower = text.lower()
        #print(text_lower)
    news_headline = text_lower.split('\n\n')
    news_headline_singleline = news_headline[0]
    news_headline_singleline = news_headline_singleline.replace("\n", " ")
    print(news_headline_singleline)
    news_headline_words = news_headline_singleline.split()
    for words in forbidden_words:
        for wantedWord in news_headline_words:
            if words == wantedWord:
                print('buldum :' + words)
                found_word_list.append(words)
                return True
for x in range(unreadNewsparameter):
    maybe_next_time_location = pyautogui.locateOnScreen('maybe_next_time.png')
    if maybe_next_time_location == None:
        print('no banner in sight')
    else:
        print(maybe_next_time_location)
        print('Adblocker banner popped-up')
        maybe_next_time_button = pyautogui.center(maybe_next_time_location)
        pyautogui.moveTo(maybe_next_time_button[0], maybe_next_time_button[1], 1)
        pyautogui.click()
        
    print(x)
    pyautogui.moveTo(320,190,1)
    pyautogui.click()
    current_news_headline = pyautogui.screenshot(region=(385,196,750,154))
    current_news_headline_rgb = current_news_headline.convert('RGB')
    current_news_headline_grayscale = ImageOps.grayscale(current_news_headline_rgb)
    current_news_headline_inverted = ImageOps.invert(current_news_headline_grayscale)
    current_news_headline_inverted_edge_more = current_news_headline_inverted.filter(ImageFilter.EDGE_ENHANCE_MORE)
    current_headline_text = pytesseract.image_to_string(current_news_headline_inverted_edge_more)
    current_headline_text = current_headline_text.replace("'",' ')
    current_headline_text = current_headline_text.replace(",",' ')
    current_headline_text = current_headline_text.replace(":",' ')
    current_headline_text = current_headline_text.replace("’",' ')
    current_headline_text = current_headline_text.replace("‘",' ')
    wordhunt_function_returned_state = wordHunt(current_headline_text)
    if wordhunt_function_returned_state:
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
    pyautogui.moveTo(1080,190,1.2)
    pyautogui.click()
    print("---------------------------------------------------------------")
print('news marked as undread  :'+ str(news_marked_as_undread_count))
print('found forbidden words  :' + str(found_wanted_word_count))
print(found_word_list)
#logging analysis results to a text file
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
#all results logged to a text file
        
        
        
        
# current_news_headline = pyautogui.screenshot(region=(350,196,750,154))
# current_news_headline.show()
# current_news_headline_rgb = current_news_headline.convert('RGB')
# current_news_headline_grayscale = ImageOps.grayscale(current_news_headline_rgb)
# current_news_headline_inverted = ImageOps.invert(current_news_headline_grayscale)
# current_news_headline_inverted_edge_more = current_news_headline_inverted.filter(ImageFilter.EDGE_ENHANCE_MORE)
# current_headline_text = pytesseract.image_to_string(current_news_headline_inverted_edge_more)
# current_headline_text = current_headline_text.replace("'",' ')
# current_headline_text = current_headline_text.replace(":",' ')
# current_headline_text = current_headline_text.replace("’",' ')
# current_headline_text = current_headline_text.replace(",",' ')
# current_headline_text = current_headline_text.replace("‘",' ')
# text_lower=current_headline_text.lower()
# news_headline = text_lower.split('\n\n')
# news_headline_singleline = news_headline[0]
# news_headline_singleline = news_headline_singleline.replace("\n", " ")
# news_headline_words = news_headline_singleline.split()
# print(news_headline_words)
        



