# Import required libraries
from flask import Flask, render_template, request
from wtforms.form import Form
from wtforms import TextAreaField, validators
from wtforms.validators import DataRequired, Length
from forms import ReviewForm
import os
import pickle
import numpy as np

# Load the vectorizer script file
from vectorizer import vect


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# Unpickle and set up the classification model
current_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(current_dir,
                                    'pkl_objects/classifier.pkl'), 'rb'))

def classify(file):
	label = {0:'negative',
	         1:'positive'}
	X = vect.transform([file])
	y = clf.predict(X)[0]
	return label[y], np.max(clf.predict_proba(X))

# Train classification model
def train(file, y):
	X = vect.transform([file])
	clf.partial_fit(X, [y])

@app.route('/')
def index():
	form = ReviewForm()
	return render_template('index.html', form=form)

@app.route('/outcomes', methods=['POST', 'GET'])
def outcomes():
	form = ReviewForm()
	if request.method == 'POST' and form.validate():
		review = form.review.data
		y, proba = classify(review)
		return render_template('outcomes.html',
	content=review,
	prediction=y,
	probability=round(proba*100, 2), form=form)
	return render_template('outcomes.html', form=form)



if __name__ == '__main__':
	app.run(debug=True) # Turn debug to True while debugging


