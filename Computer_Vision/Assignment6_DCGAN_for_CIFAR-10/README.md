# DCGAN for CIFAR-10 Image Generation

## Introduction

In this assignment, we aim to design and implement a Deep Convolutional Generative Adversarial Network (DCGAN) capable of generating CIFAR-10 images. The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. The goal is to train the DCGAN model to learn the underlying distribution of CIFAR-10 images and generate realistic images that resemble the ones in the dataset.

## Instructions

1. **Dataset Download**: Download the CIFAR-10 dataset from the official website or pytorch - torchvision.datasets.CIFAR10

2. **Data Preprocessing**: Preprocess the dataset by resizing the images to a suitable size and normalizing the pixel values.

3. **Model Design**: Design the architecture of the DCGAN model using PyTorch. The generator and discriminator networks should be defined with appropriate layers and activation functions.

4. **Training**: Train the DCGAN model on the preprocessed CIFAR-10 dataset. Use techniques such as mini-batch gradient descent and adversarial training to optimize the model parameters.

5. **Image Generation**: After training, generate CIFAR-10-like images using the trained generator network. Save and visualize the generated images to assess their quality.

6. **Evaluation**: Evaluate the quality of the generated images using visual inspection.

7. **Documentation**: Provide detailed documentation of the model architecture, training procedure, and evaluation results with code comments.

## Files Included

- `DCGAN_CIFAR10.ipynb`: Jupyter Notebook containing Python code for model implementation, training, and evaluation.
- `README.md`: This README file providing an overview of the assignment, instructions, and guidelines for implementation.

## Model Architecture

The DCGAN model consists of two main components: the generator and the discriminator. The generator takes random noise as input and generates fake images, while the discriminator tries to distinguish between real and fake images. Both networks are trained simultaneously in an adversarial manner.

## Conclusion

In completing this assignment, I gained practical experience in designing and training a Deep Convolutional Generative Adversarial Network (DCGAN) for image generation tasks. By working on the CIFAR-10 dataset, I learned how to preprocess image data, define complex neural network architectures, and optimize models using adversarial training techniques. Additionally, evaluating the quality of generated images provided insights into the effectiveness of the DCGAN in capturing and generating realistic image samples.

## References

- DCGAN Paper: [https://arxiv.org/abs/1511.06434](https://arxiv.org/abs/1511.06434)
- PyTorch Documentation: [https://pytorch.org/docs/stable/index.html](https://pytorch.org/docs/stable/index.html)
- CIFAR-10 Dataset: [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)
