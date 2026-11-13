# Laptop Price Prediction Using Machine Learning

## Project Overview

This project focuses on predicting laptop price categories using Machine Learning techniques. It analyzes laptop specifications such as company, processor, RAM, storage, screen size, and weight to classify laptops into three price categories: Low, Medium, and High.

An interactive web application is developed using Streamlit to allow users to enter laptop specifications and receive price category predictions.

## Objectives

- Explore and analyze laptop price data.
- Perform data preprocessing and feature engineering.
- Apply feature scaling and Principal Component Analysis (PCA).
- Train and compare multiple Machine Learning models.
- Evaluate model performance.
- Develop an interactive prediction application using Streamlit.

## Dataset

**Dataset:** Laptop Price Dataset (`laptop_price.csv`)

The dataset contains 1,303 laptop records with 13 original columns, including:

- Company
- Product
- TypeName
- Inches
- ScreenResolution
- CPU
- RAM
- Memory
- GPU
- Operating System
- Weight
- Price (Euros)

The target variable is `Price_Category`, divided into:
- Low
- Medium
- High

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- PCA
- Streamlit
- Joblib
- Google Colab

## Machine Learning Models

Three classification algorithms were implemented:

1. Decision Tree Classifier
2. Random Forest Classifier
3. Gradient Boosting Classifier

The models were compared using accuracy, precision, recall, and F1-score.

## Project Workflow

1. Data Collection and Loading
2. Data Exploration
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature Scaling
6. Dimensionality Reduction using PCA
7. Model Training
8. Model Comparison and Evaluation
9. Streamlit Web Application Development

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Laptop-Price-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Laptop-Price-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Application Features

- Interactive laptop specification inputs.
- Machine Learning-based price category prediction.
- Easy-to-use Streamlit interface.
- Three output categories: Low, Medium, and High.

## Screenshots

Application screenshots will be added here.

## Project Information

**Project Title:** Laptop Price Prediction Using Machine Learning

**Domain:** Data Science and Machine Learning

**Tools:** Python, Scikit-learn, Streamlit

---

⭐ If you find this project useful, feel free to star the repository!
