# Intel Image Classification with Transfer Learning

This project aims to classify images into six different categories using transfer learning with pretrained models such as ResNet50, AlexNet, and VGG16. The dataset used for this project contains approximately 25,000 images grouped into categories including buildings, forests, glaciers, mountains, seas, and streets. The data was initially published by Intel on [Analytics Vidhya](https://datahack.analyticsvidhya.com) for an image classification challenge.

![Image](https://images.unsplash.com/photo-1487073947834-59f68f2647c4)

## Dataset Details

- **Dataset Source:** [Intel Image Classification Dataset](https://www.kaggle.com/datasets/puneet6060/intel-image-classification/data)
- **Number of Images:** 
  - Training: 14,000 images
  - Validation: 3,000 images
  - Testing: 7,000 images

## Pretrained Models and Classes

Three pretrained models are used for transfer learning:
1. ResNet50
2. AlexNet
3. VGG16

The classes for classification are:
- 'buildings' (0)
- 'forest' (1)
- 'glacier' (2)
- 'mountain' (3)
- 'sea' (4)
- 'street' (5)

## Model Performance

### ResNet50 Model
- Training Accuracy: 98.12%
- Testing Accuracy: 96.88%

#### Accuracy on Validation Dataset
- Buildings: 90%
- Forest: 98%
- Glacier: 80%
- Mountain: 92%
- Sea: 93%
- Street: 94%

#### Accuracy on Testing Dataset
- Buildings: 84%
- Forest: 99%
- Glacier: 79%
- Mountain: 91%
- Sea: 95%
- Street: 94%

### AlexNet Model
- Accuracy on Validation Images: 89.01%

#### Accuracy on Testing Images
- Buildings: 78%
- Forest: 97%
- Glacier: 79%
- Mountain: 91%
- Sea: 85%
- Street: 97%

### VGG16 Model
- Accuracy on Validation Images: 92.17%

#### Accuracy on Testing Images
- Buildings: 86%
- Forest: 99%
- Glacier: 86%
- Mountain: 84%
- Sea: 97%
- Street: 96%

## Unseen Data Prediction

Each model is tested on unseen data from the 'seg_pred' folder, and the output is visualized.

## Conclusion

Transfer learning using pretrained models significantly improves image classification accuracy, with VGG16 demonstrating the highest performance among the models evaluated.

