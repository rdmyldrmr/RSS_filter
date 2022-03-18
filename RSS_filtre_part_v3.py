unreadNewsparameter = 1000 #define number of news headline to be read
import pyautogui #import libraries
from datetime import datetime
from PIL import ImageOps
from PIL import ImageFilter
import pytesseract
found_wanted_word_count = 0
news_marked_as_undread_count = 0
found_word_list= []
#define array of forbiden words
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
    if len(text) == 0: #there is no text found in the screenshot
        return False #return wordhunt function result as false
    else:
        text_lower = text.lower() #convert headline to all lowercase
    news_headline = text_lower.split('\n\n') #get rid of unwanted chars
    news_headline_singleline = news_headline[0] #take the first sentence
    news_headline_singleline = news_headline_singleline.replace("\n", " ") #get rid of unwanted chars
    news_headline_words = news_headline_singleline.split() #convert sentence to words
    for words in forbidden_words: #look for unwanted word through headline words
        for wantedWord in news_headline_words:
            if words == wantedWord:
                found_word_list.append(words)
                return True #return wordhunt function result as true
#start the main loop
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
    pyautogui.moveTo(320,190,1) #move mouse next to headline
    pyautogui.click() 
    current_news_headline = pyautogui.screenshot(region=(385,196,750,154)) #take screenshot of the headline 
    current_news_headline_rgb = current_news_headline.convert('RGB') #OpenCV is BGR, Pillow is RGB
    current_news_headline_grayscale = ImageOps.grayscale(current_news_headline_rgb) #convert color image to grayscale 
    current_news_headline_inverted = ImageOps.invert(current_news_headline_grayscale) #invert colors black2white white2black
    current_news_headline_inverted_edge_more = current_news_headline_inverted.filter(ImageFilter.EDGE_ENHANCE_MORE) #enhabce image
    current_headline_text = pytesseract.image_to_string(current_news_headline_inverted_edge_more) #convert image to text with OCR
    current_headline_text = current_headline_text.replace("'",' ')#get rid of apostrophes 
    current_headline_text = current_headline_text.replace(",",' ')#get rid of commas
    current_headline_text = current_headline_text.replace(":",' ')#get rid of colons
    current_headline_text = current_headline_text.replace("’",' ')#get rid of apostrophes
    current_headline_text = current_headline_text.replace("‘",' ')#get rid of apostrophes
    wordhunt_function_returned_state = wordHunt(current_headline_text) #call wordhunt function
    if wordhunt_function_returned_state: #found a forbidden word
        pyautogui.press('j') #next new headline please
        print('marked:read')
        found_wanted_word_count += 1 #increment counter
        print('found wanted word count :' + str(found_wanted_word_count))
    else:
        pyautogui.press('m') #mark this post as UNread
        print('marked:UN_read')
        news_marked_as_undread_count += 1 #increment counter
        print('news marked as undread count :'+ str(news_marked_as_undread_count))
        pyautogui.press('j') #next new headline please
    pyautogui.moveTo(1080,190,1.2)
    pyautogui.click()
    print("---------------------------------------------------------------")
print('news marked as undread  :'+ str(news_marked_as_undread_count))
print('found forbidden words  :' + str(found_wanted_word_count))
print(found_word_list)
#logging analysis results to a text file
now = datetime.now() #get the date and time 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #day month year hour minute second
write_date=open('rsslog.txt','a') #open txt log file
write_date.write('\n')
write_date.write('--------------------------------\n')
write_date.write(dt_string) #log the date
write_date.write('\n')
write_date.write('reviewed total news headlines :' + str(unreadNewsparameter)) # log data
write_date.write('\n')
write_date.write('news marked as unread count :'+ str(news_marked_as_undread_count)) # log data 
write_date.write(' \n')
write_date.write('found word count :' + str(found_wanted_word_count)) # log data
write_date.write('\n')
write_date.close()
with open('rsslog.txt', 'a') as f: # log found forbidden words to txt file
    for item in found_word_list:
        f.write("%s " % item)
#all results logged to a text file