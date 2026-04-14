![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

# Plant Disease Detection using CNN

A deep learning project that detects plant diseases from leaf images using a Convolutional Neural Network (CNN). The model is trained on the PlantVillage dataset and can classify multiple plant diseases with high accuracy.

---

## Project Demo

Prediction Example:

<img width="523" height="478" alt="Screenshot 2026-04-14 at 8 56 48 PM" src="https://github.com/user-attachments/assets/af9b14e0-680d-4f2e-84ed-f69d10d1b65f" />

Confusion Matrix:

<img width="516" height="432" alt="image" src="https://github.com/user-attachments/assets/a33c4bf0-5f5f-463b-9be4-4a095cfb291e" />


---

## Features

- Image-based plant disease detection  
- Multi-class classification (healthy and diseased leaves)  
- CNN-based deep learning model  
- High accuracy predictions  
- Confusion matrix evaluation  
- Works on unseen images  

---

## Dataset

This project uses the PlantVillage dataset.

Due to size limitations, the dataset is not included.

Download it from:
https://www.kaggle.com/datasets/emmarex/plantdisease  

After downloading, place it in:
dataset/PlantVillage/


---

## Tech Stack

- Python  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  
- Scikit-learn  

---

## Model Architecture

- Convolutional Layers  
- ReLU Activation  
- MaxPooling Layers  
- Flatten Layer  
- Dense Layers  
- Softmax Output  

---

## Project Structure
Plant-Disease-Detection-using-CNN/
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
├── plant_disease_detection.ipynb
└── dataset/


---

## Installation

Clone the repository:

git clone https://github.com/sarnika09-cell/Plant-Disease-Detection-using-CNN.git
cd Plant-Disease-Detection-using-CNN


Install dependencies:
pip install -r requirements.txt


---

## Usage

Train the model:
python train.py

Run prediction:
python predict.py


---

## Results

- Achieved high accuracy on validation data  
- Successfully classified plant diseases  
- Example: Tomato Late Blight with high confidence  

---

## Future Improvements

- Add data augmentation  
- Deploy as web/mobile app  
- Use advanced architectures (ResNet, EfficientNet)  

---

## Author

Sarnika  
