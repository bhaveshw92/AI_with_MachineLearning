# LSTM Autoencoder for Time Series Signal Regeneration

## Introduction

This assignment focuses on designing and implementing an LSTM-based autoencoder to regenerate the original time series signal. The goal is to develop a deep learning model capable of learning the underlying patterns in the signal and accurately reconstructing it after training.

## Dataset Generation

To generate the dataset, the provided code snippet is used to create 5000 samples of time series signals. Each sample consists of 100 data points, with random variations in frequency and amplitude.

## Instructions

1. **Dataset Generation**: Run the provided code snippet to generate 5000 samples of time series signals.

2. **Model Design**: Design an LSTM-based autoencoder architecture using PyTorch to learn and reconstruct the original time series signals.

3. **Training**: Train the LSTM autoencoder model using the generated dataset to minimize the reconstruction error.

4. **Evaluation**: Evaluate the trained model's performance by comparing the regenerated signals with the original ones.

5. **Visualization**: Visualize the original and reconstructed signals to assess the accuracy of the autoencoder.

## Files Included

- `LSTM_Autoencoder_Time_Series.ipynb`: Jupyter Notebook containing Python code for model implementation, training, and evaluation.
- `README.md`: This README file providing an overview of the assignment, instructions, and guidelines for implementation.

## Conclusion

In completing this assignment, I gained practical experience in developing an LSTM-based autoencoder for time series signal regeneration. By training the model on the generated dataset, I learned how to capture and reconstruct the underlying patterns in the signals using deep learning techniques. Additionally, evaluating the model's performance provided insights into its effectiveness in accurately regenerating the original signals. Overall, this assignment enhanced my understanding of LSTM networks and their applications in signal processing tasks.

## References

- PyTorch Documentation: [https://pytorch.org/docs/stable/index.html](https://pytorch.org/docs/stable/index.html)
- LSTM Autoencoder Tutorial: [https://www.kaggle.com/vincentman0403/lstm-autoencoder-for-anomaly-detection](https://www.kaggle.com/vincentman0403/lstm-autoencoder-for-anomaly-detection)
- Signal Processing with Python: [https://docs.scipy.org/doc/scipy/reference/signal.html](https://docs.scipy.org/doc/scipy/reference/signal.html)
