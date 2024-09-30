# Sentiment Analysis using Word Embeddings

## Overview

This project focuses on performing sentiment analysis on movie reviews using word embeddings. The dataset used is "Bag of Words Meets Bags of Popcorn," where the task is to predict the sentiment of movie reviews as positive or negative. The primary objective is to utilize word embeddings, particularly Word2Vec, to convert movie reviews into numerical representations.

## Table of Contents

1. Introduction
2. Objective
3. Tasks
4. Evaluation Criteria
5. Summary
6. Detailed Steps
7. Contributing
8. License

## Introduction

In this project, we aim to perform sentiment analysis on movie reviews by leveraging word embeddings. The dataset provided contains movie reviews labeled as either positive or negative. The project involves exploring the dataset, preprocessing the text data, and training a Word2Vec model to generate word embeddings.

## Objective

The objective of this assignment is to:

- Utilize word embeddings, particularly Word2Vec, to convert movie reviews into numerical representations.
- Predict the sentiment of movie reviews as positive or negative.

## Tasks

The project is divided into the following tasks:

1. **Data Exploration**: Explore the provided dataset to understand its structure, including the format of the reviews and the sentiment labels (positive or negative).
2. **Preprocessing**: Preprocess the text data by removing HTML tags, punctuation, and stopwords. Tokenize the reviews and convert them to lowercase.
3. **Word Embeddings**: Train a Word2Vec model on the preprocessed movie reviews to generate word embeddings. Experiment with different vector dimensions and window sizes to optimize the embeddings.

## Evaluation Criteria

The evaluation criteria for this project include:

- Running the code from your system (Data attached).
- Adding code comments in each step to explain the process.
- Preparing a step-by-step report or presentation (MS Word/PPT) to present your findings and recommendations.

## Summary

The `Sentiment_Analysis_Word_Embeddings_with_Gensim.ipynb` notebook covers the following steps:

1. **Data Exploration**:

   - Load the dataset containing movie reviews and their sentiment labels.
   - Explore the dataset to understand its structure and content.

2. **Preprocessing**:

   - Remove HTML tags, punctuation, and stopwords from the reviews.
   - Tokenize the reviews and convert them to lowercase.
   - Prepare the text data for training the Word2Vec model.

3. **Word Embeddings**:
   - Train a Word2Vec model using the preprocessed movie reviews.
   - Experiment with different vector dimensions and window sizes to optimize the word embeddings.
   - Generate numerical representations of the movie reviews using the trained Word2Vec model.

## Detailed Steps

### Data Exploration

- **Loading the Dataset**: The dataset is loaded into a pandas DataFrame for easy manipulation and exploration.
- **Understanding the Structure**: The dataset contains columns for the review text and the corresponding sentiment label (positive or negative).

### Preprocessing

- **Cleaning the Text**: HTML tags, punctuation, and stopwords are removed from the reviews to ensure that only meaningful words are retained.
- **Tokenization**: The cleaned reviews are tokenized, converting the text into a list of words.
- **Lowercasing**: All words are converted to lowercase to maintain consistency.

### Word Embeddings

- **Training Word2Vec Model**: A Word2Vec model is trained on the preprocessed reviews to generate word embeddings. Different vector dimensions and window sizes are experimented with to find the optimal settings.
- **Generating Numerical Representations**: The trained Word2Vec model is used to convert the movie reviews into numerical representations, which can be used for sentiment analysis.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.
