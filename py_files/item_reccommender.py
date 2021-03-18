  
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

class ItemRecommender():
    '''
    Content based item recommender
    '''
    def __init__(self, similarity_measure=None):
        self.similarity_matrix = None
        self.item_names = None

        if similarity_measure == None:
            self.similarity_measure = cosine_similarity
        else:
            self.similarity_measure = similarity_measure

    
    def fit(self, X, titles=None):
        '''
        Takes a numpy array of the item attributes and creates the similarity matrix
        INPUT -
            X: NUMPY ARRAY - Rows are items, columns are feature values / or DF
            titles: LIST - List of the item names/titles in order of the numpy arrray
        
        OUTPUT - None
        Notes:  You might want to keep titles and X as attributes to refer to them later
        Create the a similarity matrix of item to item similarity
        '''

      
        
        if isinstance(X, pd.DataFrame):
            self.item_counts = X
            self.item_names = X.index
            self.similarity_df = pd.DataFrame(self.similarity_measure(X.values, X.values),
                 index = self.item_names)
        else:
            self.item_counts = X
            self.similarity_df = pd.DataFrame(self.similarity_measure(X, X),
                 index = titles)
            self.item_names = self.similarity_df.index

        
    def get_recommendations(self, item, n=5):
        '''
        Returns the top n items related to the item passed in
        INPUT:
            item    - STRING - Name of item in the original DataFrame 
            n       - INT    - Number of top related items to return 
        OUTPUT:
            items - List of the top n related item names
        For a given item find the n most similar items to it (this can be done using the similarity matrix created in the fit method)
        '''
        return self.item_names[self.similarity_df.loc[item].values.argsort()[-(n+1):-1]].values[::-1]
