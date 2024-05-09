# Lipreading AI Tool - LipNet AI

## Project Overview

### Goal
The project aims to develop a lip reading machine learning model capable of deciphering lip movements and converting them into text. The objective is to assist individuals with hearing impairments in understanding spoken language through visual cues.

### Objective
- Develop a data preprocessing pipeline to extract relevant features from video data.
- Design and implement a deep learning model architecture to decode lip movements accurately.
- Train the model on 1 speaker dataset to achieve high accuracy in lip reading.
- Evaluate the model's performance and implement a Streamlit application to present the model.

## Implementation Details

### Libraries Used
- OpenCV
- TensorFlow
- cv2
- Matplotlib
- Imageio
- gdown
- NumPy
- Streamlit

### Dataset
The GRID Audiovisual Sentence Corpus dataset is used, containing audio and video recordings of 34 speakers uttering over 1000 sentences. Only data from one speaker is considered for training.

### Video and Alignment Preprocessing
- Load_Video Function: Converts the video into frames and captures the lip section using a static slicer.
- Load_Alignments Function: Loads alignments with vocabulary and converts characters to numerical values.
- Load_Data Function: Simultaneously loads video frames and alignments.
- Save as GIF: Combines frames from the video into a GIF for visualization.

### Data Pipeline Creation
- TensorFlow's Dataset API is used to construct an efficient data pipeline.
- Data Extraction: Extract data from the folder with an extension of .mpg.
- Shuffle: Randomizes the order of elements in the dataset.
- Padding: Pads each alignment and frame to a standard length.
- Preloading: Preloads data when the ML model is learning.

### Model Architecture
- The lip reading model comprises 3D convolutional layers, LSTM layers, and Dense layers.
- 3D Convolutional Layers: Extract spatial and temporal features.
- LSTM Layers: Capture temporal dependencies and sequence information.
- Dense Layers: Predict characters based on extracted features.
- Utilizes Connectionist Temporal Classification (CTC) loss function for sequence-to-sequence mapping tasks.

### Training Process
- Model Compilation: Compiled with the Adam optimizer and custom CTC loss function.
- Callbacks: ModelCheckpoint and LearningRateScheduler employed during training.
- Training Epochs: Trained for 50 epochs.
- Evaluation: Model performance evaluated using the testing dataset.

## Conclusion and Learnings
- Implemented a lip reading AI model using deep learning techniques.
- Utilized TensorFlow's Dataset API for efficient data processing.
- Learned about 3D convolutional layers, LSTM layers, and Dense layers for sequence prediction tasks.
- Gain insights into Connectionist Temporal Classification (CTC) loss function for sequence mapping.
- Trained the model on a GPU, with training taking approximately 10 hours.
- Developed a Streamlit application to interactively predict lip movements based on selected video files.

## Note
- I have only attached 19 video and its respective alignments to the github folder the entire dataset can be found GRID Corpus website.

## References
- Video Reference: [YouTube](https://www.youtube.com/watch?v=uKyojQjbx4c&t=3607s)
- Original Paper: [arXiv](https://arxiv.org/abs/1611.01599)
- Associated Code for Paper: [GitHub](https://github.com/rizkiarm/LipNet)
- Dataset: [GRID Corpus](https://spandh.dcs.shef.ac.uk/gridcorpus/)
- Code Reference: [GitHub](https://github.com/nicknochnack/LipNet)
- ARS Tutorial: [Keras Documentation](https://keras.io/examples/audio/ctc_asr/#model)
- AI Tool: [OpenAI Chat](https://chat.openai.com/)

