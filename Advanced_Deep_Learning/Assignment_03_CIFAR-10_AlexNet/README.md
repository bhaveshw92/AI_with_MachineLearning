# Transfer Learning with AlexNet on CIFAR-10 Dataset

This repository contains code for performing transfer learning with AlexNet on the CIFAR-10 dataset using both PyTorch and TensorFlow.

## Dataset
The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. The classes are: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck.

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
1. Import the CIFAR-10 dataset from Kaggle or use `torchvision.datasets.CIFAR10`.
2. Perform transfer learning by fine-tuning the pre-trained AlexNet model.
3. Evaluate the model's performance using training and testing accuracies.
4. Print the classification report to analyze the performance metrics.

## Results
The script will train the model, evaluate its performance, and display the training and testing accuracies. It will also print the classification report showing precision, recall, and F1-score for each class.

