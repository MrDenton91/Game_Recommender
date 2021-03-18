from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from sklearn.linear_model import SGDClassifier
from cleaning import clean_it
from item_reccommender import ItemRecommender

import numpy as np
import re
import pandas as pd

'https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html'
'currently data types for columns'
#Title              object
#Meta_score          int64
#Summary            object
#Developer          object
#Genre              object
#User_score         object
#GamesRelease       object


system = 'ps4_'

data = clean_it(system)
data.set_index('Title', inplace = True)
#X = data['bag_of_words'].to_numpy()
#y = data['Title'].to_numpy()
print(data.head())
print(data.dtypes)

count = CountVectorizer()
count_matrix = count.fit_transform(data['bag_of_words'])
indices = pd.Series(data.index)


rec = ItemRecommender()
count_df = pd.DataFrame(count_matrix.todense(), index=indices.values)

rec.fit(count_df)

print(rec.get_recommendations('GOD OF WAR'))




################################################################
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#count_vect = CountVectorizer(stop_words='english')

#X_test_counts = count_vect.fit_transform(raw_documents=X_test)

#X_train_counts = count_vect.fit_transform(raw_documents=X_train)
#tfidf_transformer = TfidfTransformer(use_idf=False)
#X_test_tfidf = tfidf_transformer.fit_transform(X_test_counts)
#print (X_test_tfidf.shape)

#print ('\nTransforming the test data...\n')
#count_vect = CountVectorizer(stop_words='english')
#X_test_counts = count_vect.fit_transform(raw_documents=X_test)

#tfidf_transformer = TfidfTransformer(use_idf=False)
#X_test_tfidf = tfidf_transformer.fit_transform(X_test_counts)
#print (X_test_tfidf.shape)

#print (X_test_tfidf)
#print (y_train.shape)

#docs_test = X_test

#print ('\nApplying the classifier...\n')
#text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
#                     ('tfidf', TfidfTransformer(use_idf=True)),
#                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
#                      alpha=1e-3, random_state=42, verbose=1)),
#])

#text_clf.fit(X_train, y_train)

#predicted = text_clf.predict(docs_test)


#print (np.mean(predicted == y_test))

#print(metrics.classification_report(y_test, predicted,
#    target_names=X.target_names))