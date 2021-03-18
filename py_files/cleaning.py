import pandas as pd
import numpy as np


def clean_it(system):

    data = pd.read_csv(system+'game_data.csv')
    data = data[data.User_score != 'tbd']
    #data.set_index('Title', inplace =True)


    # Need to convert and collect evrything into one thing
    #data['word_bag'] = ''

    ############################
    # Need to clean up summary and descriptino list before doing a word Bag
    ##
    summary = data['Summary'].tolist()
    game_list = []
    for game in summary:
        game = game.replace(',','').replace(':','').replace(';','').replace('[','').replace(']','').replace('(','').replace(')','').replace('.','')
        games = game.lower()
        game_list.append(games)
    arr = np.array(game_list)
    data.drop(columns = ['Summary'], inplace= True)
    data['Summary'] = arr

    descripton = data['Descrition'].tolist()
    des_list = []
    for des in descripton:
        des = des.replace('official site:','').replace(' http://www.',' ').replace('.com/','')
        des_list.append(des)
    dess = np.array(des_list)
    data.drop(columns = ['Descrition'], inplace = True)
    data['Descrition'] = dess



    columns = data.columns
    data['bag_of_words'] = ''
    for index, row in data.iterrows():
        words = ''
        for col in columns:
            
            words += ''.join(str(row[col]))+ ' '
        data['bag_of_words'][index] = words    

    data.drop(columns = ['Meta_score','Summary','User_score','GamesRelease','Descrition'], inplace = True)


    return data
