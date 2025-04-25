# Sentiment Analysis of Customer Reviews
Natural Language Processing | Machine Learning | Streamlit Deployment

Welcome! This project uses Natural Language Processing (NLP) techniques to classify customer reviews as either positive or negative. It includes data preprocessing, model experimentation, and deployment through a Streamlit web application.

You can try the model here:
https://km-sentiment-analysis.streamlit.app/

## Project Overview
Goal: Classify the sentiment of customer reviews using machine learning.

Dataset: Pre-labeled customer reviews with binary sentiment labels (positive or negative).

## Approach

Text cleaning & preprocessing (tokenization, stopword removal, lemmatization)

Text vectorization using TF-IDF

Model building with several ML algorithms

Evaluation using accuracy and F1 score

Deployment via Streamlit for real-time prediction

## Models Explored
Random Forest

Naive Bayes

Support Vector Machine (SVM)

Voting Classifier (Best-performing)

The Voting Classifier gave the best results as it leverages the strengths of multiple models, leading to better generalization, especially for real-world text inputs.

## Technologies Used
Python

Pandas, Numpy

NLTK

Scikit-learn

Jupyter Notebook

## Streamlit (for deployment)
👉 https://km-sentiment-analysis.streamlit.app/

Paste in any customer review and get instant feedback on whether the sentiment is positive or negative.
