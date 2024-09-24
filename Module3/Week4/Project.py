import numpy as np
import pandas as pd

# load data

data = pd.read_csv('D:/Homework/Module3/Week4/IMDB-Dataset.csv')

### preprocessing Exploratory
# remove duplicates
data = data.drop_duplicates()

# remove stopword'k
import re
import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
import contractions

stop = set(stopwords.words('english'))

# expanding contractions

def expand_contractions(text):
    return contractions.fix(text)

# Function to clean data

def preprocess_text(text):

    wnl = WordNetLemmatizer()
    soup = BeautifulSoup(text, 'html.parser') #remove HTML Tag
    text = soup.get_text()
    text = expand_contractions(text)
    emoji_clean = re.compile("["
                            u'\U0001F600-\U0001F64F' #emotinons
                            u'\U0001F300-\U0001F5FF' #symboys & pictographs
                            u'\U0001F680-\U0001F6FF' #transport & map symbos
                            u'\U0001F1E0-\U0001F1FF' #Flags
                            u'\U00002702-\U000027B0' #emotinons
                            u'\U000024C2-\U0001F251' #emotinons
                            "]+", flags = re.UNICODE)
    text = emoji_clean.sub(r'', text)
    text = re.sub(r'\.(?=\S)','. ', text) # add space after full stop
    text = re.sub(r'http\S+', '', text) # remove URLS
    text = "".join([
        word.lower() for word in text if word not in string.punctuation
    ]) #remove punctuation and make text lowercase
    text = " ".join([
        wnl.lemmatize(word) for word in text.split() if word not in stop and word.isalpha()
    ])# remove stopword and return word to origin
    return text

## text Encoding
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

X_data = data['review']
y_data = data['sentiment']
# print(X_data.describe())
# print(y_data.describe())
X_train,X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state= 42)

# TF-IDF vectorizer
tfidf_V = TfidfVectorizer(max_features=1000)
tfidf_V.fit(X_train, y_train)

X_train_encoded = tfidf_V.transform(X_train)
X_test_encoded = tfidf_V.transform(X_test)

# print(X_train_encoded.shape)
# print(y_train.describe())
### Clasifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# # Decision tree maxdepth = 5
dt_classifier = DecisionTreeClassifier(
    max_depth = 5,
    criterion = 'entropy',
    random_state= 42
)
dt_classifier.fit(X_train_encoded, y_train)
y_pred = dt_classifier.predict(X_test_encoded)
print(accuracy_score(y_pred, y_test))
# # Decision tree
dt_classifier = DecisionTreeClassifier(
    criterion = 'entropy',
    random_state= 42
)
dt_classifier.fit(X_train_encoded, y_train)
y_pred = dt_classifier.predict(X_test_encoded)
print(accuracy_score(y_pred, y_test))

## randomforest
rf_classifier = RandomForestClassifier(
    n_estimators = 100, max_depth = 5, max_features = 'sqrt', bootstrap = True, random_state = 42
)
rf_classifier.fit(X_train_encoded, y_train)
y_pred = rf_classifier.predict(X_test_encoded)
print(accuracy_score(y_pred, y_test))
## Adaboost
adb_classifier = AdaBoostClassifier(
    n_estimators = 100, random_state = 42
)
adb_classifier.fit(X_train_encoded, y_train)
y_pred = adb_classifier.predict(X_test_encoded)
print(accuracy_score(y_pred, y_test))
## Gradient Boosting
gb_classifier = GradientBoostingClassifier(
    n_estimators = 100, random_state = 42
)
gb_classifier.fit(X_train_encoded, y_train)
y_pred = gb_classifier.predict(X_test_encoded)
print(accuracy_score(y_pred, y_test))
## XGBoosing
XGB_classifier = XGBClassifier(n_estimators = 100)
XGB_classifier.fit(X_train_encoded, y_train)
y_pred = XGB_classifier.predict(X_test_encoded)
print(accuracy_score(y_pred, y_test))

## Inference
example_encoded = tfidf_V.transform(df['review'][:2])
example_pred = dt_classifier.predict(example_encoded)
