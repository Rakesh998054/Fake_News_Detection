# AI-Powered Fake News Detection Using Text Classification

## Deployed in Streamlit app : https://ai-power-fake-news-detection.streamlit.app/ .

## Project Overview

Fake news is a major problem in today's digital world. This project uses Artificial Intelligence and Machine Learning techniques to automatically classify news articles as **Fake News** or **Real News**.

The system uses Natural Language Processing (NLP) techniques to clean and convert news text into numerical features and applies Machine Learning algorithms to detect misinformation.

---

## Objectives

- Detect whether a news article is fake or real
- Apply NLP techniques for text preprocessing
- Convert text data into numerical form using TF-IDF
- Train multiple Machine Learning models
- Compare model performance using evaluation metrics

---

## Dataset Description

This project uses the Fake News Detection Dataset.

The dataset contains two files:

### 1. Fake.csv
Contains fake news articles.

Features:

- title: Title of the news article
- text: Full news content
- subject: Category of news
- date: Date of publication

Label:

- 0 → Fake News


### 2. True.csv
Contains real news articles.

Features:

- title: Title of the news article
- text: Full news content
- subject: Category of news
- date: Date of publication

Label:

- 1 → Real News

The two datasets are combined and used for machine learning classification.

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Machine Learning Algorithms

---

## Machine Learning Algorithms Used

### 1. K-Nearest Neighbor (KNN)
A non-parametric algorithm that classifies news based on similarity with existing examples.

### 2. Logistic Regression
A supervised learning algorithm used for binary classification.

### 3. Random Forest
An ensemble learning algorithm that uses multiple decision trees for prediction.

### 4. Neural Network
A deep learning model used to learn complex patterns in text data.


<img width="1364" height="644" alt="real" src="https://github.com/user-attachments/assets/5a8cd55c-67b0-41fc-a726-1f96b2cbaff6" />

<br><br><br>

<img width="1366" height="641" alt="fake" src="https://github.com/user-attachments/assets/e9b5d976-4210-437e-b7aa-bbe87052b1ec" />


---





