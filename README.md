# 🛡️ NoCaptcha_MLOps

Welcome to **NoCaptcha_MLOps**! 🎉 This project is your new favorite superhero against CAPTCHA abuse. Think of it as the Batman of the internet, but instead of batarangs, we’re using machine learning pipelines! 🦇🤖

## Demo: [nocaptcha.tech](https://nocaptcha.tech)

---

## 📜 Project Overview

### What is NoCaptcha_MLOps? 🤔

NoCaptcha_MLOps is a machine learning-based solution that combats CAPTCHA abuse with style and precision. Imagine a bouncer at a fancy club, but for your website. It detects shady bots, gives them a polite "nope," and ensures your website stays bot-free and fabulous. 💃

### Why NoCaptcha_MLOps? 🌟

CAPTCHAs are the internet’s version of "Are you a robot?" But let’s face it—some bots are just too clever. That’s where we step in. This project beefs up CAPTCHA security with machine learning, turning your CAPTCHA into Fort Knox. Let’s make the web a safer (and cooler) place! 🌐

---

## 🚀 How to Run This Project

### Prerequisites 📋

Before embarking on this exciting journey, make sure you’ve packed these essentials:

- [Docker](https://docs.docker.com/get-docker/) 🐳 (the ship that carries your app!)
- [Docker Compose](https://docs.docker.com/compose/) (the crew that runs the ship!)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (because cloud magic doesn’t happen on its own)
- [Git](https://git-scm.com/) (the trusty time machine for your code)

### Steps to Run the Project 🏃‍♂️

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Sidharthareddy99/NoCaptcha_MLops.git
   cd NoCaptcha_MLops
   ```

2. **Set up environment variables**:
   - Create a `.env` file in the root directory and spill some secrets (safely, of course):
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
   - Fire up your browser and head to:
     ```sh
     http://localhost:8000
     ```

---

## 🛠️ Project Structure

Here’s how the magic happens:

```plaintext
NoCaptcha_MLops/
├── app.py                   # FastAPI application (our star player)
├── Dockerfile               # Dockerfile for building the app
├── docker-compose.yml       # Docker Compose file (the maestro)
├── requirements.txt         # Python dependencies (because every magician needs tools)
├── src/
│   ├── NoCaptcha_MLOps/
│   │   ├── components/
│   │   │   ├── data_ingestion.py       # Data: Collected.
│   │   │   ├── data_preprocessing.py   # Data: Cleaned.
│   │   │   ├── data_training.py        # Data: Smarter.
│   │   │   └── prediction_pipeline.py  # Data: Predictive.
│   │   ├── config/
│   │   │   └── configuration.py        # Configuration wizard
│   │   └── pipeline/
│   │       ├── training_pipeline.py    # Training magic
│   │       └── prediction_pipeline.py  # Prediction powerhouse
└── .env                     # Environment variables (top-secret stuff)
```

---

## 🤖 CI/CD Pipeline

Meet our always-on-duty butler, **GitHub Actions**:

### Features:
- **Continuous Integration**:
  - Linting and unit testing every time you push to the `main` branch (because bugs aren’t invited to this party).
- **Continuous Delivery**:
  - Builds and pushes Docker images to Amazon ECR (your app’s cloud chauffeur).
- **Continuous Deployment**:
  - Deploys the latest Docker image to a self-hosted runner (the final destination!).

---

## 🎉 Contributing

Want to join the fun? Here’s how:

1. Fork the repository (make it yours for a bit).
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Add your awesome changes (`git commit -m 'Add some feature'`).
4. Push to your branch (`git push origin feature/YourFeatureName`).
5. Open a pull request (the internet thanks you in advance).

Together, let’s make CAPTCHA abuse a thing of the past! 🌐

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). That means you’re free to use, modify, and share it—just don’t forget to give credit where it’s due. 😊

---

## 📞 Contact

Got questions? Need help? Or just want to say hi? Reach out!

- **Email**: [sidharthreddy114@gmail.com](mailto:sidharthreddy114@gmail.com)

---

Thank you for checking out **NoCaptcha_MLOps**! 🚀 Now go forth and make the internet a safer, bot-free place! 🎉

