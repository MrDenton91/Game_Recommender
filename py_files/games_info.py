

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd


DRIVER_PATH = 'C:\\Users\\Nick\\Documents\\Python Scripts\\chromedriver'

def getting_every_game(system):

    # want this to bbe in wodowless mode, can change with Headless
    options = Options()
    options.headless = True
    options.add_argument("--test-type")
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options = options, executable_path = DRIVER_PATH) 
    baseURL = 'https://www.metacritic.com/browse/games/release-date/available/ps4/metascore'
    #driver.get(baseURL) 

    title = []
    meta_score = []
    summary = []
    description_list = []
    user_score =[]
    release_date = []


    df = pd.read_csv(system+"game_urls.csv")
    meta_urls = df['meta_url']
    for url in meta_urls:
        url = url + '/details'
        try:
            driver.get(url)
            driver.implicitly_wait(1)

            try:
            #title
                game_title = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/a/h1')
                
                # score
                me_score = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/div[1]/div/div/a/div/span')
                
                #summary
                summ = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/span[2]')

                ###################################
                #I'm going to do someabasic cleaning here in the procress, but the cleaning.py will do most of it.
                description = (driver.find_element_by_xpath('//*[@id="main"]/div[4]/table/tbody').text)

                description = description.replace('Rating: ','').replace('Developer:','').replace('Genre(s):','').replace('Number of Online Players:','').replace('official site:','')
                description = description.replace('\n','').replace(',','')
                description = description.lower()
                #####################################
                # User Score
                user = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/div[2]/div/div/a/div')
                
                #Release date
                date =driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/ul/li[2]/span[2]')
                

                title.append(game_title.text)
                meta_score.append(me_score.text)
                summary.append(((summ.text).replace(',','').replace('.','')).lower())
                description_list.append(description)
                user_score.append(user.text)
                release_date.append((date.text).replace(',',''))
                
            except: 
                pass
        except:
            continue
        print('Url: ' + url)
    games_dict = {'Title' :title, 'Meta_score': meta_score, 'Summary':summary,
                    'User_score': user_score, "GamesRelease":release_date,
                    'Descrition' : description_list}
    df = pd.DataFrame(games_dict)
    df.to_csv(system+'_game_data.csv', index= False)
    driver.close()
    pass

#print(title)