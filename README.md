# Student Performance Indicator Projects

This repository contains three independent projects, each focused on predicting students' math scores using machine learning. Each project showcases a different deployment method to demonstrate scalability, automation, and flexibility in various cloud environments.

---

## Project Overview
The **Student Performance Indicator** predicts students' math scores based on demographic and academic features, such as:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading and Writing Scores

Each project follows these general steps:
1. **Data Ingestion** – Loading and splitting the dataset.
2. **Data Transformation** – Handling missing values and encoding categorical variables.
3. **Model Training** – Training multiple regression models to predict math scores.
4. **Web Application** – A Flask-based web app for making predictions.
5. **Deployment** – Using different strategies for hosting and scalability.

---

## Project Structure

```
E2E-Student-Performance-Indicator/
│── AWS-EB-CI-CD/             # Deployment using AWS Elastic Beanstalk with CI/CD
│── AWS-EC2-CI-CD/            # Deployment using AWS EC2 with CI/CD
│── Azure-deployment/         # Deployment on Azure using Docker
```

---

## Deployment Methods

### 1. **AWS Elastic Beanstalk with CI/CD**
- **Purpose:** Simplified deployment with managed hosting.
- **Features:** Automated integration via GitHub Actions and Elastic Beanstalk configurations.
- **Setup:** Found in `AWS-EB-CI-CD/`.

### 2. **AWS EC2 with CI/CD**
- **Purpose:** Manual deployment for flexible infrastructure control.
- **Features:** Dockerized application deployed on EC2 with CI/CD pipelines.
- **Setup:** Found in `AWS-EC2-CI-CD/`.

### 3. **Azure Deployment with Docker**
- **Purpose:** Containerized deployment using Azure Web Apps.
- **Features:** Uses Azure Container Registry and Web Apps for managed hosting.
- **Setup:** Found in `Azure-deployment/`.

---

## Prerequisites
To work with these projects, ensure you have the following tools installed:
- **AWS CLI** (for Elastic Beanstalk and EC2 deployments)
- **Azure CLI** (for Azure deployments)
- **Docker** (for containerization)
- **Python 3.x** (for running the applications)
- **Git** (for version control and CI/CD workflows)

---

## Getting Started

### **1. Clone the Repository**

### **2. Navigate to the Desired Deployment Folder**
For example, to work on the AWS Elastic Beanstalk deployment:
```bash
cd AWS-EB-CI-CD
```

### **3. Follow the Deployment Instructions**
Each folder contains a `README.md` file with specific instructions for deploying that project.

---

## Technologies Used
- **Python** (pandas, NumPy, scikit-learn)
- **Flask** (Web framework)
- **Docker** (Containerization)
- **AWS** (Elastic Beanstalk, EC2)
- **Azure** (Web Apps with Docker)
- **GitHub Actions** (CI/CD workflows)