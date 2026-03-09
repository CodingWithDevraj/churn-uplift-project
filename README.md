---

# 🌾 AgriIntel — AI-Driven Crop Yield Prediction & Farm Decision Support System

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-ScikitLearn-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

AgriIntel is an **end-to-end machine learning system** designed to predict **cotton production using environmental and economic factors** such as rainfall, temperature, and cultivation cost.

The project integrates **multiple agricultural datasets**, builds a **predictive ML model**, and deploys it through an **interactive Streamlit dashboard** that enables users to estimate crop production under different farming conditions.

This project demonstrates how **AI and data science can support precision agriculture and data-driven farm planning.**

---

# 🚀 Live Demo

🔗 Streamlit App
[https://agriintel-crop-yield-prediction-hcd6cnnizm4ypzymfqdnpc.streamlit.app/](https://agriintel-crop-yield-prediction-hcd6cnnizm4ypzymfqdnpc.streamlit.app/)

---

# 📌 Problem Statement

Agricultural productivity is influenced by several **dynamic environmental and economic factors**, including:

* Rainfall patterns
* Temperature fluctuations
* Cultivation costs
* Market conditions

However, farmers and agricultural planners often lack **predictive tools that combine these variables into actionable insights.**

Without predictive analytics:

• Crop production planning becomes uncertain
• Resource allocation becomes inefficient
• Risk management becomes difficult

This project aims to build a **data-driven crop yield prediction system** capable of estimating agricultural output using historical agricultural data.

---

# 🧠 Solution Overview

AgriIntel provides a **machine learning–based decision support system** that predicts cotton production using historical agricultural data.

The system workflow includes:

1️⃣ **Multi-dataset integration**
2️⃣ **Feature engineering for environmental indicators**
3️⃣ **Machine learning model training**
4️⃣ **Deployment through an interactive dashboard**

Users can input environmental conditions and receive **real-time crop production predictions.**

---

# 🏗 System Architecture

```
Agricultural Datasets
(Crop Production, Rainfall, Temperature, Labor Cost, Market Price)
            │
            ▼
Data Cleaning & Preprocessing
(Pandas, NumPy)
            │
            ▼
Feature Engineering
(Rain Efficiency, Interaction Features)
            │
            ▼
Model Training
(Linear Regression, Random Forest)
            │
            ▼
Model Evaluation
(R² Score, RMSE)
            │
            ▼
Prediction System
(Streamlit Dashboard)
            │
            ▼
Agricultural Decision Support
```

This architecture reflects a **typical industry ML pipeline used in production analytics systems.**

---

# 📊 Datasets Used

The project integrates **multiple agricultural datasets** to capture environmental conditions affecting crop production.

### Crop Production Dataset

* State-wise cotton production data
* Area cultivated and yield statistics

### Rainfall Dataset

* Historical rainfall patterns across Indian regions

### Temperature Dataset

* Daily temperature data for major cities

### Labor Cost Dataset

* Agricultural cultivation cost statistics

### Cotton Price Dataset

* Market price trends for cotton

All datasets were **cleaned, aligned, and merged** into a unified ML dataset.

---

# ⚙️ Data Processing Pipeline

The project follows a structured data pipeline:

1️⃣ Data Cleaning
2️⃣ Feature Engineering
3️⃣ Dataset Integration
4️⃣ Time Alignment Across Datasets
5️⃣ Model Training
6️⃣ Model Evaluation
7️⃣ Dashboard Deployment

This pipeline ensures **data quality, model reliability, and reproducibility.**

---

# 🧠 Machine Learning Models

Two regression models were trained and evaluated.

### Linear Regression

Captures relationships between crop production and environmental variables.

### Random Forest Regressor

An ensemble learning method capable of modeling **non-linear relationships and feature interactions.**

---

# 📈 Model Performance

| Model             | R² Score | RMSE |
| ----------------- | -------- | ---- |
| Linear Regression | **0.91** | 187  |
| Random Forest     | 0.87     | 221  |

The **Linear Regression model achieved the highest accuracy** and was selected for deployment.

---

# 🤖 Prediction Logic

The prediction system estimates cotton production using the following input variables:

* Rainfall
* Average Temperature
* Cultivation Cost
* Rainfall–Temperature Interaction
* Rain Efficiency Index

These engineered features help the model **capture environmental relationships affecting crop productivity.**

---

# 🖥 Interactive Dashboard

An interactive **Streamlit web dashboard** was developed to demonstrate the prediction system.

Users can input environmental conditions and obtain **real-time crop production estimates.**

### Dashboard Features

• Clean and intuitive interface
• Real-time prediction system
• Project methodology explanation
• Technical overview of models and datasets

The dashboard acts as a **prototype decision support tool for agritech platforms.**

---

# 🛠 Technology Stack

| Category         | Tools               |
| ---------------- | ------------------- |
| Programming      | Python              |
| Data Processing  | Pandas, NumPy       |
| Machine Learning | Scikit-Learn        |
| Visualization    | Matplotlib, Seaborn |
| Web Application  | Streamlit           |
| Version Control  | GitHub              |

---

# 📂 Project Structure

```
AgriIntel
│
├── data
│   ├── crop_production.csv
│   ├── rainfall.csv
│   ├── temperature.csv
│   ├── labor.csv
│   └── cotton_price.csv
│
├── notebooks
│   └── data_analysis.ipynb
│
├── models
│   └── crop_yield_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ▶️ Running the Project

### Install dependencies

```
pip install -r requirements.txt
```

### Run the Streamlit dashboard

```
streamlit run app.py
```

The application will launch locally in your browser.

---

# 📈 Skills Demonstrated

This project demonstrates key **data science and machine learning competencies**:

• Data Cleaning & Preprocessing
• Feature Engineering
• Multi-dataset Integration
• Machine Learning Model Development
• Model Evaluation & Validation
• Interactive Dashboard Development
• End-to-End ML Pipeline Design

---

# 🔮 Future Improvements

Potential enhancements include:

• Integration of **satellite NDVI vegetation data**
• Soil moisture and soil quality datasets
• Multi-crop prediction models
• Deployment as a **cloud-based API**
• Integration with **real-time weather APIs**

---

# 💡 Potential Applications

AgriIntel can support:

• Precision agriculture platforms
• Agritech analytics systems
• Smart farming advisory tools
• Agricultural robotics planning
• Government agricultural policy planning

---

# 👨‍💻 Author

**Devraj Choudhary**

B.Tech – Computer Science & Engineering
Gurukul Kangri Deemed to be University

Interests
• Data Science
• Machine Learning
• AI for Agriculture

GitHub
[https://github.com/CodingWithDevraj](https://github.com/CodingWithDevraj)

LinkedIn
[https://www.linkedin.com/in/devraj-choudhary-3889412bb/](https://www.linkedin.com/in/devraj-choudhary-3889412bb/)

---

