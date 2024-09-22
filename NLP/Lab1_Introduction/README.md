# Natural Language Processing (NLP) Projects

This repository contains a collection of NLP exercises and assignments that demonstrate various stages of text processing, sentiment analysis, and text classification using machine learning models. The three key projects are:

1. **Assignment Exercise 1: Preprocessing Twitter Data for NLP Tasks**
2. **Assignment Exercise 2: Sentiment Analysis on YouTube Comments**
3. **Assignment Exercise 3: Naive Bayes Classifier for Text Classification**

## 1. Assignment Exercise 1: Preprocessing Twitter Data for NLP Tasks

### Overview

This project focuses on the data preprocessing stage, specifically cleaning and structuring a dataset of tweets. It prepares the data for future NLP tasks or machine learning models.

### Key Features

- **Dataset**: A CSV file containing tweets.
- **Data Processing**:
  - Loaded and displayed the dataset for initial inspection.
  - Exported the processed data into a new CSV file with tabular formatting.

### How to Run

Run the notebook `Assignment_Exercise1_NLP.ipynb` in Jupyter to load and process the tweets dataset.

### Output

A new CSV file with the cleaned and formatted tweet data.

---

## 2. Assignment Exercise 2: Sentiment Analysis on YouTube Comments

### Overview

This project involves cleaning and preparing YouTube video comments for sentiment analysis. The focus is on text preprocessing techniques to prepare the data for analysis or model training.

### Key Features

- **Dataset**: YouTube comments dataset.
- **Text Cleaning**:
  - Removed unwanted characters using regular expressions.
  - Normalized text using Unicode.
  - Removed stopwords using NLTK.

### How to Run

Run the notebook `Assignment_Exercise2_NLP.ipynb` in Jupyter to clean the YouTube comments and prepare the dataset for sentiment analysis.

### Output

A cleaned dataset ready for sentiment analysis, which can be used in future NLP tasks.

---

## 3. Assignment Exercise 3: Naive Bayes Classifier for Text Classification

### Overview

In this project, a Naive Bayes classifier is implemented to classify texts from the `20 Newsgroups` dataset. The goal is to categorize news articles into different groups using machine learning.

### Key Features

- **Dataset**: `fetch_20newsgroups` dataset from `scikit-learn`.
- **Text Classification**:
  - Trained a Naive Bayes classifier on the dataset to predict text categories.
  - Explored the number of unique categories and evaluated the classifier's performance.

### How to Run

Run the notebook `Assignment_Exercise3_NLP.ipynb` in Jupyter to train the Naive Bayes classifier on the dataset and evaluate the results.

### Output

A trained Naive Bayes model that classifies texts into different categories, along with evaluation metrics such as accuracy.

---
