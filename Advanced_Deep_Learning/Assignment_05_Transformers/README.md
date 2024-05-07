# Assignment: Sentiment Analysis using Transformers

This repository contains code for performing sentiment analysis on the Tweets dataset using transformers library in Python.

## Dataset

The Tweets.csv dataset is used for this assignment. The dataset contains tweets labeled with three classes: positive, negative, and neutral. To make it a binary dataset, the neutral class has been removed.

## Methodology

1. **Transfer Learning using Pipeline**: The `pipeline` function from the transformers library is used for transfer learning. The default model used is `distilbert-base-uncased-finetuned-sst-2-english`.

2. **Fine-tuning**: Fine-tuning is performed by training the transformer model for 5 epochs. The `distilbert-base-uncased` checkpoint is used, as it trains faster.

## Instructions

1. Use the Tweets.csv dataset provided.
2. Remove the neutral class from the dataset to make it binary.
3. Implement transfer learning using the pipeline function for transformers.
4. Perform fine-tuning by training the transformer model for 5 epochs.
5. Compare the results of transfer learning with fine-tuning.

## Results

The scripts will perform sentiment analysis using transformers and display the results for both transfer learning and fine-tuning.

