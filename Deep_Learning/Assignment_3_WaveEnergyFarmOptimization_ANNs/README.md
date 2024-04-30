## Assignment 3: Large-scale Wave Energy Farm Optimization Through ML

### Question 1: ANNs with TensorFlow

#### Dataset:
- Utilize the [Wave Energy Converters (WEC) dataset](https://archive.ics.uci.edu/dataset/882/large-scale+wave+energy+farm) from the UCI Machine Learning Repository.
- The dataset contains hundreds of features and total farm power output.
- Focus on predicting the total farm power using TensorFlow and Keras.

#### Tasks:
1. **Data Preparation:**
   - Utilize the WEC_SYDNEY_100.CSV file from the dataset.
   - Read the dataset description carefully for understanding.

2. **Model Development:**
   - Design an Artificial Neural Network (ANN) model using TensorFlow and Keras.
   - Follow the ML pipeline and flow covered in Lecture 10.
   - Train the initial ANN model to predict total farm power.

3. **Hyperparameter Tuning:**
   - Design a second ANN model with three hyperparameters changed.
   - Compare the performance of both models.

### Observations:
- Model 1: Optimizer = Adam, Learning Rate = 0.01, Mean Absolute Error = 0.095
- Model 2: Optimizer = SGD, Learning Rate = 0.001, Mean Absolute Error = 0.105
- Model 1 performed better with the specified hyperparameters, while Model 2 also showed good performance in predicting the Total Power attribute.

### Notebook:
- The notebook file for this assignment is available and attached to this folder named 'Assignment3_WaveEnergyFarmOptimization_ANNs.ipynb'.
