
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


DRIVER_PATH = 'C:\\Users\\Nick\\Documents\\Python Scripts\\chromedriver'

### For testing 
#baseURL = 'https://www.metacritic.com/browse/games/release-date/available/ps4/metascore'
#driver.get(baseURL) 

def game_collecting(system):

    
# want this to bbe in wodowless mode, can change with Headless
    options = Options()
    options.headless = True
    options.add_argument("--test-type")
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options = options, executable_path = DRIVER_PATH) 

    main_urls = {'ps4': 'https://www.metacritic.com/browse/games/release-date/available/ps4/metascore?page=',
                'xbox_one': 'https://www.metacritic.com/browse/games/release-date/available/xboxone/metascore?page=',
                'switch': 'https://www.metacritic.com/browse/games/release-date/available/switch/metascore?page=',
                'pc': 'https://www.metacritic.com/browse/games/release-date/available/pc/metascore?page=',
                'xbox_series_x': 'https://www.metacritic.com/browse/games/release-date/available/xbox-series-x/metascore?page=',
                'ps5': 'https://www.metacritic.com/browse/games/release-date/available/ps5/metascore?page=' 
                }

    #soup = BeautifulSoup(driver.page_source, 'lxml')
    base_url = main_urls[system]
    game_url = []

    for k in range(0,26):
        url = base_url + str(k)
        driver.get(url)
        #driver.implicitly_wait(3)
            ## grabs every Url for each game in at metacritic website page .
        for i in range(8):
            for j in range(170):
                try:   
                    thing = driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/div/div[1]/div/div['+str(i) +']/table/tbody/tr[' + str(j) +']/td[2]/a')
                    #print(thing.get_attribute('href'))
                    meta_url = thing.get_attribute('href').replace(' ','').replace('\n','')
                    
                    meta_url = ''.join(meta_url)
                    game_url.append(meta_url)

                except:
                    pass
            print(i)
        print('Page' + str(k))



    # I expect to see 2536 games listed for the ps4 there will be 26 pages of content
    print(len(game_url))

    dict = {'meta_url': game_url}

    df = pd.DataFrame(dict)
    df.to_csv(system +'_game_urls.csv', index= False)
    driver.close()
    pass