# 👁️ OCT Diagnosis using Deep Learning

A Deep Learning-based web application that detects and classifies **retinal diseases** from OCT (Optical Coherence Tomography) eye scans. This project is built using **PyTorch** for the backend model and *Streamlit* for the interactive frontend.

🔗 **Live Demo**: [Click to Open App](https://oct-diagnosis-napu3yjhkcntywwtmx3mhn.streamlit.app/)

---

## ❓ Problem Statement

With the advancement of imaging technologies in ophthalmology, **millions of OCT (Optical Coherence Tomography) scans are generated globally each year** to detect and monitor retinal diseases. However, analyzing these scans manually requires time, clinical expertise, and resources — making it difficult to serve remote or under-resourced areas.

This project provides an **automated, AI-powered solution** that:
- Speeds up the **diagnosis process**
- Reduces the **workload of ophthalmologists**
- Improves **early detection and treatment** of critical eye diseases
- Makes diagnosis **accessible** via a lightweight and interactive web interface

---

## 📌 Table of Contents

- [✨ Features](#-features)
- [📂 Dataset](#-dataset)
- [📊 Model Architecture](#-model-architecture)
- [🚀 How to Use](#-how-to-use)

---

## ✨ Features

- 📤 Upload OCT images and get instant diagnosis.
- 🔍 Classifies into four categories:
  - CNV (Choroidal Neovascularization)
  - DME (Diabetic Macular Edema)
  - Drusen
  - Normal
- ⚙️ Image preprocessing and model inference with PyTorch.
- 🌙 Clean and responsive **dark mode UI** with loading animations.
- 🧪 Easy to extend with new models or features.

---

## 📂 Dataset

The dataset used is from **Kaggle's OCT & OCT Angiography** dataset:

- 🔗 [Original Dataset](https://www.kaggle.com/datasets/paultimothymooney/kermany2018)
- Contains 4 classes:
  - **CNV**, **DME**, **Drusen**, and **Normal**
- Each image is a retina OCT scan (grayscale or RGB)
- Used a balanced subset for training

---

## 📊 Model Architecture

- Backbone: Custom **Convolutional Neural Network (CNN)**
- Output: 4-class softmax
- Activation: ReLU and Softmax
- Trained with **CrossEntropyLoss** and **Adam optimizer**

> 🔍 The model was saved using `model.state_dict()` and later reloaded for prediction in the deployed app.

---

## 🚀 How to Use

### 🔗 Try the Web App
Visit the live app here:  
👉 **[https://oct-diagnosis-napu3yjhkcntywwtmx3mhn.streamlit.app](https://oct-diagnosis-napu3yjhkcntywwtmx3mhn.streamlit.app)**

### 🧪 Local Setup (Optional)

```bash
git clone https://github.com/yourusername/oct-diagnosis.git
cd oct-diagnosis
pip install -r requirements.txt
streamlit run app.py
