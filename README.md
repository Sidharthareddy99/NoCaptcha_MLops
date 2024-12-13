# 🛡️ NoCaptcha_MLOps

Welcome to the **NoCaptcha_MLOps** project! 🎉 This project is designed to build a robust machine learning pipeline to detect and prevent CAPTCHA abuse. Dive in to learn more and contribute to making the internet a safer place! 🌐

---

## 📜 Project Overview

### What is NoCaptcha_MLOps? 🤔

NoCaptcha_MLOps is a machine learning-based solution aimed at detecting and preventing CAPTCHA abuse. By combining data ingestion, preprocessing, training, and deployment pipelines, we create a reliable system to identify and block suspicious activities effectively.

### Why NoCaptcha_MLOps? 🌟

CAPTCHAs are essential for protecting websites from bots and automated abuse. However, advanced bots can sometimes bypass traditional CAPTCHA mechanisms. This project enhances CAPTCHA security by using machine learning to proactively identify and mitigate abuse, ensuring safer online experiences for everyone. 🌐

---

## 🚀 How to Run This Project

### Prerequisites 📋

Before running this project, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/) 🐳
- [Docker Compose](https://docs.docker.com/compose/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (configured with your credentials)
- [Git](https://git-scm.com/)

### Steps to Run the Project 🏃‍♂️

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Sidharthareddy99/NoCaptcha_MLops.git
   cd NoCaptcha_MLops
   ```

2. **Set up environment variables**:
   - Create a `.env` file in the root directory and add the following variables:
     ```env
     DAGSHUB_USER=your_dagshub_username
     DAGSHUB_TOKEN=your_dagshub_token
     AWS_ACCESS_KEY_ID=your_aws_access_key_id
     AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
     AWS_REGION=your_aws_region
     MONGO_URI=your_mongo_uri
     DATABASE_NAME=your_database_name
     COLLECTION_NAME=your_collection_name
     ```

3. **Build and run the Docker containers**:
   ```sh
   docker-compose up --build
   ```

4. **Access the application**:
   - Open your browser and go to:
     ```sh
     http://localhost:8000
     ```

---

## 🛠️ Project Structure

Here’s a quick overview of the project structure:

```plaintext
NoCaptcha_MLops/
├── app.py                   # FastAPI application
├── Dockerfile               # Dockerfile for building the app
├── docker-compose.yml       # Docker Compose file
├── requirements.txt         # Python dependencies
├── src/
│   ├── NoCaptcha_MLOps/
│   │   ├── components/
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_preprocessing.py
│   │   │   ├── data_training.py
│   │   │   └── prediction_pipeline.py
│   │   ├── config/
│   │   │   └── configuration.py
│   │   └── pipeline/
│   │       ├── training_pipeline.py
│   │       └── prediction_pipeline.py
└── .env                     # Environment variables
```

---

## 🤖 CI/CD Pipeline

Our project includes a robust CI/CD pipeline using GitHub Actions:

### Features:
- **Continuous Integration**:
  - Linting and running unit tests on every push to the `main` branch.
- **Continuous Delivery**:
  - Building and pushing Docker images to Amazon ECR.
- **Continuous Deployment**:
  - Deploying the latest Docker image to a self-hosted runner.

---

## 🎉 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

Let’s collaborate to make the internet safer! 🌐

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the license terms.

---

## 📞 Contact

If you have any questions or need support, feel free to reach out:

- **Email**: [sidharthreddy114@gmail.com](mailto:sidharthreddy114@gmail.com)

---

Thank you for exploring **NoCaptcha_MLOps**! 🚀

