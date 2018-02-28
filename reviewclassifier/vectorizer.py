# Import libraries
from sklearn.feature_extraction.text import HashingVectorizer 
import re 
import os 
import pickle

# Load current working directory
cur_dir = os.path.dirname(__file__) 
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl'), 'rb'))

# Clean and tockenize the text
def tokenizer(text):
	text = re.sub('<[^>]*>', '', text)    
	emos = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text.lower())
	text = re.sub('[\W]+', ' ', text.lower())+ ' '.join(emos).replace('-', '')    
	tokenized = [w for w in text.split() if w not in stop]    
	return tokenized

# Convert tokenized words into vectors
vect = HashingVectorizer(decode_error='ignore',
                         n_features=2**21,
						 preprocessor=None,
						 tokenizer=tokenizer)
