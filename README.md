# Movie Review Classifier
This model classifies the movie reviews entered by the audiens into positive or negative opinions.
## Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [pyprind]()
- [os]()
- [re]()
- [nltk]()
- [pickle]()
- [sqlite3]()
- [flask]()
- [wtforms]()

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)
## Dataset
This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. There is additional unlabeled data for use as well. Raw text and already processed bag of words formats are provided.

## Download Data
http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz

## Jupyter Notebooks Code

## prepare_data.ipynb
This notebook involves the data preparation steps, which involves cleaning of data and converting the modified data into csv files.

## movie_review_classifier.ipynb
To apply word-of-bag techniques and to classify the model

## sqlite_setup.ipynb
To setup the database

# Flask Web App code
run the app by using python app.py after navigating to reviewclassifier subdirectory 
