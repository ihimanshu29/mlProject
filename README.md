## End to End ML Project: House Price Predictor (Deployed)

### 📦 Dockerized Flask App with ML Model
- Trained on housing data
- Predicts house prices in real-time
- Built with: Python, Flask, Scikit-learn
- Containerized with Docker
- Deployed on Render

👉 **Live Demo**: [https://mlapp.onrender.com](https://mlapp.onrender.com)

### ⚙️ To Run Locally:
```bash
git clone ...
docker build -t ml-app .
docker run -p 5000:5000 ml-app
