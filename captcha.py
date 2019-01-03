from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
import time

def googlesignin():
    
    
    print(Fore.RED + ('\n' + '\n'))
    print(Fore.RED + ('WELCOME TO THE CAPTCHA ASSISTANT TOOL BY @THENORTHCOP'))
    print(Fore.RED + ('/////////////////////////////////////////////////////' + '\n' + '\n'))
    

    accounts = open('accounts.txt', 'r').readlines()
    for userpass in accounts:
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--no-sandbox')
        options.add_argument("--incognito")
        #options.add_argument("--headless")
        browser = webdriver.Chrome(options= options, executable_path=r'chromedriver.exe')
        browser.minimize_window()
        browser.get("https://accounts.google.com/signin/v2/identifier?hl=EN&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        
        
    
        gmailusername = userpass.split(',')[0]
        gmailpassword = userpass.split(',')[1]
    
        if '@gmail.com' in gmailusername:
    
            print(Fore.BLUE + 'Signing in with account username {} and password {}'.format(gmailusername,gmailpassword))
    
            print(Fore.BLUE + ("Signing into your google account"))
        
            time.sleep(3)
            
            GmailBox = browser.find_element_by_id("identifierId")
            GmailBox.send_keys(gmailusername)
    

            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(2)

            pw = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located(('xpath','//*[@id="password"]/div[1]/div/div[1]/input')))
        
            pw.send_keys(gmailpassword)
            
            time.sleep(7)
            checkurl = browser.current_url
            print (checkurl)
           
            
            if 'myaccount.google.com' in checkurl:
                print(Fore.GREEN + ("Succesfully Logged in to google!"))
        
            else:
                print(Fore.RED + ('There was an error signing in, please check your account username / password or your internet connection and try again.'))
                exit()
                
            time.sleep (3)

            time.sleep(2)
        
            print(Fore.RED + 'Now watching a dank meme compilation')

            browser.get("https://www.youtube.com/watch?v=jk-xUMvXvwk")
            time.sleep(700)
    
            print(Fore.GREEN + 'Finished Watching Youtube!' + '\n')
            
            print(Fore.RED + 'Now generating searches' + '\n')
    
            searchlist = open('Searchlist.txt', 'r').readlines()
    
            for each in searchlist:
                print('searching for {}'.format(each))
                browser.get('https://www.google.com/search?q={}&rlz=1C1CHBF_enCA811CA811&oq={}&aqs=chrome..69i57j69i60j0j69i60l2j0.729j0j4&sourceid=chrome&ie=UTF-8'.format(each,each))
                time.sleep(1)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
       
        
                print(Fore.GREEN + 'Finished Generating Searches!' + '\n')
    
                print(Fore.GREEN + 'Finished Generating 1 clicks for {}!'.format(gmailusername))
    
            browser.delete_all_cookies()
            time.sleep(5)
            browser.close()

        else:
            print ('please submit a gmail account')
            
    print(Fore.GREEN + 'Finished Generating 1 clicks for all accounts!')
        
googlesignin()
