# Student Performance Indicator with AWS Elastic Beanstalk Deployment

This project aims to predict students' math scores based on demographic and academic factors using machine learning. The system includes data ingestion, transformation, training, and a web interface for making predictions. The application is deployed using **AWS Elastic Beanstalk**, allowing for scalable and managed hosting of the web application.

## Project Overview
The **Student Performance Indicator** leverages machine learning to predict students' math scores based on various features such as gender, race/ethnicity, parental education level, lunch type, test preparation course, and reading/writing scores.

The implementation consists of:
1. **Data Ingestion** – Loading and splitting the dataset.
2. **Data Transformation** – Handling missing values and encoding categorical variables.
3. **Model Training** – Training multiple regression models to predict math scores.
4. **Web Application** – Deploying the trained model using Flask for user interaction.
5. **AWS Elastic Beanstalk Deployment** – Hosting the application on AWS with managed infrastructure.

---

## Features
- **Automated data preprocessing** (missing value handling, encoding categorical features, feature scaling)
- **Multiple machine learning models** with hyperparameter tuning
- **Evaluation and selection of the best-performing model**
- **Web application for real-time predictions**
- **Scalable deployment using AWS Elastic Beanstalk**

---

## Project Structure

```
Student-Performance-Indicator/
│── src/
│   ├── components/
│   │   ├── data_ingestion.py  # Handles data loading and train-test split
│   │   ├── data_transformation.py  # Data preprocessing and transformation
│   │   ├── model_trainer.py  # Training machine learning models
│   ├── pipeline/
│   │   ├── predict_pipeline.py  # Prediction pipeline for web app
│   ├── exception.py  # Custom error handling
│   ├── logger.py  # Logging setup
│   ├── utils.py  # Utility functions for model evaluation and saving objects
│── artifacts/  # Stores processed data and trained models
│── templates/
│   ├── home.html  # Web interface for prediction
│   ├── index.html  # Landing page
│── notebooks/  # Jupyter notebooks for analysis
│── .github/workflows/  # CI/CD pipelines for automated testing and deployment
│── .ebextensions/  # Configuration files for AWS Elastic Beanstalk deployment
│── setup.py  # Script for packaging and distributing the application
│── application.py  # Flask application entry point for AWS Elastic Beanstalk
│── requirements.txt  # Required Python packages
│── README.md  # Project documentation
│── Procfile  # Specifies application execution commands for AWS deployment
│── .elasticbeanstalk/  # AWS EB CLI configuration files
```

## Deployment on AWS Elastic Beanstalk

### **Prerequisites**
Ensure you have the following installed:
- **AWS CLI**
- **Elastic Beanstalk CLI**
- **Python 3.x**
- **Virtual Environment (venv)**

### **Deploying the Application**

1. **Initialize Elastic Beanstalk**
   ```bash
   eb init -p python-3.x student-performance-indicator
   ```
2. **Create and Deploy the Environment**
   ```bash
   eb create student-performance-env
   ```
3. **Deploy the Application**
   ```bash
   eb deploy
   ```
4. **Check the Application Status**
   ```bash
   eb status
   ```
5. **Open the Deployed Application**
   ```bash
   eb open
   ```

---

## Dataset

The dataset contains student performance records with the following attributes:
- **Gender**
- **Race/Ethnicity**
- **Parental Level of Education**
- **Lunch Type (Standard/Free-Reduced)**
- **Test Preparation Course (Completed/None)**
- **Reading Score**
- **Writing Score**
- **Math Score (Target Variable)**

---

## Model Training
- Models used: **Random Forest, Decision Tree, Gradient Boosting, XGBoost, CatBoost, AdaBoost, Linear Regression**
- The best model is selected based on **R² score**.

---

## Web Application

The web interface allows users to enter student attributes and receive a predicted math score.

### **Endpoints**
- `/` – Home page
- `/predictdata` – Prediction form

---

## Technologies Used
- **Python** (pandas, NumPy, scikit-learn)
- **Machine Learning** (Regression models)
- **Flask** (Web framework)
- **AWS Elastic Beanstalk** (Cloud hosting and deployment)
- **Logging & Exception Handling** (Custom logging and error handling)
