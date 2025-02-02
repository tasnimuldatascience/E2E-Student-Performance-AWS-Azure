# Student Performance Indicator with AWS EC2 Deployment

This project predicts students' math scores based on demographic and academic factors using machine learning. The system includes data ingestion, transformation, training, and a web interface for making predictions. The application is deployed on **AWS EC2**, allowing for scalable and customizable hosting of the web application.

## Project Overview
The **Student Performance Indicator** leverages machine learning to predict students' math scores based on various features such as gender, race/ethnicity, parental education level, lunch type, test preparation course, and reading/writing scores.

The implementation consists of:
1. **Data Ingestion** – Loading and splitting the dataset.
2. **Data Transformation** – Handling missing values and encoding categorical variables.
3. **Model Training** – Training multiple regression models to predict math scores.
4. **Web Application** – Deploying the trained model using Flask for user interaction.
5. **AWS EC2 Deployment** – Hosting the application on an EC2 instance.

---

## Features
- **Automated data preprocessing** (missing value handling, encoding categorical features, feature scaling)
- **Multiple machine learning models** with hyperparameter tuning
- **Evaluation and selection of the best-performing model**
- **Web application for real-time predictions**
- **Customizable deployment using AWS EC2**

---

## Project Structure

```
AWS-CI-CD/
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
│── .gitignore             # Files and folders to ignore in version control
│── app.py                 # Flask application entry point
│── Dockerfile             # Docker configuration for containerizing the application
│── requirements.txt       # Required Python packages
│── setup.py               # Script for packaging and distributing the application
│── README.md              # Project documentation
```

---

## Deployment on AWS EC2

### **Prerequisites**
Ensure you have the following:
- **AWS CLI** installed and configured
- An **EC2 instance** with:
  - Security group allowing inbound traffic on ports 22 (SSH) and 5000 (Flask)
  - Key pair for SSH access

### **Steps for Deployment**

1. **Launch an EC2 Instance**
   - Use the AWS Management Console or CLI to launch an EC2 instance.
   - Choose an Ubuntu AMI and configure security group rules.

2. **Connect to the Instance**
   ```bash
   ssh -i "your-key.pem" ubuntu@your-ec2-public-ip
   ```

3. **Update and Install Dependencies**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip docker.io git -y
   ```

4. **Clone the Repository**

5. **Build and Run the Docker Container**
   - Build the image:
     ```bash
     sudo docker build -t student-performance-app .
     ```
   - Run the container:
     ```bash
     sudo docker run -d -p 5000:5000 student-performance-app
     ```

6. **Access the Application**
   - Open a browser and navigate to `http://<your-ec2-public-ip>:5000/`

7. **(Optional) Configure CI/CD Pipeline**
   - Use the `.github` workflows for automated testing and deployment.

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
- **AWS EC2** (Cloud hosting and deployment)
- **Docker** (Containerization)
- **Logging & Exception Handling** (Custom logging and error handling)
