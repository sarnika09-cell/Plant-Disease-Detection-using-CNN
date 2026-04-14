# Plant-Disease-Detection-using-CNN

## Overview

Plant diseases significantly affect agricultural productivity and crop yield. Early detection is essential to minimize losses.

This project uses a Convolutional Neural Network (CNN) to automatically classify plant leaf images into different disease categories using the PlantVillage dataset.

## Features
- Image-based plant disease classification
- Multi-class prediction (healthy and diseased leaves)
- Deep learning using CNN
- Confusion matrix for evaluation
- Works on unseen test images

## Dataset
The dataset used is the PlantVillage dataset, which contains labeled images of plant leaves.

- Type: Image dataset  
- Classes: Multiple categories including Tomato, Potato, and Pepper diseases along with healthy leaves  
- Structure: Images are organized into class-specific folders 

Dataset is not included due to size limitations.

get it from:
[https://www.kaggle.com/datasets/emmarex/plantdisease](https://drive.google.com/drive/folders/1nuOswgZP-DePt-4fejGuwCp337ZB9lxu?usp=drive_link)

Place it inside:
dataset/PlantVillage/

## Project Structure

Plant-Disease-Detection-CNN/
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── dataset/


## Technologies Used
- Python  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  
- Scikit-learn  

## Model Architecture
The CNN model consists of the following layers:

- Convolutional layers for feature extraction  
- ReLU activation function for non-linearity  
- MaxPooling layers for dimensionality reduction  
- Flatten layer to convert feature maps into a vector  
- Fully connected dense layer  
- Output layer with Softmax activation for multi-class classification  

## Experimental Setup
- Image size: 128 × 128  
- Batch size: 32  
- Epochs: 5–10  
- Optimizer: Adam  
- Loss function: Sparse Categorical Crossentropy  

## Training
To train the model, run:
python train.py


The trained model will be saved as `plant_model.h5`.

## Prediction
To test the model on a new image, run:
python predict.py


Update the image path in `predict.py` before running.

## Evaluation
Model performance is evaluated using a confusion matrix.

- Diagonal elements represent correct predictions  
- Off-diagonal elements represent misclassifications  
- Higher diagonal values indicate better performance

  ## How to Run

1. Install dependencies
pip install -r requirements.txt

2. Train model
python train.py

3. Run prediction
python predict.py

## Results
The model achieves high accuracy in classifying plant diseases.

## Output Screenshots

### Prediction Result
<img width="444" height="491" alt="Screenshot 2026-04-14 at 8 20 52 PM" src="https://github.com/user-attachments/assets/630f6ba5-d18e-43c0-980a-a1f321702177" />

### Confusion Matrix
<img width="516" height="432" alt="image" src="https://github.com/user-attachments/assets/ff9d788f-f79a-4a1b-b79b-dd443c78e2f4" />

Example prediction:
- Predicted Class: Tomato Late Blight  
- Confidence: 1.00  

## Conclusion

The CNN model successfully classifies plant diseases with high accuracy. 
This system can assist farmers and researchers in early disease detection and improve agricultural productivity.

## Requirements
Install dependencies using:
pip install -r requirements.txt


## Notebook
[https://colab.research.google.com/your-notebook-link](https://colab.research.google.com/drive/1l6j4UWF4iHGzr80HAgqBosvYfJbe7RMv?usp=sharing)
