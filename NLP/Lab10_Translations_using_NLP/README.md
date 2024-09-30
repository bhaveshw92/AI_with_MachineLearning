# Natural Language Processing with LSTMs and Attention Mechanism

This repository contains a collection of tutorials, lecture notes, and ipynb Notebooks focused on using Translations for Natural Language Processing (NLP).

## Contents

### 1. English to French Translation using LSTMs

## Overview

This Jupyter Notebook demonstrates how to perform English to French translation using a sequence-to-sequence model with Long Short-Term Memory (LSTM) networks. The notebook is based on the concepts and code provided in the Keras blog and official Keras examples.

## Table of Contents

1. Introduction
2. Prerequisites
3. Usage
4. Summary
5. Exercises
6. Contributing
7. License

## Introduction

The `English_to_French_Translation_using_LSTMs.ipynb` notebook is part of a series of lab exercises aimed at enhancing your understanding of sequence-to-sequence learning using LSTM networks. This particular notebook focuses on building a model to translate English sentences to French.

Exercise 1: English sentences to French translation using LSTM
sequence-to-sequence (Content): https://blog.keras.io/a-ten-minuteintroduction-to-sequence-to-sequence-learning-in-keras.html
Code: https://keras.io/examples/nlp/lstm_seq2seq/

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed Jupyter Notebook.

## Usage

To use this notebook, follow these steps:

1. Clone the repository or download the notebook file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the notebook file.
4. Start Jupyter Notebook.
5. In the Jupyter Notebook interface, open `English_to_French_Translation_using_LSTMs.ipynb`.

## Summary

The `English_to_French_Translation_using_LSTMs.ipynb` notebook covers the following topics:

- **Data Preparation**: Loading and preprocessing the dataset for training the model.
- **Model Architecture**: Building the sequence-to-sequence model using LSTM layers.
- **Training**: Training the model on the dataset.
- **Inference**: Using the trained model to translate English sentences to French.
- **Evaluation**: Evaluating the performance of the model on test data.

### Detailed Steps:

1. **Data Preparation**:

   - Load the dataset containing English-French sentence pairs.
   - Preprocess the data by tokenizing the sentences and padding them to a fixed length.
   - Create input and output sequences for the encoder and decoder.

2. **Model Architecture**:

   - Define the encoder model using LSTM layers.
   - Define the decoder model using LSTM layers and a dense layer with softmax activation.
   - Compile the model with appropriate loss function and optimizer.

3. **Training**:

   - Train the model using the prepared dataset.
   - Monitor the training process using validation data.

4. **Inference**:

   - Define the inference models for the encoder and decoder.
   - Implement a function to translate English sentences to French using the trained model.

5. **Evaluation**:
   - Evaluate the model's performance on a test set.
   - Calculate metrics such as accuracy and BLEU score to assess the quality of translations.

## Exercises

The notebook includes the following exercises:

1. **Exercise 1**: Modify the model architecture to improve translation accuracy.
2. **Exercise 2**: Experiment with different hyperparameters and observe their impact on model performance.
3. **Exercise 3**: Extend the notebook to support translation from French to English.

Each exercise is designed to be self-contained and includes detailed instructions and code snippets to help you complete the tasks.

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

---

### 2. Spanish-to-English Translation using Attention Mechanisms

## Overview

This Jupyter Notebook demonstrates how to train a sequence-to-sequence model for Spanish-to-English translation using attention mechanisms. The notebook is roughly based on the paper "Effective Approaches to Attention-based Neural Machine Translation" by Luong et al., 2015, and follows the tutorial provided by TensorFlow.

## Table of Contents

1. Introduction
2. Prerequisites
3. Usage
4. Summary
5. Exercises
6. Contributing
7. License

## Introduction

The `Spanish_to_English_using_Attention_Mechanisms.ipynb` notebook is part of a series of lab exercises aimed at enhancing your understanding of sequence-to-sequence learning with attention mechanisms. This particular notebook focuses on building a model to translate Spanish sentences to English.

Exercise 2: Tutorial to demonstrate how to train a sequence-tosequence model for Spanish-to-English translation roughly based on
Effective Approaches to Attention-based Neural Machine Translation
(Luong et al., 2015).
https://www.tensorflow.org/text/tutorials/nmt_with_attention

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed Jupyter Notebook.

## Usage

To use this notebook, follow these steps:

1. Clone the repository or download the notebook file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the notebook file.
4. Start Jupyter Notebook.
5. In the Jupyter Notebook interface, open `Spanish_to_English_using_Attention_Mechanisms.ipynb`.

## Summary

The `Spanish_to_English_using_Attention_Mechanisms.ipynb` notebook covers the following topics:

- **Data Preparation**: Loading and preprocessing the dataset for training the model.
- **Model Architecture**: Building the sequence-to-sequence model with attention mechanisms.
- **Training**: Training the model on the dataset.
- **Inference**: Using the trained model to translate Spanish sentences to English.
- **Evaluation**: Evaluating the performance of the model on test data.

### Detailed Steps:

1. **Data Preparation**:

   - Load the dataset containing Spanish-English sentence pairs.
   - Preprocess the data by tokenizing the sentences and padding them to a fixed length.
   - Create input and output sequences for the encoder and decoder.

2. **Model Architecture**:

   - Define the encoder model using LSTM layers.
   - Implement the attention mechanism to focus on relevant parts of the input sequence.
   - Define the decoder model using LSTM layers and a dense layer with softmax activation.
   - Compile the model with appropriate loss function and optimizer.

3. **Training**:

   - Train the model using the prepared dataset.
   - Monitor the training process using validation data.

4. **Inference**:

   - Define the inference models for the encoder and decoder.
   - Implement a function to translate Spanish sentences to English using the trained model.

5. **Evaluation**:
   - Evaluate the model's performance on a test set.
   - Calculate metrics such as accuracy and BLEU score to assess the quality of translations.

## Exercises

The notebook includes the following exercises:

1. **Exercise 1**: Modify the model architecture to improve translation accuracy.
2. **Exercise 2**: Experiment with different hyperparameters and observe their impact on model performance.
3. **Exercise 3**: Extend the notebook to support translation from English to Spanish.

Each exercise is designed to be self-contained and includes detailed instructions and code snippets to help you complete the tasks.

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
