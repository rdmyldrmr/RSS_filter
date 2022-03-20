import pyautogui
from tkinter import *
from tkinter import ttk
import re
from datetime import datetime
from PIL import ImageOps
from PIL import ImageFilter
import pytesseract
from PIL import Image, ImageTk
import sys
sys.setrecursionlimit(2500)
#im = Image.open("otopark.jpg")
#photo = ImageTk.PhotoImage(im)
#photo_label = tk.Label(root, image=photo)
#photo_label.pack()

found_word_list= []
forbidden_words = ['apple','microsoft','tesla','samsung','iphone','iphones','amazon',
                   'twitter','ipad','galaxy','xbox','huawei','harmonyos','qualcomm',
                   'elon','elan','musk','bezos','spacex','windows','google','xbox',
                   'oneplus','ios','amd','gta','facebook','playstation','marvel','ipados',
                   'oppo','snapdragon','qualcomm','youtube','xiaomi','toshiba','chromebook',
                   'whatsapp','instagram','irobot','roomba','nvidia','alexa','waymo',
                   'sony','amd','zte','disney+','macbook','macos','at&t','nokia','watchos',
                   'tiktok','lenovo','porsche','clubhouse','nissan','yahoo','evtol',
                   'bitcoin','pokemon','android','redmi','volkswagen','mercedes','volvo','renault',
                   'xperia','philips','airpods','airpod','ps4','ps5','netflix',
                   'imac','homepod','realme','boeing','skoda','broadcom','branson','starlink','hyundai',
                   'biden','trump','vivo','robinhood','hbo','cryptocurrency','opensea',
                   'bugatti','t-mobile','ripple','seat','steam','token','nissan','honda','pinterest',
                   'blockchain','uber','firefox','mitsubishi','nsa','rogan',
                   'hulu','lnstagram','snyder','opel','maserati','poco','nft','covid-19','toyota',
                   'crispr','nintendo','nikon','covid','verizon','metaverse',
                   'fiat','peugeot','peacock','bentley','mitsubishi','marvel','ps5','motorola','ps4',
                   'covld-19','vodafone','tencent','wechat','honor','pelaton',
                   'audi','ford','fortnite','roku','quibi','brexit','salesforce','lamborghini','jaguar',
                   'ferrari','mclaren','chevrolet','spotify','pokémon','aston','blackberry',
                   'airbnb','p85','cadillac','bmw','corvette','wearos','comcast','peloton','p55','p54'
                   ]

    #check if the entry value is number
def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 4
    #start and trigger filtering
def start():
    loop_to_go = num.get()
    news_headline_inspection(loop_to_go)   
    #start filtering the RSS
def news_headline_inspection(loop_to_go):
    banner_check()
    if loop_to_go == 0:
        loging_results_to_file()
        print("loop sayısının sonuna geldik")     
    else:
        #print(loop_to_go)
        loop_to_go = loop_to_go-1
        pyautogui.moveTo(320,190,1)
        pyautogui.click()
        current_news_headline = pyautogui.screenshot(region=(385,196,750,154))
        current_news_headline_rgb = current_news_headline.convert('RGB')
        current_news_headline_grayscale = ImageOps.grayscale(current_news_headline_rgb)
        current_news_headline_inverted = ImageOps.invert(current_news_headline_grayscale)
        current_news_headline_inverted_edge_more = current_news_headline_inverted.filter(ImageFilter.EDGE_ENHANCE_MORE)
        #im = Image.open(current_news_headline_inverted_edge_more)
        #photo = ImageTk.PhotoImage(im)
        current_headline_text = pytesseract.image_to_string(current_news_headline_inverted_edge_more)
        current_headline_text = current_headline_text.replace("'",' ')
        current_headline_text = current_headline_text.replace(",",' ')
        current_headline_text = current_headline_text.replace(":",' ')
        current_headline_text = current_headline_text.replace("’",' ')
        current_headline_text = current_headline_text.replace("‘",' ')
        wordhunt_function_returned_state = wordHunt(current_headline_text)
        if wordhunt_function_returned_state:
            pyautogui.press('j')
            #print('marked:read')
            forbidden_word_counter.set(forbidden_word_counter.get() + 1)
        else:
            pyautogui.press('m')
            #news_marked_as_undread_count += 1
            pyautogui.press('j')
        pyautogui.moveTo(1080,190,1.2)
        pyautogui.click()
        read_RSS_counter.set(read_RSS_counter.get() + 1)
        highlight_label.configure(text='Toplam '+str(num.get())+' haberden '+str(read_RSS_counter.get())+
                                ' incelendi ve '+str(forbidden_word_counter.get())+ ' yasaklı kelime bulundu.'  )
        root.update()
        news_headline_inspection(loop_to_go)
        
