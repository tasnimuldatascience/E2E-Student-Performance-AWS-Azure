# Student Performance Indicator with Azure Web App Deployment

This project predicts students' math scores based on demographic and academic factors using machine learning. The system includes data ingestion, transformation, training, and a web interface for making predictions. The application is deployed using **Azure Web Apps** with Docker, allowing for scalable and managed hosting of the web application.

## Project Overview
The **Student Performance Indicator** leverages machine learning to predict students' math scores based on various features such as gender, race/ethnicity, parental education level, lunch type, test preparation course, and reading/writing scores.

The implementation consists of:
1. **Data Ingestion** – Loading and splitting the dataset.
2. **Data Transformation** – Handling missing values and encoding categorical variables.
3. **Model Training** – Training multiple regression models to predict math scores.
4. **Web Application** – Deploying the trained model using Flask for user interaction.
5. **Azure Web App Deployment with Docker** – Hosting the application on Azure using a Docker container.

---

## Features
- **Automated data preprocessing** (missing value handling, encoding categorical features, feature scaling)
- **Multiple machine learning models** with hyperparameter tuning
- **Evaluation and selection of the best-performing model**
- **Web application for real-time predictions**
- **Scalable deployment using Azure Web Apps with Docker**

---

## Project Structure

```
Azure-deployment/
│── .github/               # CI/CD pipelines for automated testing and deployment
│── artifacts/             # Stores processed data and trained models
│── notebook/              # Jupyter notebooks for analysis
│── src/                   # Core source code
│   ├── components/        # Data ingestion, transformation, and model training scripts
│   ├── pipeline/          # Prediction pipeline for web app
│   ├── logger.py          # Logging setup
│   ├── exception.py       # Custom error handling
│   ├── utils.py           # Utility functions for model evaluation and saving objects
│── templates/             # HTML templates for Flask web application
│── app.py                 # Flask application entry point
│── Dockerfile             # Docker configuration for containerizing the application
│── requirements.txt       # Required Python packages
│── setup.py               # Script for packaging and distributing the application
│── README.md              # Project documentation
```

---

## Deployment on Azure Web Apps with Docker

### **Prerequisites**
Ensure you have the following installed:
- **Azure CLI**
- **Docker**
- **Python 3.x**
- **Virtual Environment (venv)**

### **Steps for Deployment**

1. **Build the Docker Image**
   ```bash
   docker build -t student-performance-app .
   ```

2. **Test Locally (Optional)**
   ```bash
   docker run -p 5000:5000 student-performance-app
   ```
   Open `http://localhost:5000/` in your browser to test the application.

3. **Login to Azure**
   ```bash
   az login
   ```

4. **Push Docker Image to Azure Container Registry (ACR)**
   - Create an ACR:
     ```bash
     az acr create --resource-group student-performance-rg --name studentPerformanceACR --sku Basic
     ```
   - Login to ACR:
     ```bash
     az acr login --name studentPerformanceACR
     ```
   - Tag and push the image:
     ```bash
     docker tag student-performance-app studentperformanceacr.azurecr.io/student-performance-app
     docker push studentperformanceacr.azurecr.io/student-performance-app
     ```

5. **Create an Azure Web App for Containers**
   ```bash
   az webapp create --resource-group student-performance-rg --plan student-performance-plan --name student-performance-app --deployment-container-image-name studentperformanceacr.azurecr.io/student-performance-app
   ```

6. **Configure and Start the Web App**
   - Update app settings:
     ```bash
     az webapp config appsettings set --resource-group student-performance-rg --name student-performance-app --settings WEBSITES_PORT=5000
     ```
   - Restart the application:
     ```bash
     az webapp restart --name student-performance-app --resource-group student-performance-rg
     ```

7. **Open the Application**
   ```bash
   az webapp browse --name student-performance-app --resource-group student-performance-rg
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
- **Azure Web Apps with Docker** (Cloud hosting and containerization)
- **Logging & Exception Handling** (Custom logging and error handling)
