# Fashion MNIST Classification with PyTorch and TensorFlow

This repository contains code for performing image classification on the Fashion MNIST dataset using both PyTorch and TensorFlow.

## Dataset
The Fashion MNIST dataset consists of 70,000 grayscale images of fashion items belonging to 10 categories. Each image is of size 28 x 28 pixels.

## Requirements
- Python 3.x
- PyTorch
- TensorFlow
- TorchVision (for PyTorch)
- Pandas
- NumPy
- Matplotlib
- scikit-learn

## Instructions
1. Import the Fashion MNIST dataset from Kaggle or use `torchvision.datasets.FashionMNIST`.
2. Preprocess the dataset and resize the images to 64 x 64 pixels.
3. Design a neural network for classification using either PyTorch or TensorFlow.
4. Train the model and evaluate its performance using training and testing accuracies.
5. Print the classification report to analyze the performance metrics.

## Results
The script will train the model and display the training and testing accuracies. It will also print the classification report showing precision, recall, and F1-score for each class.