def wordHunt(text):
    if len(text) == 0:
        return False
    else:
        text_lower = text.lower()
    news_headline = text_lower.split('\n\n')
    news_headline_singleline = news_headline[0]
    news_headline_singleline = news_headline_singleline.replace("\n", " ")
    #print(news_headline_singleline)
    news_headline_words = news_headline_singleline.split()
    for words in forbidden_words:
        for wantedWord in news_headline_words:
            if words == wantedWord:
                #print('buldum :' + words)
                found_word_list.append(words)
                return True        
def banner_check():
    adblock_detected_location = pyautogui.locateOnScreen('adblock_detected.png')
    #pyautogui.scroll(-10)
    if adblock_detected_location == None:
        pyautogui.moveTo(320,190)
    else:
        for i in range(4):
            pyautogui.press('down')
        maybe_next_time_location = pyautogui.locateOnScreen('maybe_next_time.png')
        maybe_next_time_button = pyautogui.center(maybe_next_time_location)
        pyautogui.moveTo(maybe_next_time_button[0], maybe_next_time_button[1], 1)
        pyautogui.click()

#logging analysis results to a text file
def loging_results_to_file():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    write_date=open('rsslog.txt','a')
    write_date.write('\n')
    write_date.write('--------------------------------\n')
    write_date.write(dt_string)
    write_date.write('\n')
    news_marked_as_undread_count = num.get() - forbidden_word_counter.get()
    write_date.write('reviewed total news headlines :' + str(num.get()))
    write_date.write('\n')
    write_date.write('news marked as unread count :'+ str(news_marked_as_undread_count))
    write_date.write(' \n')
    write_date.write('found word count :' + str(forbidden_word_counter.get()))
    write_date.write('\n')
    write_date.close()
    with open('rsslog.txt', 'a') as f:
        for item in found_word_list:
            f.write("%s " % item)
#all results logged to a text file

#Create the GUI
root = Tk()
root.title('RSS_Filter')
root.geometry('400x110')
    #Adding Entry Widget
entry_widget_label = ttk.Label(text='İncelenecek RSS Sayısı:')
entry_widget_label.grid(row =0, column = 0,sticky ='E')
check_num_wrapper = (root.register(check_num), '%P')
num = IntVar()
unreadNewsparameter = ttk.Entry(root,width=4, textvariable=num, validate='key',validatecommand=check_num_wrapper)
unreadNewsparameter.grid(row =0, column = 1,sticky ='W')
    #Adding a Button
start_button = ttk.Button(root, text="İncelemeye Başla",command=start)
start_button.grid(row =1, column = 0,columnspan = 2)
    #Adding Remaining RSS label Widget
inspected_RSS_label = ttk.Label(text='İncelenen RSS Sayısı : ')
inspected_RSS_label.grid(row =2, column = 0,sticky ='E')
    #Adding Read RSS Counter Widget
read_RSS_counter = IntVar()
read_RSS_counter_label = ttk.Label( textvar=read_RSS_counter)
read_RSS_counter_label.grid(row =2, column = 1,sticky ='W')
    #Adding forbidden word counter label Widget
found_word_count_label = ttk.Label(text='Bulunan yasaklı kelime sayısı : ')
found_word_count_label.grid(row =3, column = 0,sticky ='E')
    #Adding forbidden word counter label Widget
forbidden_word_counter = IntVar()
forbidden_word_counter_label = ttk.Label( textvar=forbidden_word_counter)
forbidden_word_counter_label.grid(row =3, column = 1,sticky ='W')

    #Add new headline label
highlight_label = ttk.Label(text='Toplam 0 haberden 0 incelendi ve 0 yasaklı kelime bulundu.')
highlight_label.grid(row =4, column = 0,sticky ='E',columnspan = 2)

#photo_label = ttk.Label(root, image=photo)
#photo_label.grid(row =5, column = 0)
    #start GUI
root.mainloop()